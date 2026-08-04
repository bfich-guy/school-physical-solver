from decimal import Decimal


#region Conductor length

def get_conductor_length_by_general_resistance_and_cross_sectional_area_and_electric_resistivity(
    *,
    general_resistance: Decimal,
    cross_sectional_area: Decimal,
    electric_resistivity: Decimal,
) -> Decimal:

    conductor_length: Decimal = (general_resistance * cross_sectional_area) / electric_resistivity
    return conductor_length

#endregion
