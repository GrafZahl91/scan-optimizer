import os
import shutil
import time

from logger import LOGGER
from pipeline.pipeline import Pipeline
from utils import wait_until_complete, wait_until_pdf_valid

pipeline = Pipeline()


class Worker:

    def __init__(self, folder):
        self.folder = folder

        self.processed = {
            f for f in os.listdir(folder)
            if f.lower().endswith(".pdf")
        }

        LOGGER.info(
            f"{len(self.processed)} vorhandene PDF(s) übersprungen."
        )

    def start(self):

        LOGGER.info(f"Überwache {self.folder}")

        while True:

            try:

                for filename in sorted(os.listdir(self.folder)):

                    if not filename.lower().endswith(".pdf"):
                        continue

                    if filename in self.processed:
                        continue

                    path = os.path.join(self.folder, filename)

                    LOGGER.info(f"Neue PDF gefunden: {filename}")

                    if not wait_until_complete(path):
                        LOGGER.warning("Datei noch nicht vollständig.")
                        continue

                    if not wait_until_pdf_valid(path):
                        LOGGER.warning("PDF noch nicht gültig.")
                        continue

                    LOGGER.info("PDF ist bereit.")

                    try:

                        pipeline.process(path)

                        self.processed.add(filename)

                        LOGGER.info("Verarbeitung abgeschlossen.")

                    except Exception:

                        LOGGER.exception("Fehler bei Verarbeitung")

                        failed = f"/failed/{filename}"

                        try:
                            shutil.move(path, failed)
                            LOGGER.warning(
                                f"PDF nach {failed} verschoben."
                            )
                        except Exception:
                            LOGGER.exception(
                                "Konnte PDF nicht nach /failed verschieben."
                            )

                        self.processed.add(filename)

            except Exception:

                LOGGER.exception("Worker-Fehler")

            time.sleep(2)
