#!/usr/bin/env python3

import json
from pathlib import Path

DEBUG_DIR = Path("/volume1/docker/scan-optimizer/debug")

reports = sorted(DEBUG_DIR.glob("*/report.json"))

if not reports:
    print("❌ Keine Reports gefunden.")
    raise SystemExit(1)

latest = reports[-1]

print(f"Prüfe {latest.parent.name}")

report = json.loads(latest.read_text())

errors = []

# ---------- Seiten ----------
pages = report.get("pages", {})

if pages.get("total", 0) < 1:
    errors.append("Keine Seiten erkannt.")

if pages.get("kept", 0) < 1:
    errors.append("Keine KEEP-Seite vorhanden.")

# ---------- Deskew ----------
deskew = report.get("deskew", {})

if not deskew:
    errors.append("Deskew-Daten fehlen.")

# ---------- Border ----------
border = report.get("border", {})

if not border:
    errors.append("Border-Daten fehlen.")

# ---------- Timings ----------
timings = report.get("timings", {})

required_steps = [
    "ArchiveStep",
    "ConvertStep",
    "CleanupStep",
    "EnhanceStep",
    "DeskewStep",
    "BorderRemovalStep",
    "BlankPageStep",
    "RebuildStep",
]

for step in required_steps:
    if step not in timings:
        errors.append(f"{step} fehlt.")

if errors:
    print("\n❌ Regression fehlgeschlagen:\n")
    for e in errors:
        print(" -", e)
    raise SystemExit(1)

print("\n✅ Regression erfolgreich")

print("\nPipeline-Zeiten:")

for step, value in timings.items():
    print(f"{step:20} {value:6.3f} s")
