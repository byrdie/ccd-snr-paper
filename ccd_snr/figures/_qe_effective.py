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

    ccd = optika.sensors.E2VCCDAIAMaterial()

    eqe_measured = ccd.quantum_efficiency_measured

    wavelength = na.geomspace(10, 10000, axis="wavelength", num=1001) * u.AA

    eqe = ccd.quantum_efficiency_effective(
        rays=optika.rays.RayVectorArray(
            wavelength=wavelength,
            direction=na.Cartesian3dVectorArray(0, 0, 1),
        ),
        normal=na.Cartesian3dVectorArray(0, 0, -1),
    )

    fig, ax = plt.subplots(
        figsize=(aastex.column_width_inches, 2.5),
        constrained_layout=True,
    )
    na.plt.plot(
        wavelength,
        eqe,
        ax=ax,
        label=r"empirical fit",
    )
    na.plt.scatter(
        eqe_measured.inputs,
        eqe_measured.outputs,
        ax=ax,
        label="measurement",
        s=10,
    )
    ax.set_xscale("log")
    ax.set_xlabel(f"wavelength ({wavelength.unit:latex_inline})")
    ax.set_ylabel("effective quantum efficiency")
    ax.legend()

    result.append(aastex.NoEscape(r"\vspace{5pt}"))
    result.add_fig(fig, width=None)

    result.add_caption(
        aastex.NoEscape(
            r"""
A reproduction of Figure 6 of \citet{Boerner2012} that plots the measured,
effective \QE\ of the \AIA\ \CCDs\ against the \citet{Stern1994} model with
$\eta_0 = \backsurfaceCCE$, 
$\delta = \oxideThickness$,
$W = \implantThickness$,
and $D = \substrateThickness$.
"""
        )
    )

    return result
