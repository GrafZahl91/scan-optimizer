import cv2
import numpy as np
from pathlib import Path

from logger import LOGGER


DEBUG_DIR = Path("/debug/border")
DEBUG_DIR.mkdir(parents=True, exist_ok=True)


class BorderRemovalStep:

    def run(self, job):

        LOGGER.info("BorderRemoval wird ausgeführt...")

        for page in job.pages:

            image = cv2.imread(str(page))

            if image is None:
                LOGGER.warning(f"{page.name}: Bild konnte nicht geladen werden.")
                continue

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            self.detect(page, image, gray)

        return job

    def detect(self, page, image, gray):

        h, w = gray.shape

        debug = image.copy()

        # Messbereich
        offset = 50

        cv2.line(debug, (offset, 0), (offset, h), (0,255,0), 3)
        cv2.line(debug, (w-offset, 0), (w-offset, h), (0,255,0), 3)

        cv2.line(debug, (0, offset), (w, offset), (255,0,0), 3)
        cv2.line(debug, (0, h-offset), (w, h-offset), (255,0,0), 3)

        cv2.imwrite(
            str(DEBUG_DIR / f"{page.stem}_measurement.png"),
            debug,
        )

        left_profile = [
            int(gray[:, x].mean())
            for x in range(min(100, w))
        ]

        right_profile = [
            int(gray[:, w-1-x].mean())
            for x in range(min(100, w))
        ]

        LOGGER.info(
            f"{page.name}: Left profile: "
            + " ".join(map(str, left_profile[:25]))
        )

        LOGGER.info(
            f"{page.name}: Right profile: "
            + " ".join(map(str, right_profile[:25]))
        )
