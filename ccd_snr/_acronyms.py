import aastex

__all__ = [
    "acronyms",
]


def acronyms() -> list[aastex.Acronym]:
    """
    A list of acronyms that are used in the body of the article.
    """
    return [
        aastex.Acronym("CCD", "charge-coupled device", plural=True),
        aastex.Acronym("CMOS", "complementary metal–oxide–semiconductor"),
        aastex.Acronym("FUV", "far ultraviolet"),
        aastex.Acronym("EUV", "extreme ultraviolet"),
        aastex.Acronym("CCE", "charge-collection efficiency"),
        aastex.Acronym("QE", "quantum efficiency"),
        aastex.Acronym("QY", "quantum yield"),
        aastex.Acronym("SNR", "signal-to-noise ratio"),
        aastex.Acronym("AIA", "the Atmospheric Imaging Assembly"),
        aastex.Acronym("IRIS", "the Interface Region Imaging Spectrograph"),
    ]
