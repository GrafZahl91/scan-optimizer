# Scan Optimizer

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Docker](https://img.shields.io/badge/Docker-ready-2496ED.svg?logo=docker&logoColor=white)
![Platform](https://img.shields.io/badge/Synology-Docker-success)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)

**Smart PDF optimization for Paperless-ngx with automatic document type detection.**

Scan Optimizer automatically detects whether an incoming PDF is a **scanned document** or a **digitally generated PDF**.

- **Scanned PDFs** are automatically enhanced using an OpenCV-based image processing pipeline.
- **Digital PDFs** bypass image processing completely, preserving vector graphics, colors and text quality without unnecessary recompression.

Designed for fully automated document workflows on **Paperless-ngx**, **Docker** and **Synology NAS**.

---

# Why Scan Optimizer?

Most scanner software simply stores PDFs exactly as they were scanned.

Scan Optimizer automatically performs:

- Automatic document type detection
- Image enhancement
- Contrast optimization (CLAHE)
- Deskew correction
- Hybrid border detection
- Automatic cropping
- Blank page removal
- OCR preprocessing
- PDF optimization
- JPEG compression (scanned documents only)

Digital PDFs are preserved without quality loss.

---

# Features

## Intelligent Document Processing

- Automatic document type detection
- Separate processing paths for scanned and digital PDFs
- Digital PDF passthrough
- Automatic processing reports
- Debug image generation

## Image Processing

- Automatic image cleanup
- CLAHE contrast enhancement
- OCR preprocessing
- Automatic deskew correction
- Hybrid border detection
- Automatic document cropping

## PDF Optimization

- Rebuild optimized PDFs from processed images
- JPEG compression
- Configurable JPEG quality
- Significant file size reduction
- Preserve original page order

## Document Processing

- Automatic blank page detection
- Coverage-based blank page analysis
- Remove empty pages

## Platform Support

- Docker
- Docker Compose
- Synology NAS
- Linux
- Paperless-ngx

---

# Processing Pipeline

```text
                     Incoming PDF
                          │
                          ▼
              Document Type Detection
                          │
             ┌────────────┴────────────┐
             │                         │
             ▼                         ▼
        DIGITAL PDF              SCANNED PDF
             │                         │
             │                  Archive Original
             │                         │
             │                  Render PDF
             │                         │
             │                  Image Cleanup
             │                         │
             │                  CLAHE Enhancement
             │                         │
             │                  OCR Preprocessing
             │                         │
             │                  Deskew Correction
             │                         │
             │                  Hybrid Border Detection
             │                         │
             │                  Automatic Cropping
             │                         │
             │                  Blank Page Detection
             │                         │
             │                  JPEG Compression
             │                         │
             └──────────────► Optimized PDF
```

---

# Configuration

Configuration is stored in:

```text
config/config.yaml
```

---

# Installation

```bash
git clone https://github.com/GrafZahl91/scan-optimizer.git
cd scan-optimizer
docker compose up -d --build
```

The optimizer automatically watches the configured scan directory and processes every incoming PDF.

---

# Project Structure

```text
config/
src/
tests/
docs/
debug/
optimized/
originals/
docker-compose.yml
README.md
CHANGELOG.md
CONTRIBUTING.md
```

---

# Performance

Current processing pipeline includes:

- Automatic document type detection
- PyMuPDF rendering
- OpenCV image cleanup
- CLAHE enhancement
- OCR preprocessing
- Automatic deskew
- Hybrid border detection
- Automatic cropping
- Coverage-based blank page detection
- JPEG PDF rebuild

Digital PDFs are preserved without unnecessary rendering while scanned documents are automatically optimized.

---

# Testing

Regression test documents are located in:

```text
tests/
```

The repository contains reference documents for validating:

- Document type detection
- Hybrid border detection
- Automatic cropping
- Blank page detection
- OCR preprocessing
- PDF generation

---

# Roadmap

## Version 1.x

- Lossless PDF optimization
- OCR text layer
- Additional regression tests
- Performance improvements

## Future

- Web interface
- Batch statistics
- Quality profiles
- Plugin architecture

---

# License

MIT License
