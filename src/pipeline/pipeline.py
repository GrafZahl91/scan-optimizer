import time
from pipeline.archive import ArchiveStep
from pipeline.convert import ConvertStep
from pipeline.cleanup import CleanupStep
from pipeline.enhance import EnhanceStep
from pipeline.deskew import DeskewStep
from pipeline.blank_pages import BlankPageStep
from pipeline.rebuild import RebuildStep
from pipeline.job import Job
from report import Report


class Pipeline:

    def __init__(self):

        self.steps = [
            ArchiveStep(),
            ConvertStep(),
            CleanupStep(),
            EnhanceStep(),
            DeskewStep(),
            BlankPageStep(),
            RebuildStep(),
        ]

    def process(self, pdf_path):

        job = Job(pdf_path).create()

        for step in self.steps:
            start = time.perf_counter()

            job = step.run(job)

            elapsed = round(time.perf_counter() - start, 3)

            job.report["timings"][step.__class__.__name__] = elapsed

        Report().save(job)

        return job
