import cv2
import numpy as np

from logger import LOGGER


class BlankPageStep:

    BORDER = 40

    BLACK_THRESHOLD = 2.0
    AREA_THRESHOLD = 500000

    def run(self, job):

        LOGGER.info("Analysiere Seiten...")

        job.page_info = []

        for page in job.pages:

            gray = cv2.imread(str(page), cv2.IMREAD_GRAYSCALE)

            h, w = gray.shape

            gray = gray[
                self.BORDER:h-self.BORDER,
                self.BORDER:w-self.BORDER
            ]

            mean = np.mean(gray)
            std = np.std(gray)

            _, binary = cv2.threshold(
                gray,
                0,
                255,
                cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
            )

            black = np.count_nonzero(binary)
            black_percent = black / binary.size * 100

            contours, _ = cv2.findContours(
                binary,
                cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE
            )

            contour_area = 0

            for contour in contours:
                contour_area += cv2.contourArea(contour)

            status = "KEEP"

            if (
                black_percent < self.BLACK_THRESHOLD
                and contour_area < self.AREA_THRESHOLD
            ):
                status = "BLANK"

            job.page_info.append(
                {
                    "page": page,
                    "mean": mean,
                    "std": std,
                    "black_percent": black_percent,
                    "contour_area": contour_area,
                    "status": status,
                }
            )

            LOGGER.info(
                f"{page.name}: "
                f"black={black_percent:.2f}% "
                f"area={contour_area:.0f} "
                f"-> {status}"
            )

        return job
