# Scan Optimizer

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Docker](https://img.shields.io/badge/Docker-ready-2496ED.svg?logo=docker&logoColor=white)
![Platform](https://img.shields.io/badge/Synology-Docker-success)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)

Automatic PDF optimization pipeline for **Paperless-ngx** running on **Docker** and **Synology NAS**.

Scan Optimizer automatically improves scanned PDF documents before they are imported into Paperless-ngx. The pipeline enhances image quality, straightens pages, removes borders, crops documents, removes blank pages and rebuilds a compact PDF while preserving excellent readability.

---

# Why Scan Optimizer?

Most scanner software simply stores PDFs exactly as they were scanned.

Scan Optimizer automatically performs:

- Image enhancement
- Contrast optimization (CLAHE)
- Deskew correction
- Border detection
- Automatic cropping
- Blank page removal
- PDF optimization
- JPEG compression

The result is a clean and compact PDF ready for archiving in Paperless-ngx.

---

# Features

## Image Processing

- Automatic image cleanup
- CLAHE contrast enhancement
- Automatic deskew correction
- Automatic border detection
- Automatic document cropping

## PDF Optimization

- Rebuild PDF from processed images
- JPEG compression
- Configurable JPEG quality
- Significant file size reduction
- Preserve original page order

## Document Processing

- Automatic blank page detection
- Remove empty pages
- Processing reports
- Debug image generation

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
Archive Original
      │
      ▼
Render PDF (PyMuPDF)
      │
      ▼
Image Cleanup
      │
      ▼
CLAHE Enhancement
      │
      ▼
Deskew
      │
      ▼
Border Detection
      │
      ▼
Automatic Crop
      │
      ▼
Blank Page Detection
      │
      ▼
JPEG Compression
      │
      ▼
Rebuild Optimized PDF
      │
      ▼
Ready for Paperless-ngx
```

---

# Configuration

Configuration is stored in

```text
config/config.yaml
```

Example:

```yaml
convert:
  dpi: 200

cleanup:
  gaussian_blur: 3
  median_blur: 3

deskew:
  enabled: true
  min_angle: 2
  max_angle: 10

crop:
  enabled: true
  margin: 10

blank_page:
  enabled: true
  dry_run: false

enhance:
  enabled: true
  autocontrast: true
  clahe:
    enabled: true
    clip_limit: 2.0
    tile_grid_size: 8

pdf:
  jpeg_quality: 80
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/GrafZahl91/scan-optimizer.git
cd scan-optimizer
```

Start the optimizer

```bash
docker compose up -d --build
```

The optimizer automatically watches the configured scan directory and processes every incoming PDF.

---

# Project Structure

```text
config/
src/
tests/
debug/
optimized/
originals/
docker-compose.yml
README.md
CHANGELOG.md
```

---

# Performance

Current processing pipeline includes

- PyMuPDF rendering
- OpenCV image cleanup
- CLAHE enhancement
- Automatic deskew
- Contour-based border detection
- Automatic cropping
- Blank page removal
- JPEG PDF rebuild

Typical documents are significantly reduced in size while maintaining excellent readability.

---

# Debugging

Debug information is written to

```text
debug/
```

including

- Border detection images
- Processing reports
- Timing information

---

# Testing

Regression test documents are located in

```text
tests/
```

The repository includes sample documents for validating

- Border detection
- Cropping
- Blank page removal
- PDF generation

---

# Requirements

- Python 3.8+
- Docker
- Docker Compose
- OpenCV
- PyMuPDF

---

# Supported Platforms

- ✅ Synology NAS
- ✅ Docker
- ✅ Docker Compose
- ✅ Linux
- ✅ Paperless-ngx

---

# Roadmap

## Version 1.x

- Improved PDF compression
- Additional enhancement filters
- OCR preprocessing improvements
- More regression tests
- Performance optimizations

## Future

- Web interface
- Batch statistics
- Quality profiles
- OCR quality estimation

---

# Project Status

Current status

- ✅ Stable
- ✅ Production Ready
- ✅ Actively Maintained

---

# License

MIT License

---

# Author

Developed for Paperless-ngx document workflows running on Synology NAS using Docker.

Contributions, bug reports and feature requests are welcome.
