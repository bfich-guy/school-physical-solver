from decimal import Decimal


#region Electric current

def get_electric_current_by_electric_power_and_electric_voltage(
    *,
    electric_power: Decimal,
    electric_voltage: Decimal,
) -> Decimal:

    electric_current: Decimal = electric_power / electric_voltage
    return electric_current


def get_electric_current_by_electric_voltage_and_electric_resistance(
    *,
    electric_voltage: Decimal,
    electric_resistance: Decimal,
) -> Decimal:

    electric_current: Decimal = electric_voltage / electric_resistance
    return electric_current


def get_electric_current_by_electromotive_force_and_electric_voltage_and_electric_internal_resistance(
    *,
    electromotive_force: Decimal,
    electric_voltage: Decimal,
    electric_internal_resistance: Decimal,
) -> Decimal:

    electric_current: Decimal = (electromotive_force - electric_voltage) / electric_internal_resistance
    return electric_current


def get_electric_current_by_ampere_force_and_magnetic_induction_and_conductor_length_and_angle_sinus(
    *,
    ampere_force: Decimal,
    magnetic_induction: Decimal,
    conductor_length: Decimal,
    angle_sinus: Decimal,
) -> Decimal:
    
    electric_current: Decimal = ampere_force / (magnetic_induction * conductor_length * angle_sinus)
    return electric_current

#endregion
