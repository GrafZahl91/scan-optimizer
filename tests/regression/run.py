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

pages = report.get("pages", {})

if pages.get("total") != 2:
    errors.append("Falsche Seitenanzahl")

if pages.get("kept") != 1:
    errors.append("KEEP-Seiten stimmen nicht")

if pages.get("removed") != 1:
    errors.append("Entfernte Seiten stimmen nicht")

if "deskew" not in report:
    errors.append("Deskew fehlt")

if "timings" not in report:
    errors.append("Timings fehlen")

if errors:
    print("\n❌ Regression fehlgeschlagen:\n")
    for e in errors:
        print(" -", e)
    raise SystemExit(1)

print("\n✅ Regression erfolgreich")
