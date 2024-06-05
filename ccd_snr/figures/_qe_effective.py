import matplotlib.pyplot as plt
import astropy.units as u
import named_arrays as na
import optika
import aastex

__all__ = [
    "qe_effective",
]


def qe_effective() -> aastex.Figure:
    """
    A figure reproducing Figure 12 of Stern (1994).
    """

    result = aastex.Figure("eqe", position="htb!")

    wavelength = na.geomspace(10, 10000, axis="wavelength", num=1001) * u.AA

    eqe = optika.sensors.quantum_efficiency_effective(
        wavelength=wavelength,
    )

    eqe_max = optika.sensors.quantum_efficiency_effective(
        wavelength=wavelength,
        cce_backsurface=1,
    )

    fig, ax = plt.subplots(
        figsize=(aastex.column_width_inches, 2.5),
        constrained_layout=True,
    )
    na.plt.plot(
        wavelength,
        eqe,
        ax=ax,
        label="effective QE",
    )
    na.plt.plot(
        wavelength,
        eqe_max,
        ax=ax,
        label="transmissivity",
    )
    ax.set_xscale("log")
    ax.set_xlabel(f"wavelength ({wavelength.unit:latex_inline})")
    ax.set_ylabel("efficiency")
    ax.legend()

    result.add_fig(fig, width=None)

    result.add_caption(
        aastex.NoEscape(
            r"""
A reproduction of Figure 12 of \citet{Stern1994} showing the theoretical, effective
\QE\ vs. wavelength of a Tektronix $512 \times 512$ pixel \CCD\ calculated using
\href{https://optika.readthedocs.io/en/latest/_autosummary/optika.sensors.quantum_efficiency_effective.html}
{\texttt{optika.sensors.quantum\_efficiency\_effective()}}
"""
        )
    )

    return result
