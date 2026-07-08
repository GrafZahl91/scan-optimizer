import time

import fitz

from config import config
from logger import LOGGER


class ConvertStep:
    def run(self, job):
        dpi = config.get("convert.dpi", 200)

        LOGGER.info(f"Arbeitsordner: {job.workdir}")
        LOGGER.info(f"Konvertiere PDF mit PyMuPDF ({dpi} DPI)...")

        start = time.perf_counter()

        doc = fitz.open(job.pdf)
        job.pages = []

        for index, page in enumerate(doc):
            pix = page.get_pixmap(dpi=dpi)
            outfile = job.workdir / f"page-{index + 1}.png"
            pix.save(outfile)
            job.pages.append(outfile)

        duration = time.perf_counter() - start

        LOGGER.info(
            f"{len(job.pages)} Seite(n) gefunden ({duration:.2f} s)"
        )

        return job
