import aastex

__all__ = [
    "authors",
]


def authors() -> list[aastex.Author]:
    """
    A list of the authors of this article and their affiliations.
    """

    msu = aastex.Affiliation(
        "Montana State University, "
        "Department of Physics, "
        "P.O. Box 173840, "
        "Bozeman, MT 59717, USA"
    )

    gsfc = aastex.Affiliation(
        "Goddard Space Flight Center, 8800 Greenbelt Rd, Greenbelt, MD 20771, USA"
    )

    roy = aastex.Author(
        name="Roy T. Smart",
        affiliation=msu,
        orcid="0000-0002-9997-5515",
        email="roytsmart@gmail.com",
    )

    charles = aastex.Author(
        name="Charles C. Kankelborg",
        affiliation=msu,
        orcid="0000-0002-1992-7469",
    )

    jake = aastex.Author(
        name="Jacob D. Parker",
        orcid="0000-0001-8732-8284",
        affiliation=gsfc,
    )

    return [
        roy,
        charles,
        jake,
    ]
