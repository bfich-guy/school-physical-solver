from decimal import Decimal


#region Electric resistance

def get_electric_resistance_by_electric_voltage_and_electric_current(
    *,
    electric_voltage: Decimal,
    electric_current: Decimal,
) -> Decimal:

    electric_resistance: Decimal = electric_voltage / electric_current
    return electric_resistance

#endregion
