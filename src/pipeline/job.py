from pathlib import Path
import shutil
from debug import Debug


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

        # Gemeinsamer Debug-Helper
        self.debug = Debug(self)

        # Sammelstelle für Statistiken
        self.report = {
            "document": self.name,
            "pages": {},
            "deskew": {},
            "border": {},
            "timings": {}
        }

    def create(self):

        if self.workdir.exists():
            shutil.rmtree(self.workdir)

        self.workdir.mkdir(parents=True)

        return self
