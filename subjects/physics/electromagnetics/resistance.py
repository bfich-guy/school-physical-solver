from decimal import Decimal


#region General resistance

def get_general_resistance_by_electric_voltage_and_electric_current(
    *,
    electric_voltage: Decimal,
    electric_current: Decimal,
) -> Decimal:

    general_resistance: Decimal = electric_voltage / electric_current
    return general_resistance


def get_general_resistance_by_electric_resistivity_and_conductor_length_and_cross_sectional_area(
    *,
    electric_resistivity: Decimal,
    conductor_length: Decimal,
    cross_sectional_area: Decimal,
) -> Decimal:

    general_resistance: Decimal = (electric_resistivity * conductor_length) / cross_sectional_area
    return general_resistance

#endregion


#region Electric resistivity

def get_electric_resistivity_by_general_resistance_and_cross_sectional_area_and_conductor_length(
    *,
    general_resistance: Decimal,
    cross_sectional_area: Decimal,
    conductor_length: Decimal,
) -> Decimal:

    electric_resistivity: Decimal = (general_resistance * cross_sectional_area) / conductor_length
    return electric_resistivity

#endregion


#region Internal resistance

def get_internal_resistance_by_electromotive_force_and_electric_voltage_and_electric_current(
    *,
    electromotive_force: Decimal,
    electric_voltage: Decimal,
    electric_current: Decimal,
) -> Decimal:

    internal_resistance: Decimal = (electromotive_force - electric_voltage) / electric_current
    return internal_resistance

#endregion
