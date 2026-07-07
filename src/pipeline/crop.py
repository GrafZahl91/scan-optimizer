import cv2
import numpy as np

from logger import LOGGER
from config import config


class CropStep:

    def run(self, job):

        if not config.get("crop.enabled", True):
            return job

        LOGGER.info("ContentCrop wird ausgeführt...")

        margin = 25

        for page in job.pages:

            image = cv2.imread(str(page))

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            _, thresh = cv2.threshold(
                gray,
                0,
                255,
                cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
            )

            kernel = np.ones((3, 3), np.uint8)
            thresh = cv2.morphologyEx(
                thresh,
                cv2.MORPH_OPEN,
                kernel
            )

            ys, xs = np.where(thresh > 0)

            if len(xs) == 0 or len(ys) == 0:
                LOGGER.info(f"{page.name}: kein Inhalt erkannt.")
                continue

            x1 = max(xs.min() - margin, 0)
            y1 = max(ys.min() - margin, 0)
            x2 = min(xs.max() + margin, image.shape[1])
            y2 = min(ys.max() + margin, image.shape[0])

            debug = image.copy()

            cv2.rectangle(
                debug,
                (x1, y1),
                (x2, y2),
                (0, 0, 255),
                8
            )

            cv2.imwrite(
                f"/debug/{page.stem}-debug.png",
                debug
            )

            LOGGER.info(
                f"{page.name}: ContentBox {x2-x1}x{y2-y1}px"
            )

        return job
