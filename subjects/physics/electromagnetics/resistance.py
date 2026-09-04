from decimal import Decimal


#region External resistance

def get_electric_external_resistance_by_electric_voltage_and_electric_current(
    *,
    electric_voltage: Decimal,
    electric_current: Decimal,
) -> Decimal:

    electric_external_resistance: Decimal = electric_voltage / electric_current
    return electric_external_resistance


def get_electric_external_resistance_by_electric_resistivity_and_conductor_length_and_cross_sectional_area(
    *,
    electric_resistivity: Decimal,
    conductor_length: Decimal,
    cross_sectional_area: Decimal,
) -> Decimal:

    electric_external_resistance: Decimal = (electric_resistivity * conductor_length) / cross_sectional_area
    return electric_external_resistance

#endregion


#region Electric resistivity

def get_electric_resistivity_by_electric_external_resistance_and_cross_sectional_area_and_conductor_length(
    *,
    electric_external_resistance: Decimal,
    cross_sectional_area: Decimal,
    conductor_length: Decimal,
) -> Decimal:

    electric_resistivity: Decimal = (electric_external_resistance * cross_sectional_area) / conductor_length
    return electric_resistivity

#endregion


#region Internal resistance

def get_electric_internal_resistance_by_electromotive_force_and_electric_voltage_and_electric_current(
    *,
    electromotive_force: Decimal,
    electric_voltage: Decimal,
    electric_current: Decimal,
) -> Decimal:

    electric_internal_resistance: Decimal = (electromotive_force - electric_voltage) / electric_current
    return electric_internal_resistance

#endregion
