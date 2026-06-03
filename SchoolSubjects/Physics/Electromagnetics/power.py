from decimal import Decimal

from utils import get_decimal_array_from_string_array

def get_power_by_current_and_voltage(*,
                                     current: str,
                                     voltage: str,
                                     ) -> Decimal | None:
    
    string_value_array: list[str] = [current, voltage]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    decimal_current, decimal_voltage = decimal_value_array
    power: Decimal = decimal_current * decimal_voltage
    return power

def get_power_by_current_and_resistance(*,
                                        current: str,
                                        resistance: str,
                                        ) -> Decimal | None:
    
    string_value_array: list[str] = [current, resistance]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_current, decimal_resistance = decimal_value_array
        power: Decimal = pow(decimal_current, 2) * decimal_resistance
        return power
    except ZeroDivisionError:
        return None
    
