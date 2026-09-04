from decimal import Decimal


#region Linear momentum

def get_linear_momentum_by_object_mass_and_linear_velocity(
    *,
    object_mass: Decimal,
    linear_velocity: Decimal,
) -> Decimal:

    linear_momentum: Decimal = object_mass * linear_velocity
    return linear_momentum


def get_linear_momentum_by_kinetic_energy_and_linear_velocity(
    *,
    kinetic_energy: Decimal,
    linear_velocity: Decimal,
) -> Decimal:

    linear_momentum: Decimal = (Decimal("2") * kinetic_energy) / linear_velocity
    return linear_momentum

#endregion
