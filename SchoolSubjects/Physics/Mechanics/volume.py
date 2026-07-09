from decimal import Decimal

from config import GRAVITATIONAL_ACCELERATION

#region Object volume

def get_object_volume_by_object_mass_and_material_density(
    *,
    object_mass: Decimal,
    material_density: Decimal,
) -> Decimal:

    object_volume: Decimal = object_mass / material_density
    return object_volume

#endregion


#region Submerged volume

def get_submerged_volume_by_buoyant_force_and_fluid_density_and_gravitational_acceleration(
    *,
    buoyant_force: Decimal,
    fluid_density: Decimal,
    gravitational_acceleration: Decimal = GRAVITATIONAL_ACCELERATION
) -> Decimal:

    submerged_volume: Decimal = buoyant_force / (fluid_density * gravitational_acceleration)
    return submerged_volume

#endregion
