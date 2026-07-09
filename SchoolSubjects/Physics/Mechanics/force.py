from decimal import Decimal

from config import GRAVITATIONAL_ACCELERATION


#region Resultive force

def get_resultant_force_by_object_mass_and_general_acceleration(
    *,
    object_mass: Decimal,
    general_acceleration: Decimal = GRAVITATIONAL_ACCELERATION,
) -> Decimal:

    resultant_force: Decimal = object_mass * general_acceleration
    return resultant_force

#endregion


#region Buoyant force

def get_buoyant_force_by_fluid_density_and_gravitational_acceleration_and_submerged_volume(
    *,
    fluid_density: Decimal,
    gravitational_acceleration: Decimal = GRAVITATIONAL_ACCELERATION,
    submerged_volume: Decimal,
) -> Decimal:

    buoyant_force: Decimal = fluid_density * gravitational_acceleration * submerged_volume
    return buoyant_force

#endregion
