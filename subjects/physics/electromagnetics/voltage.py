from decimal import Decimal


#region General voltage

def get_general_voltage_by_general_current_and_electric_power(
    *,
    general_current: Decimal,
    electric_power: Decimal,
) -> Decimal:

    general_voltage: Decimal = electric_power / general_current
    return general_voltage


def get_general_voltage_by_general_current_and_general_resistance(
    *,
    general_current: Decimal,
    general_resistance: Decimal,
) -> Decimal:

    general_voltage: Decimal = general_current * general_resistance
    return general_voltage


def get_general_voltage_by_electromotive_force_and_general_current_and_internal_resistance(
    *,
    electromotive_force: Decimal,
    general_current: Decimal,
    internal_resistance: Decimal,
) -> Decimal:

    general_voltage: Decimal = electromotive_force - (general_current * internal_resistance)
    return general_voltage

#endregion
