import time
import fitz

PDF = "/scans/Dokument_2026-07-07_12-22-38.pdf"

start = time.perf_counter()

doc = fitz.open(PDF)

print(f"PDF geöffnet ({len(doc)} Seiten)")

for i, page in enumerate(doc):

    page_start = time.perf_counter()

    pix = page.get_pixmap(dpi=200)

    outfile = f"/tmp/page-{i+1}.png"

    pix.save(outfile)

    print(
        f"Seite {i+1}: "
        f"{time.perf_counter()-page_start:.2f} s"
    )

print(
    f"Gesamt: {time.perf_counter()-start:.2f} s"
)
