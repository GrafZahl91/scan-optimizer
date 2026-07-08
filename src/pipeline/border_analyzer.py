import cv2
from pathlib import Path

DEBUG_DIR = Path("/debug/border")
DEBUG_DIR.mkdir(parents=True, exist_ok=True)


class BorderAnalyzer:

    def analyze(self, job, page, image, gray):

        h, w = gray.shape

        debug = image.copy()

        offset = 50

        cv2.line(debug, (offset, 0), (offset, h), (0, 255, 0), 3)
        cv2.line(debug, (w - offset, 0), (w - offset, h), (0, 255, 0), 3)
        cv2.line(debug, (0, offset), (w, offset), (255, 0, 0), 3)
        cv2.line(debug, (0, h - offset), (w, h - offset), (255, 0, 0), 3)

        cv2.imwrite(
            str(DEBUG_DIR / f"{page.stem}_measurement.png"),
            debug,
        )

        left_profile = [
            int(gray[:, x].mean())
            for x in range(min(100, w))
        ]

        right_profile = [
            int(gray[:, w - 1 - x].mean())
            for x in range(min(100, w))
        ]

        result = {
            "left_profile": left_profile[:25],
            "right_profile": right_profile[:25],
        }

        job.report["border"][page.name] = result

        return result
