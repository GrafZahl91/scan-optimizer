import time

from logger import LOGGER


class PipelineStep:

    name = "PipelineStep"

    def log(self, message):
        LOGGER.info(f"[{self.name}] {message}")

    def debug(self, job, stage, filename, image):
        job.debug.save(stage, filename, image)

    def measure(self, label, func, *args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        self.log(f"{label}: {elapsed:.2f} s")
        return result
