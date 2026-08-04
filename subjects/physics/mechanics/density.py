from decimal import Decimal


#region General density

def get_general_density_by_general_mass_and_general_volume(
    *,
    general_mass: Decimal,
    general_volume: Decimal,
) -> Decimal:

    general_density: Decimal = general_mass / general_volume
    return general_density


def get_general_density_by_hydrostatic_pressure_and_gravitational_acceleration_and_fluid_height(
    *,
    hydrostatic_pressure: Decimal,
    gravitational_acceleration: Decimal,
    fluid_height: Decimal,
) -> Decimal:

    general_density: Decimal = hydrostatic_pressure / (gravitational_acceleration * fluid_height)
    return general_density

#endregion
