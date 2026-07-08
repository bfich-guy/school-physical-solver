from decimal import Decimal

#region Mass

def get_mass_by_density_and_volume(
    *,
    density: Decimal,
    volume: Decimal,
) -> Decimal:

    mass: Decimal = density * volume
    return mass


def get_mass_by_resultant_force_and_general_acceleration(
    *,
    resultant_force: Decimal,
    general_acceleration: Decimal,
) -> Decimal:

    mass: Decimal = resultant_force / general_acceleration
    return mass


def get_mass_by_momentum_and_linear_velocity(
    *,
    momentum: Decimal,
    linear_velocity: Decimal,
) -> Decimal:

    mass: Decimal = momentum / linear_velocity
    return mass

#endregion
