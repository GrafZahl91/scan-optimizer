import cv2
from logger import LOGGER
from pipeline.border_analyzer import BorderAnalyzer

class BorderRemovalStep:
    def __init__(self):
        self.analyzer = BorderAnalyzer()

    def run(self, job):
        LOGGER.info("BorderRemoval wird ausgeführt...")

        for page in job.pages:
            image = cv2.imread(str(page))

            if image is None:
                LOGGER.warning(
                    f"{page.name}: Bild konnte nicht geladen werden."
                )
                continue

            gray = cv2.cvtColor(
                image,
                cv2.COLOR_BGR2GRAY,
            )

            result = self.analyzer.analyze(
                job,
                page,
                image,
                gray,
            )

            crop = result["detected"]

            left = crop["left"]
            right = crop["right"]
            top = crop["top"]
            bottom = crop["bottom"]

            h, w = image.shape[:2]

            cropped = image[
                top:h - bottom,
                left:w - right,
            ]

            cv2.imwrite(str(page), cropped)

        return job
