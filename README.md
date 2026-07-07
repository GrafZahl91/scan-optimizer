# 📄 Scan Optimizer

Automatic scan optimization pipeline for **ScanSnap**, **Synology NAS** and **Paperless-ngx**.

Scan Optimizer watches a folder for new PDF scans, archives the original document, optimizes the pages and generates a cleaned PDF ready for Paperless-ngx.

---

## Current Version

**v0.3.2-beta**

**Status:** 🟢 Functional Alpha

---

## Current Features

- Automatic folder monitoring
- Original PDF archiving
- PDF rendering using PyMuPDF
- Image optimization using OpenCV
- Automatic blank page detection
- Automatic blank page removal
- Configurable via YAML
- Docker support
- Synology NAS compatible
- Paperless-ngx integration

---

## Processing Pipeline

```text
Incoming PDF
      │
      ▼
Archive Original
      │
      ▼
Render PDF
      │
      ▼
Image Optimization
      │
      ▼
Blank Page Detection
      │
      ▼
Rebuild PDF
      │
      ▼
Optimized PDF
