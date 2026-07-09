from decimal import Decimal


#region Electric current

def get_electric_current_by_electric_power_and_electric_voltage(
    *,
    electric_power: Decimal,
    electric_current: Decimal,
) -> Decimal:

    electric_current: electric_power / electric_voltage
    return electric_current


def get_electric_current_by_electric_voltage_and_electric_resistance(
    *,
    electric_voltage: Decimal,
    electric_resistance: Decimal,
) -> Decimal:

    electric_current: Decimal = electric_voltage / electric_resistance
    return electric_current

#endregion
