import os
import time
import pikepdf


def wait_until_complete(path, timeout=30):

    last_size = -1
    stable = 0

    start = time.time()

    while time.time() - start < timeout:

        try:
            size = os.path.getsize(path)
        except FileNotFoundError:
            return False

        if size == last_size:
            stable += 1
        else:
            stable = 0

        if stable >= 2:
            return True

        last_size = size
        time.sleep(1)

    return False


def wait_until_pdf_valid(path, retries=10):

    for _ in range(retries):

        try:
            with pikepdf.open(path):
                return True
        except Exception:
            time.sleep(1)

    return False
