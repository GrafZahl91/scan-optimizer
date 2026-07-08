import numpy as np


class ProfileBorderDetector:

    def _scan(self, values, threshold):
        for i, ratio in enumerate(values):
            if ratio < threshold:
                return i
        return 0

    def detect(self, gray):

        h, w = gray.shape

        dark_threshold = 40
        border_ratio = 0.90
        max_scan_x = min(100, w)
        max_scan_y = min(100, h)

        left_profile = []
        right_profile = []
        top_profile = []
        bottom_profile = []

        for x in range(max_scan_x):
            dark = np.count_nonzero(gray[:, x] < dark_threshold)
            left_profile.append(dark / h)

        for offset in range(max_scan_x):
            x = w - 1 - offset
            dark = np.count_nonzero(gray[:, x] < dark_threshold)
            right_profile.append(dark / h)

        for y in range(max_scan_y):
            dark = np.count_nonzero(gray[y, :] < dark_threshold)
            top_profile.append(dark / w)

        for offset in range(max_scan_y):
            y = h - 1 - offset
            dark = np.count_nonzero(gray[y, :] < dark_threshold)
            bottom_profile.append(dark / w)

        left = self._scan(left_profile, border_ratio)
        right = self._scan(right_profile, border_ratio)
        top = self._scan(top_profile, border_ratio)
        bottom = self._scan(bottom_profile, border_ratio)

        confidence = 1.0 - (
            left_profile[0]
            + right_profile[0]
            + top_profile[0]
            + bottom_profile[0]
        ) / 4

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
                "top": top_profile,
                "bottom": bottom_profile,
            },
            "detected": {
                "left": left,
                "right": right,
                "top": top,
                "bottom": bottom,
                "confidence": round(confidence, 3),
            },
        }
