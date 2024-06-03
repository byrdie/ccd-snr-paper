import aastex

__all__ = [
    "authors",
]


def authors() -> list[aastex.Author]:

    msu = aastex.Affiliation(
        "Montana State University, "
        "Department of Physics, "
        "P.O. Box 173840, "
        "Bozeman, MT 59717, USA"
    )

    gsfc = aastex.Affiliation(
        "Goddard Space Flight Center, 8800 Greenbelt Rd, Greenbelt, MD 20771, USA"
    )

    return [
        aastex.Author("Roy T. Smart", affiliation=msu),
        aastex.Author("Charles C. Kankelborg", affiliation=msu),
        aastex.Author("Jacob D. Parker", affiliation=gsfc),
    ]
