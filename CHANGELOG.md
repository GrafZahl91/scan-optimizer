# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog and follows Semantic Versioning.

---

## v1.2.0

### Added

- Automatic document type detection
- Intelligent routing for scanned and digital PDFs
- Digital PDF passthrough without image recompression
- OCR preprocessing step
- Coverage-based blank page detection
- Processing reports include detected document type
- Additional regression test documents

### Changed

- Blank page detection now uses relative page coverage instead of a fixed pixel threshold
- Improved processing pipeline architecture
- Improved logging and debugging output
- Updated project documentation
- Extended regression test suite

### Fixed

- Prevent quality loss for digitally generated PDFs
- Reduced false positive blank page detection
- Improved handling of mixed document types

---

## v1.1.0

### Added

- Hybrid border detection
- OCR preprocessing
- Improved border analysis
- Debug visualization for border detection

### Changed

- Border detection combines contour and profile analysis
- Improved border removal accuracy

---

## v1.0.0

### Added

- Automatic border detection
- Automatic document cropping
- CLAHE image enhancement
- Deskew correction
- Blank page detection
- JPEG based PDF rebuild
- Configurable JPEG quality
- Debug reports
- Regression tests

### Changed

- Complete rebuild from processed images
- Massive PDF size reduction
- Contour based border detection

### Removed

- Legacy profile based border detection
