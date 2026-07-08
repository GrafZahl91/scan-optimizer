import fitz


class DocumentDetector:
    def detect(self, pdf_path):
        doc = fitz.open(pdf_path)

        image_pages = 0
        vector_pages = 0

        for page in doc:
            images = page.get_images(full=True)
            drawings = page.get_drawings()

            if len(images) == 1 and len(drawings) == 0:
                image_pages += 1
            else:
                vector_pages += 1

        doc.close()

        if image_pages >= vector_pages:
            return "SCANNED"

        return "DIGITAL"
