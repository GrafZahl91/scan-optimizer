from pipeline.archive import ArchiveStep
from pipeline.convert import ConvertStep
from pipeline.cleanup import CleanupStep
from pipeline.deskew import DeskewStep
from pipeline.crop import CropStep
from pipeline.blank_pages import BlankPageStep
from pipeline.rebuild import RebuildStep
from pipeline.job import Job


class Pipeline:

    def __init__(self):

        self.steps = [
            ArchiveStep(),
            ConvertStep(),
            CleanupStep(),
            DeskewStep(),
            CropStep(),
            BlankPageStep(),
            RebuildStep(),
        ]

    def process(self, pdf_path):

        job = Job(pdf_path).create()

        for step in self.steps:
            job = step.run(job)

        return job
