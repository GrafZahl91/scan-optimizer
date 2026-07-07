import logging
import sys

LOGGER = logging.getLogger("scan_optimizer")


def setup(level="INFO"):
    LOGGER.setLevel(level)

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s"
    )

    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(formatter)

    if not LOGGER.handlers:
        LOGGER.addHandler(console)

    return LOGGER
