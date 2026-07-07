import cv2

from logger import LOGGER
from config import config


class CropStep:

    def run(self, job):

        if not config.get("crop.enabled", True):
            LOGGER.info("Crop deaktiviert.")
            return job

        LOGGER.info("AutoCrop wird ausgeführt...")

        margin = config.get("crop.margin", 10)

        for page in job.pages:

            image = cv2.imread(str(page))

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            _, thresh = cv2.threshold(
                gray,
                250,
                255,
                cv2.THRESH_BINARY_INV
            )

            contours, _ = cv2.findContours(
                thresh,
                cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE
            )

            if not contours:
                LOGGER.info(f"{page.name}: keine Kontur gefunden.")
                continue

            contour = max(contours, key=cv2.contourArea)

            x, y, w, h = cv2.boundingRect(contour)

            x = max(0, x - margin)
            y = max(0, y - margin)

            w = min(image.shape[1] - x, w + margin * 2)
            h = min(image.shape[0] - y, h + margin * 2)

            cropped = image[y:y+h, x:x+w]

            cv2.imwrite(str(page), cropped)

            LOGGER.info(
                f"{page.name}: zugeschnitten auf {w}x{h}px"
            )

        return job
