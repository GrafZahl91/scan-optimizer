import cv2
import numpy as np
from pathlib import Path

from logger import LOGGER
from config import config


class CropStep:

    def run(self, job):

        if not config.get("crop.enabled", True):
            return job

        LOGGER.info("ContentCrop wird ausgeführt...")

        self.margin = config.get("crop.margin", 10)

        self.debug_dir = Path("/debug") / job.name
        self.debug_dir.mkdir(parents=True, exist_ok=True)

        for page in job.pages:

            LOGGER.info(f"{page.name}: analysiere...")

            image = cv2.imread(str(page))

            if image is None:
                LOGGER.warning(f"{page.name}: konnte nicht gelesen werden.")
                continue

            small = self.preprocess(page, image)

            mask = self.create_mask(page, small)

            self.find_content(page, image, mask)

        return job

    def preprocess(self, page, image):

        cv2.imwrite(
            str(self.debug_dir / f"{page.stem}_01_original.png"),
            image,
        )

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        cv2.imwrite(
            str(self.debug_dir / f"{page.stem}_02_gray.png"),
            gray,
        )

        self.scale = 0.25

        small = cv2.resize(
            gray,
            None,
            fx=self.scale,
            fy=self.scale,
            interpolation=cv2.INTER_AREA,
        )

        cv2.imwrite(
            str(self.debug_dir / f"{page.stem}_03_small.png"),
            small,
        )

        return small

    def create_mask(self, page, gray):

        blur = cv2.GaussianBlur(gray, (7, 7), 0)

        cv2.imwrite(
            str(self.debug_dir / f"{page.stem}_04_blur.png"),
            blur,
        )

        blocksize = config.get("crop.threshold_blocksize", 51)
        c = config.get("crop.threshold_c", 15)

        mask = cv2.adaptiveThreshold(
            blur,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY_INV,
            blocksize,
            c,
        )

        cv2.imwrite(
            str(self.debug_dir / f"{page.stem}_05_threshold.png"),
            mask,
        )

        close_kernel = config.get("crop.close_kernel", 15)

        kernel = np.ones((close_kernel, close_kernel), np.uint8)

        mask = cv2.morphologyEx(
            mask,
            cv2.MORPH_CLOSE,
            kernel,
        )

        cv2.imwrite(
            str(self.debug_dir / f"{page.stem}_06_close.png"),
            mask,
        )

        kernel = cv2.getStructuringElement(
            cv2.MORPH_RECT,
            (
                config.get("crop.dilate_horizontal", 45),
                5,
            ),
        )

        mask = cv2.dilate(
            mask,
            kernel,
            iterations=1,
        )

        kernel = cv2.getStructuringElement(
            cv2.MORPH_RECT,
            (
                5,
                config.get("crop.dilate_vertical", 25),
            ),
        )

        mask = cv2.dilate(
            mask,
            kernel,
            iterations=1,
        )

        cv2.imwrite(
            str(self.debug_dir / f"{page.stem}_07_dilate.png"),
            mask,
        )

        open_kernel = config.get("crop.open_kernel", 3)

        kernel = np.ones((open_kernel, open_kernel), np.uint8)

        mask = cv2.morphologyEx(
            mask,
            cv2.MORPH_OPEN,
            kernel,
        )

        cv2.imwrite(
            str(self.debug_dir / f"{page.stem}_08_open.png"),
            mask,
        )

        return mask

    def find_content(self, page, image, mask):

        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE,
        )

        if not contours:
            LOGGER.info(f"{page.name}: keine Konturen gefunden.")
            return

        debug = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

        scale = 1 / self.scale

        min_area = 500

        x1 = mask.shape[1]
        y1 = mask.shape[0]
        x2 = 0
        y2 = 0

        kept = 0

        for contour in contours:

            area = cv2.contourArea(contour)

            if area < min_area:
                continue

            kept += 1

            x, y, w, h = cv2.boundingRect(contour)

            cv2.rectangle(
                debug,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2,
            )

            x1 = min(x1, x)
            y1 = min(y1, y)
            x2 = max(x2, x + w)
            y2 = max(y2, y + h)

        cv2.imwrite(
            str(self.debug_dir / f"{page.stem}_08_contours.png"),
            debug,
        )

        if kept == 0:
            LOGGER.info(f"{page.name}: keine ausreichenden Konturen.")
            return

        x1 = max(int(x1 * scale) - self.margin, 0)
        y1 = max(int(y1 * scale) - self.margin, 0)
        x2 = min(int(x2 * scale) + self.margin, image.shape[1])
        y2 = min(int(y2 * scale) + self.margin, image.shape[0])

        out = image.copy()

        cv2.rectangle(
            out,
            (x1, y1),
            (x2, y2),
            (0, 0, 255),
            8,
        )

        cv2.imwrite(
            str(self.debug_dir / f"{page.stem}_09_box.png"),
            out,
        )

        LOGGER.info(
            f"{page.name}: {kept} Konturen -> Box {x2-x1}x{y2-y1}px"
        )
