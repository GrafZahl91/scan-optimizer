import shutil
from pathlib import Path

from logger import LOGGER


class PDFProcessor:

    def archive(self, pdf_path, archive_folder):

        pdf = Path(pdf_path)

        target = Path(archive_folder) / pdf.name

        shutil.copy2(pdf, target)

        LOGGER.info(f"Original archiviert: {target}")

        return target
