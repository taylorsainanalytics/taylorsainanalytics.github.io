"""Portfolio-safe example adapted from a production PDF extraction workflow.
Organization-specific paths, product names, identifiers, and content have been removed.
"""

import re
import fitz  # PyMuPDF
from openpyxl import Workbook

CONTENT_REGION = (60, 75, 250, 350)
HEADER_REGION = (250, 45, 575, 125)


def text_blocks(page, region):
    """Return visible text blocks in reading order from a target page region."""
    blocks = page.get_text("blocks", clip=region)
    visible = [(block[4], block[:4]) for block in blocks if "<image:" not in block[4]]
    return sorted(visible, key=lambda block: block[1][1])


def parse_metadata(filename):
    """Derive reporting dimensions from a standardized source filename."""
    match = re.search(r"(\d{2})(\d{2})(\d{2})", filename)
    if not match:
        return None
    return {
        "module": match.group(1),
        "week": match.group(2),
        "lesson": match.group(3),
    }


def extract_objectives(page):
    """Capture objective content and stop when the next document section begins."""
    objectives = []
    for text, _coords in text_blocks(page, CONTENT_REGION):
        cleaned = text.strip()
        if cleaned.upper().startswith("MATERIALS"):
            break
        if cleaned:
            objectives.append(cleaned)
    return "\n".join(objectives)


def build_row(pdf_path):
    doc = fitz.open(pdf_path)
    page = doc.load_page(0)
    metadata = parse_metadata(pdf_path)

    header_blocks = page.get_text("blocks", clip=HEADER_REGION)
    header = " ".join(block[4].strip() for block in header_blocks if block[4].strip())

    row = {
        **metadata,
        "header": header,
        "objectives": extract_objectives(page),
    }
    doc.close()
    return row


# Structured output can then be written to Excel for downstream processing.
wb = Workbook()
ws = wb.active
ws.append(["Module", "Week", "Lesson", "Header", "Objectives"])
