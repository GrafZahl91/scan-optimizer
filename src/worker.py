from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os

from logger import LOGGER


class ScanHandler(FileSystemEventHandler):

    def on_created(self, event):

        if event.is_directory:
            return

        if event.src_path.lower().endswith(".pdf"):
            LOGGER.info(f"Neue PDF erkannt: {os.path.basename(event.src_path)}")


class Worker:

    def __init__(self, folder):
        self.folder = folder

    def start(self):

        observer = Observer()

        observer.schedule(
            ScanHandler(),
            self.folder,
            recursive=False
        )

        observer.start()

        LOGGER.info(f"Überwache {self.folder}")

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()

        observer.join()
