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
        lmodern=False,
        textcomp=False,
    )

    title = pylatex.Command(
        command="title",
        arguments=[
            "On the Signal-to-noise Ratio of Charged-coupled Devices in the "
            "Extreme Ultraviolet Regime",
        ],
    )

    roy = pylatex.Command(
        command="author",
        arguments="Roy T. Smart",
        options="a",
    )

    charles = pylatex.Command(
        command="author",
        arguments="Charles C. Kankelborg",
        options="a",
    )

    jake = pylatex.Command(
        command="author",
        arguments="Jacob D. Parker",
        options="b",
    )

    msu = pylatex.Command(
        command="affil",
        arguments="Montana State University, "
        "Department of Physics, "
        "P.O. Box 173840, "
        "Bozeman, MT 59717",
        options="a",
    )

    gsfc = pylatex.Command(
        command="affil",
        arguments="Goddard Space Flight Center, "
        "8800 Greenbelt Rd, "
        "Greenbelt, MD 20771",
        options="b",
    )

    doc.preamble.append(title)

    doc.preamble.append(roy)
    doc.preamble.append(charles)
    doc.preamble.append(jake)

    doc.preamble.append(msu)
    doc.preamble.append(gsfc)

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
