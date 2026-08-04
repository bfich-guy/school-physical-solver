from decimal import Decimal


#region General current

def get_general_current_by_electric_power_and_general_voltage(
    *,
    electric_power: Decimal,
    general_voltage: Decimal,
) -> Decimal:

    general_current: Decimal = electric_power / general_voltage
    return general_current


def get_general_current_by_general_voltage_and_general_resistance(
    *,
    general_voltage: Decimal,
    general_resistance: Decimal,
) -> Decimal:

    general_current: Decimal = general_voltage / general_resistance
    return general_current


def get_general_current_by_electromotive_force_and_general_voltage_and_internal_resistance(
    *,
    electromotive_force: Decimal,
    general_voltage: Decimal,
    internal_resistance: Decimal,
) -> Decimal:

    general_current: Decimal = (electromotive_force - general_voltage) / internal_resistance
    return general_current

#endregion
