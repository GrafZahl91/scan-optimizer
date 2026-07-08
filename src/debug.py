from pathlib import Path
import cv2


class Debug:

    def __init__(self, job):
        self.base = Path("/debug") / job.name

    def save(self, step, filename, image):

        folder = self.base / step
        folder.mkdir(parents=True, exist_ok=True)

        cv2.imwrite(
            str(folder / filename),
            image,
        )
