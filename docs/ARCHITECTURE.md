# Scan Optimizer Architecture

## Overview

Scan Optimizer automatically determines whether an incoming document is a scanned PDF or a digitally generated PDF.

Digital PDFs are preserved without unnecessary rendering.

Scanned PDFs are processed through the image optimization pipeline.

## Processing Flow

Incoming PDF
        │
        ▼
Document Type Detection
        │
 ┌──────┴─────────┐
 │                │
 ▼                ▼
DIGITAL       SCANNED
 │                │
 │          Archive Original
 │                │
 │          Render PDF
 │                │
 │          Image Cleanup
 │                │
 │          CLAHE Enhancement
 │                │
 │          OCR Preprocessing
 │                │
 │          Deskew Correction
 │                │
 │          Hybrid Border Detection
 │                │
 │          Automatic Cropping
 │                │
 │          Blank Page Detection
 │                │
 │          JPEG PDF Rebuild
 │
 └──────────────► Optimized PDF

## Design Principles

- Preserve digital PDFs whenever possible.
- Optimize scanned documents automatically.
- Keep every pipeline step independent.
- Prefer configuration over hard-coded values.
- Every processing step should produce meaningful log output.

## Regression Tests

Regression test documents are stored inside:

tests/

Every new feature should be validated against the existing regression documents before release.
