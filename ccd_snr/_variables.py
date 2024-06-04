import optika
import aastex

__all__ = [
    "variables",
]


def variables() -> list[aastex.Command]:
    """
    A list of numeric variables used in this article.
    """
    return [
        aastex.Variable(
            name="bandgapEnergy",
            value=optika.sensors.energy_bandgap,
        ),
        aastex.Variable(
            name="electronHoleEnergy",
            value=optika.sensors.energy_electron_hole,
        ),
    ]
