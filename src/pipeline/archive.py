import shutil

from logger import LOGGER


class ArchiveStep:

    def run(self, job):

        destination = "/originals/" + job.pdf.name

        shutil.copy2(job.pdf, destination)

        job.archive = destination

        LOGGER.info(f"Original archiviert: {destination}")

        return job
