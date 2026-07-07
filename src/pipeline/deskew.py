import cv2
import numpy as np

from logger import LOGGER
from config import config


class DeskewStep:

    def run(self, job):

        if not config.get("deskew.enabled", True):
            LOGGER.info("Deskew deaktiviert.")
            return job

        LOGGER.info("Deskew wird ausgeführt...")

        for page in job.pages:

            gray = cv2.imread(str(page), cv2.IMREAD_GRAYSCALE)

            _, binary = cv2.threshold(
                gray,
                0,
                255,
                cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
            )

            # ---------- Methode 1 ----------
            points = np.column_stack(np.where(binary > 0))

            rect_angle = 0.0

            if len(points) > 100:

                rect_angle = cv2.minAreaRect(points)[-1]

                if rect_angle < -45:
                    rect_angle = 90 + rect_angle

            # ---------- Methode 2 ----------
            hough_angle = None

            lines = cv2.HoughLinesP(
                binary,
                1,
                np.pi / 180,
                threshold=100,
                minLineLength=300,
                maxLineGap=20,
            )

            if lines is not None:

                angles = []

                for line in lines:

                    line = np.array(line).flatten()

                    if len(line) != 4:
                        continue

                    x1, y1, x2, y2 = line

                    angle = np.degrees(
                        np.arctan2(
                            y2 - y1,
                            x2 - x1
                        )
                    )

                    if -20 < angle < 20:
                        angles.append(angle)

                if angles:
                    hough_angle = float(np.median(angles))

            LOGGER.info(
                f"{page.name}: "
                f"minAreaRect={rect_angle:.2f}° "
                f"Hough={hough_angle}"
            )

        return job
