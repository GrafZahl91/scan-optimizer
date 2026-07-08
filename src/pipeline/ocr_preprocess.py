import cv2

from config import config
from pipeline.base import PipelineStep


class OCRPreprocessStep(PipelineStep):
    name = "OCR"
    def run(self, job):
        if not config.get("ocr.enabled", True):
            return job

        self.log("Starte Verarbeitung...")

        for page in job.pages:
            image = cv2.imread(str(page))

            if image is None:
                continue

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            if config.get("ocr.denoise", True):
                gray = cv2.fastNlMeansDenoising(
                    gray,
                    None,
                    10,
                    7,
                    21,
                )

            if config.get("ocr.adaptive_threshold", False):
                gray = cv2.adaptiveThreshold(
                    gray,
                    255,
                    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                    cv2.THRESH_BINARY,
                    31,
                    12,
                )

            if config.get("ocr.sharpen", True):
                blur = cv2.GaussianBlur(gray, (0, 0), 3)
                gray = cv2.addWeighted(
                    gray,
                    1.5,
                    blur,
                    -0.5,
                    0,
                )

            cv2.imwrite(str(page), gray)


        return job
