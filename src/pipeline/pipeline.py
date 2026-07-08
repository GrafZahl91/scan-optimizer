import shutil
import time

from config import config
from logger import LOGGER
from pipeline.archive import ArchiveStep
from pipeline.document_detector import DocumentDetector
from pipeline.factory import PipelineFactory
from pipeline.job import Job
from report import Report


class Pipeline:
    def __init__(self):
        self.detector = DocumentDetector()

    def process(self, pdf_path):
        job = Job(pdf_path).create()

        doc_type = self.detector.detect(pdf_path)
        job.doc_type = doc_type
        job.report["document_type"] = doc_type

        LOGGER.info(f"Dokumenttyp erkannt: {doc_type}")

        if job.doc_type == "DIGITAL":
            ArchiveStep().run(job)

            output = f"/optimized/{job.pdf.name}"
            shutil.copy2(job.archive, output)

            job.output = output

            LOGGER.info("Digitale PDF erkannt – Bildpipeline wird übersprungen.")
            LOGGER.info(f"Optimiertes PDF: {output}")

            Report().save(job)
            return job

        steps = PipelineFactory.build(
            job.doc_type,
            config.get("profile"),
        )

        for step in steps:
            start = time.perf_counter()

            job = step.run(job)

            elapsed = round(time.perf_counter() - start, 3)
            job.report["timings"][step.__class__.__name__] = elapsed

        Report().save(job)
        return job
