from pathlib import Path
import shutil


class Job:

    def __init__(self, pdf_path):

        self.pdf = Path(pdf_path)
        self.name = self.pdf.stem

        self.workdir = Path("/tmp/jobs") / self.name

        self.pages = []

        # Informationen über jede Seite
        self.page_info = []

        self.archive = None
        self.output = None

    def create(self):

        if self.workdir.exists():
            shutil.rmtree(self.workdir)

        self.workdir.mkdir(parents=True)

        return self
