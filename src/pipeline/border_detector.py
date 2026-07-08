import cv2
import numpy as np


class BorderDetector:
    def detect(self, gray):
        h, w = gray.shape

        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blurred, 40, 120)

        kernel = np.ones((5, 5), np.uint8)
        edges = cv2.dilate(edges, kernel, iterations=2)
        edges = cv2.erode(edges, kernel, iterations=1)

        contours, _ = cv2.findContours(
            edges,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE,
        )

        if not contours:
            return {
                "left": {"dark_ratio": 0},
                "right": {"dark_ratio": 0},
                "profiles": {},
                "detected": {
                    "left": 0,
                    "right": 0,
                    "top": 0,
                    "bottom": 0,
                    "confidence": 0,
                },
            }

        contour = max(contours, key=cv2.contourArea)

        x, y, cw, ch = cv2.boundingRect(contour)

        return {
            "left": {"dark_ratio": 0},
            "right": {"dark_ratio": 0},
            "profiles": {},
            "detected": {
                "left": x,
                "right": w - (x + cw),
                "top": y,
                "bottom": h - (y + ch),
                "confidence": 1.0,
            },
        }
