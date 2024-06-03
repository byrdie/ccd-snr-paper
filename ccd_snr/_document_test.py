import pathlib
import pylatex
import ccd_snr


def test_document():
    doc = ccd_snr.document()
    assert isinstance(doc, pylatex.Document)


def test_pdf():
    pdf = ccd_snr.pdf()
    assert isinstance(pdf, pathlib.Path)
    assert pdf.exists()
