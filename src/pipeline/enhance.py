import cv2

from logger import LOGGER
from config import config


class EnhanceStep:

    def run(self, job):

        if not config.get("enhance.enabled", True):
            return job

        LOGGER.info("ImageEnhancement wird ausgeführt...")

        for page in job.pages:

            image = cv2.imread(str(page))

            if image is None:
                continue

            job.debug.save(
                "enhance",
                f"{page.stem}_01_before.png",
                image,
            )

            if config.get("enhance.autocontrast", True):
                image = self.autocontrast(image)

            job.debug.save(
                "enhance",
                f"{page.stem}_02_after.png",
                image,
            )

            cv2.imwrite(str(page), image)

        return job

    def autocontrast(self, image):

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        if config.get("enhance.clahe.enabled", True):

            clip = config.get("enhance.clahe.clip_limit", 2.0)
            grid = config.get("enhance.clahe.tile_grid_size", 8)

            clahe = cv2.createCLAHE(
                clipLimit=clip,
                tileGridSize=(grid, grid),
            )

            gray = clahe.apply(gray)

        else:

            gray = cv2.normalize(
                gray,
                None,
                0,
                255,
                cv2.NORM_MINMAX,
            )

        return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
