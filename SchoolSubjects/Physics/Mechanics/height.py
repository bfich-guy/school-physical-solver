from decimal import Decimal

from System.config import PhysicsConstants


#region Lift height

def get_lift_height_by_potential_energy_and_gravitational_force(
    *,
    potential_energy: Decimal,
    gravitational_force: Decimal,
) -> Decimal:

    lift_height: Decimal = potential_energy / gravitational_force
    return lift_height

#endregion


#region Fluid height

def get_fluid_height_by_hydrostatic_pressure_and_general_density_and_gravitational_acceleration(
    *,
    hydrostatic_pressure: Decimal,
    general_density: Decimal,
    gravitational_acceleration: Decimal = PhysicsConstants.GRAVITATIONAL_ACCELERATION.value,
) -> Decimal:

    fluid_height: Decimal = hydrostatic_pressure / (general_density * gravitational_acceleration)
    return fluid_height

#endregion
