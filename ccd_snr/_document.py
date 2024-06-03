import pathlib
import pylatex
import aastex
import ccd_snr

__all__ = [
    "document",
    "pdf",
]


def document() -> pylatex.Document:
    """
    A :class:`pylatex.Document` representation of the article.
    """

    doc = aastex.Document(
        documentclass="aastex631",
        document_options=[
            "twocolumn",
        ],
        lmodern=False,
        textcomp=False,
    )

    title = aastex.Title(
        "On the Signal-to-noise Ratio of Charged-coupled Devices in the "
        "Extreme Ultraviolet Regime",
    )

    doc.append(title)

    doc += ccd_snr.authors()

    introduction = aastex.Section("Introduction")
    introduction.append("testing")

    doc.append(introduction)

    return doc


def pdf() -> pathlib.Path:
    """
    Build a pdf version of :func:`document` and return the path of the document.
    """

    doc = document()

    path = pathlib.Path(__file__).parent / "ccd-euv-snr"
    doc.generate_pdf(
        filepath=path,
        clean_tex=False,
    )

    return path.with_suffix(".pdf")
