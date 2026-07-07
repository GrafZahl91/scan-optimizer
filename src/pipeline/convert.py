import time
import fitz

from logger import LOGGER


class ConvertStep:

    DPI = 200

    def run(self, job):

        LOGGER.info(f"Arbeitsordner: {job.workdir}")
        LOGGER.info(f"Konvertiere PDF mit PyMuPDF ({self.DPI} DPI)...")

        start = time.perf_counter()

        doc = fitz.open(job.pdf)

        job.pages = []

        for index, page in enumerate(doc):

            pix = page.get_pixmap(dpi=self.DPI)

            outfile = job.workdir / f"page-{index+1}.png"

            pix.save(outfile)

            job.pages.append(outfile)

        duration = time.perf_counter() - start

        LOGGER.info(
            f"{len(job.pages)} Seite(n) gefunden ({duration:.2f} s)"
        )

        return job
