import io
import cv2
import fitz

from logger import LOGGER
from config import config


class RebuildStep:
    def run(self, job):
        if config.get("debug.force_error", False):
            raise RuntimeError("Testfehler")

        LOGGER.info("Erzeuge optimiertes PDF...")

        pdf = fitz.open()
        kept = 0

        for index, info in enumerate(job.page_info):
            if info["status"] != "KEEP":
                LOGGER.info(f"Seite {index + 1} entfernt.")
                continue

            page_path = job.pages[index]

            image = cv2.imread(str(page_path))
            if image is None:
                LOGGER.warning(f"{page_path} konnte nicht geladen werden.")
                continue

            ok, jpg = cv2.imencode(
                ".jpg",
                image,
                [cv2.IMWRITE_JPEG_QUALITY, 92],
            )

            if not ok:
                LOGGER.warning(f"{page_path}: JPEG fehlgeschlagen.")
                continue

            img = fitz.open(
                "jpeg",
                io.BytesIO(jpg.tobytes()),
            )

            rect = img[0].rect

            page = pdf.new_page(
                width=rect.width,
                height=rect.height,
            )

            page.insert_image(
                rect,
                stream=jpg.tobytes(),
            )

            kept += 1

        output = f"/optimized/{job.name}.pdf"

        if kept:
            pdf.save(
                output,
                garbage=4,
                deflate=True,
            )
            LOGGER.info(f"{kept} Seite(n) gespeichert.")
            LOGGER.info(f"Optimiertes PDF: {output}")
        else:
            LOGGER.warning("Keine Seiten übrig.")

        pdf.close()
        job.output = output
        return job
