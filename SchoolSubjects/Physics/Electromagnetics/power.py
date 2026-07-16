from decimal import Decimal


#region Electric power

def get_electric_power_by_general_voltage_and_general_current(
    *,
    general_voltage: Decimal,
    general_current: Decimal,
) -> Decimal:

    electric_power: Decimal = general_voltage * general_current
    return electric_power


def get_electric_power_by_joule_heat_and_heating_duration(
    *,
    joule_heat: Decimal,
    heating_duration: Decimal,
) -> Decimal:

    electric_power: Decimal = joule_heat / heating_duration
    return electric_power

#endregion
