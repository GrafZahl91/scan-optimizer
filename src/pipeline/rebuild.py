import fitz

from logger import LOGGER
from config import config


class RebuildStep:

    def run(self, job):

        if config.get("debug.force_error", False):
            raise RuntimeError("Testfehler: Rebuild absichtlich abgebrochen.")

        LOGGER.info("Erzeuge optimiertes PDF...")

        src = fitz.open(job.archive)
        dst = fitz.open()

        kept = 0

        for index, info in enumerate(job.page_info):

            if info["status"] != "KEEP":
                LOGGER.info(f"Seite {index + 1} entfernt.")
                continue

            dst.insert_pdf(
                src,
                from_page=index,
                to_page=index
            )

            kept += 1

        output = f"/optimized/{job.name}.pdf"

        if kept > 0:
            dst.save(output)
            LOGGER.info(f"{kept} Seite(n) gespeichert.")
            LOGGER.info(f"Optimiertes PDF: {output}")
        else:
            LOGGER.warning("Keine Seiten übrig.")

        src.close()
        dst.close()

        job.output = output

        return job
