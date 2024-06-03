import pathlib
import pylatex

__all__ = [
    "document",
    "pdf",
]


def document() -> pylatex.Document:
    """
    A :mod:`pylatex` representation of the article.
    """

    doc = pylatex.Document(
        documentclass="spieman",
        document_options="12pt",
    )

    title = pylatex.Command(
        command="title",
        arguments=[
            "My temporary title",
        ],
    )

    author_1 = pylatex.Command(
        command="author",
        arguments=[
            "Roy T. Smart",
        ],
    )

    doc.preamble.append(title)
    doc.preamble.append(author_1)

    doc.append(pylatex.Command("maketitle"))

    doc.append("test")

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
