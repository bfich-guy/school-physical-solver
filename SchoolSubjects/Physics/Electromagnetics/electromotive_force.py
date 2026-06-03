from decimal import Decimal

from utils import get_decimal_array_from_string_array

def get_electromotive_force_by_current_and_external_resistance_and_internal_resistance(*,
                                                                                       current: str,
                                                                                       external_resistance: str,
                                                                                       internal_resistance: str
                                                                                       ) -> Decimal | None:
    
    string_value_array: list[str] = [current, external_resistance, internal_resistance]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    decimal_current, decimal_external_resistance, decimal_internal_resistance = decimal_value_array
    electromotive_force: Decimal = decimal_current * (decimal_external_resistance + decimal_internal_resistance)
    return electromotive_force

def get_electromotive_force_by_work_and_charge(*,
                                               work: str,
                                               charge: str,
                                               ) -> Decimal | None:
    
    string_value_array: list[str] = [work, charge]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_work, decimal_charge = decimal_value_array
        electromotive_force: Decimal = decimal_work / decimal_charge
        return electromotive_force
    except ZeroDivisionError:
        return None
    
def get_electromotive_force_by_voltage_and_current_and_internal_resistance(*,
                                                                           voltage: str,
                                                                           current: str,
                                                                           internal_resistance: str,
                                                                           ) -> Decimal | None:
    
    string_value_array: list[str] = [voltage, current, internal_resistance]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    decimal_voltage, decimal_current, decimal_internal_resistance = decimal_value_array
    electromotive_force: Decimal = decimal_voltage + (decimal_current * decimal_internal_resistance)
    return electromotive_force

