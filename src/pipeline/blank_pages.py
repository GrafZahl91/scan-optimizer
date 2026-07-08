import cv2
import numpy as np

from logger import LOGGER
from config import config


class BlankPageStep:

    def run(self, job):

        LOGGER.info("Analysiere Seiten...")

        border = config.get("blank_page.border", 40)
        dry_run = config.get("blank_page.dry_run", False)

        min_contour = config.get("blank_page.min_contour", 100)
        min_coverage = config.get("blank_page.min_coverage", 0.003)

        job.page_info = []

        for page in job.pages:

            gray = cv2.imread(str(page), cv2.IMREAD_GRAYSCALE)

            if gray is None:
                LOGGER.warning(f"{page.name}: Bild konnte nicht geladen werden.")
                continue

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

            page_area = gray.shape[0] * gray.shape[1]
            coverage = area / page_area if page_area else 0

            status = "KEEP"

            if coverage < min_coverage:
                status = "BLANK"

            if dry_run and status == "BLANK":
                status = "BLANK (dry-run)"

            LOGGER.info(
                f"{page.name}: "
                f"contours={kept} "
                f"area={int(area)} "
                f"coverage={coverage:.3%} "
                f"-> {status}"
            )

            job.page_info.append(
                {
                    "page": page,
                    "status": status
                }
            )

        kept_pages = sum(
            1
            for page in job.page_info
            if page["status"] == "KEEP"
        )

        job.report["pages"] = {
            "total": len(job.page_info),
            "kept": kept_pages,
            "removed": len(job.page_info) - kept_pages,
        }

        return job
