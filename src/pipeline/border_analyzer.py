import cv2
from pathlib import Path

from pipeline.border_detector import BorderDetector

DEBUG_DIR = Path("/debug/border")
DEBUG_DIR.mkdir(parents=True, exist_ok=True)


class BorderAnalyzer:

    def __init__(self):
        self.detector = BorderDetector()

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

        result = self.detector.detect(gray)

        job.report["border"][page.name] = result

        return result
