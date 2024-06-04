import aastex

__all__ = [
    "model",
]


def model() -> aastex.Section:
    result = aastex.Section("Model")
    result.append(
        r"""
In this work, we will model the light-sensitive region of the backilluminated 
\CCD\ sensor as a epitaxial silicon layer with a given thickness which is coated
with a thin oxide layer to provide a realistic transmission coefficent.
The illuminated side of the epitaxial layer is considered to be implanted with ions
up to a given depth to create the electric field within the sensor.
        
The \QE\ of a \CCD\ is given by \citet{Janesick2001} as
\begin{equation}
    \text{QE}(\lambda) = \frac{N_\text{measured}}{N_\text{incident}},
\end{equation}
where $N_\text{measured}$ is the number of photons measured by the sensor
(a photon which results in at least one collected electron), 
and $N_\text{incident}$ is the total number of photons incident on the sensor.
From inspecting Equation 3.2 of \citet{Janesick2001}, we can see that the 
The number of measured photons is given by
\begin{equation} \label{photons-measured}
    N_\text{measured} = N_\text{incident} T(\lambda) \text{CCE}(\lambda) [1 - P_r(\lambda)],
\end{equation}
where $T(\lambda)$ is the transmissivity of the Si/SiO$_2$ interface for a given
wavelength, $\lambda$, $\text{CCE}(\lambda)$ is the charge-collection efficiency
as a function of wavelength, and $P_r(\lambda)$ is the probability that all of
the photoelectrons associated with a given photon will recombine.

$T(\lambda)$ can be determined using any number of multilayer codes.
For this work, we used our software, \texttt{optika} \citep{optika}, which uses
the transfer matrix method described in \citet{Yeh1988} with the optical constants
from \citet{Windt1998}.

In \citet{Stern1994}, the \CCE\ is expressed in terms of a differential \CCE,
$\eta(z)$ (which is the fraction of electrons collected for a photon
absorbed at a depth $z$), as
\begin{equation} \label{cce}
    \text{CCE}(\lambda) = \frac{\int_0^\infty \eta(z) \exp(-\alpha z) \, dz}
                               {\int_0^\infty \exp(-\alpha z) \, dz},
\end{equation}
where $\alpha$ is the absorption coefficient of silicon for the given wavelength.

In principle, $\eta(z)$ is a function of the exact implant profile which is
usually impractical to measure.
In \citet{Stern1994}, the authors adopt a piecewise-linear approximation of
the differential \CCE,
\begin{equation} \label{differential-cce}
    \eta(z) = \begin{cases}
        \eta_0 + (1 - \eta_0) z / W, & 0 < z < W \\
        1, & W < z < D \\
        0, & D < z < \infty
    \end{cases}
\end{equation}
where $\eta_0$ is the differential \CCE\ at the back surface of the sensor,
$W$ is the thickness of the implant region,
and $D$ is the thickness of the epitaxial layer.
Plugging Equation \ref{differential-cce} into Equation \ref{cce} yields an
arithmetic expression for the \CCE,
\begin{equation}
    \text{CCE}(\lambda) = \eta_0 + \left( \frac{1 - \eta_0}{\alpha W} \right)(1 - e^{-\alpha W}) - e^{-\alpha D},
\end{equation}
which can be used in Equation \ref{photons-measured} to determine the \QE.

Finally, the probability that all the photoelectrons recombine, $P_r$, is given
by the binomial distribution, and simplifies to
\begin{equation}
    P_r = \text{CCE}(\lambda)^{\text{IQY}(\lambda)}
\end{equation}
where $\text{IQY}(\lambda)$ is the ideal \QY, and is given by \citet{Janesick2001}
as
\begin{equation}
    \text{IQY}(\lambda) = \begin{cases}
        0, & 0 < \epsilon < E_\text{g} \\
        1, & E_\text{g} < \epsilon < E_\text{eh} \\
        E_\text{eh} / \epsilon, & E_\text{eh} < \epsilon < \infty,
    \end{cases}
\end{equation}
where $\epsilon = h \nu$ is the energy of an incident photon, 
$E_\text{g} = \bandgapEnergy$ is the bandgap energy of silicon,
and $E_\text{eh} = \electronHoleEnergy$ is the energy required to generate one
electron-hole pair at room temperature.
"""
    )
    return result
