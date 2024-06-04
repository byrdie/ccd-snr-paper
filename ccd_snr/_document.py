import pathlib
import aastex
import ccd_snr

__all__ = [
    "document",
    "pdf",
]


def document() -> aastex.Document:
    """
    An :mod:`aastex` representation of the article.
    """

    doc = aastex.Document(
        documentclass="aastex631",
        document_options=[
            "twocolumn",
        ],
        lmodern=False,
        textcomp=False,
    )

    doc.packages.append(aastex.Package("amsmath"))

    doc.preamble += ccd_snr.acronyms()
    doc.variables += ccd_snr.variables()

    title = aastex.Title(
        "On the Signal-to-noise Ratio of Backilluminated CCDs in the "
        "Ultraviolet Regime",
    )
    doc.append(title)

    doc += ccd_snr.authors()

    doc.append(ccd_snr.sections.abstract())
    doc.append(ccd_snr.sections.introduction())
    doc.append(ccd_snr.sections.model())

    doc.append(aastex.Bibliography("sources"))

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
