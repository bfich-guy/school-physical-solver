from decimal import Decimal

from utils import get_decimal_array_from_string_array

def get_voltage_by_current_and_resistance(*,
                                          current: str,
                                          resistance: str,
                                          ) -> Decimal | None:
    
    string_value_array: list[str] = [current, resistance]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    decimal_current, decimal_resistance = decimal_value_array
    voltage: Decimal = decimal_current * decimal_resistance
    return voltage

def get_voltage_by_dissipated_heat_and_current_and_time(*,
                                                        dissipated_heat: str,
                                                        current: str,
                                                        time: str,
                                                        ) -> Decimal | None:
    
    string_value_array: list[str] = [dissipated_heat, current, time]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_dissipated_heat, decimal_current, decimal_time = decimal_value_array
        voltage: Decimal = decimal_dissipated_heat / (decimal_current * decimal_time)
        return voltage
    except ZeroDivisionError:
        return None

def get_voltage_by_power_and_current(*,
                                     power: str,
                                     current: str,
                                     ) -> Decimal | None:
    
    string_value_array: list[str] = [power, current]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_power, decimal_current = decimal_value_array
        voltage: Decimal = decimal_power / decimal_current
        return voltage
    except ZeroDivisionError:
        return None

