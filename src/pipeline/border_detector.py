from pipeline.border_detector_profile import ProfileBorderDetector
from pipeline.border_detector_contour import ContourBorderDetector


class BorderDetector:

    def __init__(self):
        self.profile = ProfileBorderDetector()
        self.contour = ContourBorderDetector()

    def _plausible(self, result, width, height):

        d = result["detected"]

        left = d.get("left", 0)
        right = d.get("right", 0)
        top = d.get("top", 0)
        bottom = d.get("bottom", 0)

        crop_w = width - left - right
        crop_h = height - top - bottom

        if crop_w < width * 0.70:
            return False

        if crop_h < height * 0.70:
            return False

        if left > width * 0.20:
            return False

        if right > width * 0.20:
            return False

        if top > height * 0.20:
            return False

        if bottom > height * 0.20:
            return False

        return True

    def detect(self, gray):

        h, w = gray.shape

        profile = self.profile.detect(gray)

        if self._plausible(profile, w, h):
            return profile

        contour = self.contour.detect(gray)

        if self._plausible(contour, w, h):
            return contour

        return {
            "detected": {
                "left": 0,
                "right": 0,
                "top": 0,
                "bottom": 0,
                "confidence": 0,
            },
            "profiles": {},
        }
