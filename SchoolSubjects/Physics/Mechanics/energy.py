from decimal import Decimal


#region Kinetic energy

def get_kinetic_energy_by_linear_momentum_and_linear_velocity(
    *,
    linear_momentum: Decimal,
    linear_velocity: Decimal,
) -> Decimal:

    kinetic_energy: Decimal = (linear_momentum * linear_velocity) / Decimal("2")
    return kinetic_energy

#endregion


#region Potential energy

def get_potential_energy_by_force_and_height(
    *,
    force: Decimal,
    height: Decimal,
) -> Decimal:

    potential_energy: Decimal = force * height
    return potential_energy

#endregion
