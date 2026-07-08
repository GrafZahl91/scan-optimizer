from logger import LOGGER


class PipelineStep:

    name = "PipelineStep"

    def log(self, message):
        LOGGER.info(f"[{self.name}] {message}")

    def debug(self, job, stage, filename, image):
        job.debug.save(stage, filename, image)
