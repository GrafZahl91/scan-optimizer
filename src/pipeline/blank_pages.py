import cv2
import numpy as np

from logger import LOGGER
from config import config


class BlankPageStep:

    def run(self, job):

        LOGGER.info("Analysiere Seiten...")

        border = config.get("blank_page.border", 40)
        dry_run = config.get("blank_page.dry_run", True)

        # Mindestgröße einzelner Konturen
        min_contour = config.get("blank_page.min_contour", 100)

        # Mindestfläche aller Konturen zusammen
        min_area = config.get("blank_page.min_area", 500000)

        job.page_info = []

        for page in job.pages:

            gray = cv2.imread(str(page), cv2.IMREAD_GRAYSCALE)

            h, w = gray.shape

            gray = gray[
                border:h-border,
                border:w-border
            ]

            _, binary = cv2.threshold(
                gray,
                0,
                255,
                cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
            )

            kernel = np.ones((3, 3), np.uint8)

            binary = cv2.morphologyEx(
                binary,
                cv2.MORPH_OPEN,
                kernel
            )

            contours, _ = cv2.findContours(
                binary,
                cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE
            )

            area = 0
            kept = 0

            for c in contours:

                a = cv2.contourArea(c)

                if a < min_contour:
                    continue

                area += a
                kept += 1

            status = "KEEP"

            if area < min_area:
                status = "BLANK"

            if dry_run and status == "BLANK":
                status = "BLANK (dry-run)"

            LOGGER.info(
                f"{page.name}: "
                f"contours={kept} "
                f"area={int(area)} "
                f"-> {status}"
            )

            job.page_info.append(
                {
                    "page": page,
                    "status": status
                }
            )

        return job
