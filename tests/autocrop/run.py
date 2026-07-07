from pathlib import Path
import shutil
import time

INPUT = Path("tests/autocrop/input")
SCAN = Path("/volume1/docker/paperless/scans")

files = sorted(INPUT.glob("*.pdf"))

print(f"{len(files)} Testdatei(en) gefunden.\n")

for file in files:

    target = SCAN / file.name

    print(f"→ {file.name}")

    shutil.copy2(file, target)

    time.sleep(20)

print("\nAlle Testdateien wurden übergeben.")
