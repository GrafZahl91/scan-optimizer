"""
Qualitätsprofile für Scan Optimizer.

Die Profile überschreiben gezielt Werte aus der config.yaml.
Nicht angegebene Werte bleiben unverändert.
"""

PROFILES = {
    "archive": {
        "convert.dpi": 200,
        "pdf.jpeg_quality": 80,
        "enhance.enabled": True,
        "deskew.enabled": True,
        "blank_page.enabled": True,
    },

    "ocr": {
        "convert.dpi": 300,
        "pdf.jpeg_quality": 90,
        "enhance.enabled": True,
        "deskew.enabled": True,
        "blank_page.enabled": True,
    },

    "quality": {
        "convert.dpi": 300,
        "pdf.jpeg_quality": 95,
        "enhance.enabled": True,
        "deskew.enabled": True,
        "blank_page.enabled": True,
    },

    "fast": {
        "convert.dpi": 150,
        "pdf.jpeg_quality": 70,
        "enhance.enabled": False,
        "deskew.enabled": False,
        "blank_page.enabled": True,
    },
}
