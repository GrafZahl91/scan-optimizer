from config import config
from logger import setup
from worker import Worker

log = setup(config.get("log_level"))

log.info("Scan Optimizer gestartet")

worker = Worker(config.get("watch_folder"))

worker.start()
