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

def get_potential_energy_by_gravitational_force_and_lift_height(
    *,
    gravitational_force: Decimal,
    lift_height: Decimal,
) -> Decimal:

    potential_energy: Decimal = gravitational_force * lift_height
    return potential_energy

#endregion
