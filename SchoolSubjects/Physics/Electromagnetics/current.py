from decimal import Decimal, InvalidOperation

from utils import get_decimal_array_from_string_array

def get_current_by_resistance_and_voltage(*,
                                          resistance: str,
                                          voltage: str,
                                          ) -> Decimal | None:
    
    string_value_array: list[str] = [resistance, voltage]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_resistance, decimal_voltage = decimal_value_array
        current: Decimal = decimal_voltage / decimal_resistance
        return current
    except ZeroDivisionError:
        return None
    
def get_current_by_dissipated_heat_and_resistance_and_time(*,
                                                           dissipated_heat: str,
                                                           resistance: str,
                                                           time: str,
                                                           ) -> Decimal | None:
    
    string_value_array: list[str] = [dissipated_heat, resistance, time]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_dissipated_heat, decimal_resistance, decimal_time = decimal_value_array
        current: Decimal = (decimal_dissipated_heat / (decimal_resistance * decimal_time)).sqrt()
        return current
    except (ZeroDivisionError, InvalidOperation):
        return None
    
def get_current_by_dissipated_heat_and_voltage_and_time(*,
                                                        dissipated_heat: str,
                                                        voltage: str,
                                                        time: str,
                                                        ) -> Decimal | None:
    
    string_value_array: list[str] = [dissipated_heat, voltage, time]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_dissipated_heat, decimal_voltage, decimal_time = decimal_value_array
        current: Decimal = decimal_dissipated_heat / (decimal_voltage * decimal_time)
        return current
    except ZeroDivisionError:
        return None

def get_current_by_power_and_voltage(*,
                                     power: str,
                                     voltage: str,
                                     ) -> Decimal | None:
    
    string_value_array: list[str] = [power, voltage]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_power, decimal_voltage = decimal_value_array
        current: Decimal = decimal_power / decimal_voltage
        return current
    except ZeroDivisionError:
        return None
    
