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
        
The \QE\ is the most common metric for measuring \CCD\ sensitivity and is given 
by \citet{Janesick2001} as
\begin{equation} \label{quantum-efficiency}
    \text{QE}(\lambda) = \frac{N_{e}(\lambda)}{N_\gamma}
                       = T(\lambda) \times \text{IQY}(\lambda) \times \text{CCE}(\lambda),
\end{equation}
where $N_e(\lambda)$ is the number of electrons measured by the sensor for a 
given wavelength $\lambda$,
$N_\gamma$ is the total number of photons incident on the sensor,
$T(\lambda)$ is the transmissivity of the vacuum/SiO$_2$/Si interface , 
$\text{IQY}(\lambda)$ is the ideal \QY, the number of photoelectrons generated 
per absorbed photon,
and $\text{CCE}(\lambda)$ is the charge-collection efficiency, the fraction of 
photoelectrons measured by the sensor.

$T(\lambda)$ can be determined using any number of multilayer codes, such as IMD
\citep{Windt1998}.
For this work, we used our software, \texttt{optika} \citep{optika}, 
which has a convenient Python interface and uses
the transfer matrix method described in \citet{Yeh1988} with the optical constants
from \citet{Palik1997} and \cite{Henke1993}.

The ideal \QY\ is given by \citet{Janesick2001} as
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

In \citet{Stern1994}, the \CCE\ is expressed in terms of differential \CCE,
$\eta(z)$, which is the fraction of photoelectrons collected for a photon 
absorbed at a depth $z$ into the epitaxial layer.
The total \CCE\ is then the average differential \CCE\ weighted by 
the probability of absorbing a photon at a depth $z$,
\begin{equation} \label{cce}
    \text{CCE}(\lambda) = \frac{\int_0^\infty \eta(z) \exp(-\alpha z) \, dz}
                               {\int_0^\infty \exp(-\alpha z) \, dz},
\end{equation}
where $\alpha$ is the absorption coefficient of silicon for the given wavelength.

In principle, $\eta(z)$ is a function of the exact implant profile which is
usually impractical to measure, but see \cite{Stern2004} for a case where the
authors did have a measurement of the exact implant profile.
In \citet{Stern1994}, the authors instead adopt a piecewise-linear approximation of
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
which can be used in Equation \ref{quantum-efficiency} to determine the \QE.
"""
    )
    return result
