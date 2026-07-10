from decimal import Decimal

from System.config import GRAVITATIONAL_ACCELERATION


#region Material density

def get_material_density_by_object_mass_and_object_volume(
    *,
    object_mass: Decimal,
    object_volume: Decimal,
) -> Decimal:

    material_density: Decimal = object_mass / object_volume
    return material_density

#endregion


#region Fluid density

def get_fluid_density_by_buoyant_force_and_gravitational_acceleration_and_submerged_volume(
    *,
    buoyant_force: Decimal,
    gravitational_acceleration: Decimal = GRAVITATIONAL_ACCELERATION,
    submerged_volume: Decimal,
) -> Decimal:

    fluid_density: Decimal = buoyant_force / (gravitational_acceleration * submerged_volume)
    return fluid_density

#endregion
