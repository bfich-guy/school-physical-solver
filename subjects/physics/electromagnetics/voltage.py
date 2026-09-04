from decimal import Decimal


#region Electric voltage

def get_electric_voltage_by_electric_current_and_electric_power(
    *,
    electric_current: Decimal,
    electric_power: Decimal,
) -> Decimal:

    electric_voltage: Decimal = electric_power / electric_current
    return electric_voltage


def get_electric_voltage_by_electric_current_and_electric_external_resistance(
    *,
    electric_current: Decimal,
    electric_external_resistance: Decimal,
) -> Decimal:

    electric_voltage: Decimal = electric_current * electric_external_resistance
    return electric_voltage


def get_electric_voltage_by_electromotive_force_and_electric_current_and_electric_external_resistance(
    *,
    electromotive_force: Decimal,
    electric_current: Decimal,
    electric_internal_resistance: Decimal,
) -> Decimal:

    electric_voltage: Decimal = electromotive_force - (electric_current * electric_internal_resistance)
    return electric_voltage

#endregion
