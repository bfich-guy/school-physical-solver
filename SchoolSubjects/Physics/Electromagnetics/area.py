from decimal import Decimal


#region Cross-sectional area

def get_cross_sectional_area_by_electric_resistivity_and_conductor_length_and_general_resistance(
    *,
    electric_resistivity: Decimal,
    conductor_length: Decimal,
    general_resistance: Decimal,
) -> Decimal:

    cross_sectional_area: Decimal = (electric_resistivity * conductor_length) / general_resistance
    return cross_sectional_area

#endregion
