# Scan Optimizer

Automatic PDF optimization pipeline for Paperless-ngx and Synology NAS.

## Features

- Automatic image enhancement (CLAHE)
- Automatic deskew
- Automatic border detection
- Automatic document cropping
- Automatic blank page removal
- JPEG based PDF rebuild
- Configurable JPEG quality
- Debug reports
- Docker support
- Paperless-ngx integration

## Pipeline

PDF
 ↓
Render (PyMuPDF)
 ↓
Image Cleanup
 ↓
CLAHE Enhancement
 ↓
Deskew
 ↓
Border Detection
 ↓
Auto Crop
 ↓
Blank Page Detection
 ↓
JPEG Compression
 ↓
Optimized PDF

## Configuration

Configuration is stored in:

config/config.yaml

Example:

pdf:
  jpeg_quality: 80

## Requirements

- Docker
- Docker Compose
- Python 3.8+
- OpenCV
- PyMuPDF

## License

MIT License
