#!/usr/bin/env python3

from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR / "src"))

from pipeline.pipeline import Pipeline

PRIVATE_DIR = BASE_DIR / "tests-private"
PUBLIC_DIR = BASE_DIR / "tests" / "input"

TEST_DIR = PRIVATE_DIR if PRIVATE_DIR.exists() else PUBLIC_DIR


def main():
    pipeline = Pipeline()

    pdfs = sorted(TEST_DIR.glob("*.pdf"))

    print("=" * 60)
    print(" Scan Optimizer - Regression Tests")
    print("=" * 60)
    print()

    if not pdfs:
        print(f"Keine PDF-Dateien in {TEST_DIR}")
        return

    for number, pdf in enumerate(pdfs, start=1):
        print(f"[{number:02}] {pdf.name}")
        try:
            pipeline.process(str(pdf))
            print("     ✓ PASS")
        except Exception as exc:
            print(f"     ✗ FAIL: {exc}")

    print()
    print("=" * 60)
    print(f"Tests ausgeführt: {len(pdfs)}")
    print("=" * 60)


if __name__ == "__main__":
    main()
