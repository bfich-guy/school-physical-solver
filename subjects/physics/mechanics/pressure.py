from decimal import Decimal


#region Mechanic pressure

def get_mechanic_pressure_by_general_force_and_general_area(
    *,
    general_force: Decimal,
    general_area: Decimal,
) -> Decimal:

    mechanic_pressure: Decimal = general_force / general_area
    return mechanic_pressure

#endregion


#region Hydrostatic pressure

def get_hydrostatic_pressure_by_general_density_and_gravitational_acceleration_and_fluid_height(
    *,
    general_density: Decimal,
    gravitational_acceleration: Decimal,
    fluid_height: Decimal,
) -> Decimal:

    hydrostatic_pressure: Decimal = general_density * gravitational_acceleration * fluid_height
    return hydrostatic_pressure

#endregion
