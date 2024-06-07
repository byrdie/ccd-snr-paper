import aastex


def introduction() -> aastex.Section:
    result = aastex.Section("Introduction")
    result.append(
        r"""
Backilluminated, silicon-based image sensors such as \CCDs\ and \CMOS\ sensors 
are ubiquitous in ultraviolet solar astronomy, 
and are currently used in many of NASA's most ambitious solar missions,
such as \AIA\ \citep{Lemen2012} and \IRIS\ \citep{DePontieu2014}.
Despite their popularity, measuring the \QE\ of \CCDs\ with high spectral resolution
across the \FUV\ and \EUV\ remains difficult due to the expense of calibrated, 
tunable sources in these wavelength ranges.
Therefore, theoretical models of the \QE\ fitted to sparse measurements,
such as those developed in \citet{Stern1994}, offer the best estimate of the \QE\
in the \FUV\ and \EUV.

In this work, we explore the consequences of the \citet{Stern1994} model by
developing an analytic expression for the \SNR\ implied by their model, and
validate it using a Monte Carlo simulation.
"""
    )
    return result
