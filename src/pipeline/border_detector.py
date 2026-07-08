import numpy as np


class BorderDetector:

    def detect(self, gray):

        h, w = gray.shape

        dark_threshold = 40
        border_ratio = 0.90
        max_scan = min(100, w)

        left_profile = []
        right_profile = []

        # Alle linken Spalten messen
        for x in range(max_scan):
            dark = np.count_nonzero(gray[:, x] < dark_threshold)
            left_profile.append(round(dark / h, 3))

        # Alle rechten Spalten messen
        for offset in range(max_scan):
            x = w - 1 - offset
            dark = np.count_nonzero(gray[:, x] < dark_threshold)
            right_profile.append(round(dark / h, 3))

        # Randposition bestimmen
        left = 0
        for i, ratio in enumerate(left_profile):
            if ratio < border_ratio:
                left = i
                break

        right = 0
        for i, ratio in enumerate(right_profile):
            if ratio < border_ratio:
                right = i
                break

        return {
            "left": {
                "dark_ratio": left_profile[0],
            },
            "right": {
                "dark_ratio": right_profile[0],
            },
            "profiles": {
                "left": left_profile,
                "right": right_profile,
            },
            "detected": {
                "left": left,
                "right": right,
                "confidence": round(
                    1.0 - (left_profile[0] + right_profile[0]) / 2,
                    3,
                ),
            },
        }
