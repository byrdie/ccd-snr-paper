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
        email="roytsmart@gmail.com"
    )

    charles = aastex.Author(
        name="Charles C. Kankelborg",
        affiliation=msu,
    )

    jake = aastex.Author(
        name="Jacob D. Parker",
        affiliation=gsfc,
    )

    return [
        roy,
        charles,
        jake,
    ]
