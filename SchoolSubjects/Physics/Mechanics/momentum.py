from decimal import Decimal

#region Momentum

def get_momentum_by_mass_and_linear_velocity(
    *,
    mass: Decimal,
    linear_velocity: Decimal,
) -> Decimal:

    momentum: Decimal = mass * linear_velocity
    return momentum


def get_momentum_by_kinetic_energy_and_linear_velocity(
    *,
    kinetic_energy: Decimal,
    linear_velocity: Decimal,
) -> Decimal:

    momentum: Decimal = (Decimal("2") * kinetic_energy) / linear_velocity
    return momentum

#endregion
