from decimal import Decimal


#region Electric power

def get_electric_power_by_electric_voltage_and_electric_current(
    *,
    electric_voltage: Decimal,
    electric_current: Decimal,
) -> Decimal:

    electric_power: Decimal = electric_voltage * electric_current
    return electric_power


def get_electric_power_by_joule_heat_and_heating_duration(
    *,
    joule_heat: Decimal,
    heating_duration: Decimal,
) -> Decimal:

    electric_power: Decimal = joule_heat / heating_duration
    return electric_power

#endregion
