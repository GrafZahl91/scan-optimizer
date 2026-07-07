import cv2

from logger import LOGGER


class CleanupStep:

    def run(self, job):

        LOGGER.info("Optimiere Bilder mit OpenCV...")

        kernel = cv2.getStructuringElement(
            cv2.MORPH_RECT,
            (3, 3)
        )

        for page in job.pages:

            image = cv2.imread(
                str(page),
                cv2.IMREAD_GRAYSCALE
            )

            # leicht glätten
            image = cv2.GaussianBlur(image, (3, 3), 0)

            # Salz/Pfeffer-Rauschen entfernen
            image = cv2.medianBlur(image, 3)

            # Kontrast normalisieren
            image = cv2.normalize(
                image,
                None,
                0,
                255,
                cv2.NORM_MINMAX
            )

            # Dokument binarisieren
            image = cv2.adaptiveThreshold(
                image,
                255,
                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                cv2.THRESH_BINARY,
                35,
                15
            )

            # Kleine schwarze Punkte entfernen
            image = cv2.morphologyEx(
                image,
                cv2.MORPH_OPEN,
                kernel
            )

            cv2.imwrite(str(page), image)

        LOGGER.info("OpenCV-Optimierung abgeschlossen.")

        return job
