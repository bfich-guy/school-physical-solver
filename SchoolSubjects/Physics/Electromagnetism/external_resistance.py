from decimal import Decimal

from utils import get_decimal_array_from_string_array

def get_external_resistance_by_current_and_voltage(*,
                                                   current: str,
                                                   voltage: str,
                                                   ) -> Decimal | None:
    
    string_value_array: list[str] = [current, voltage]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_current, decimal_voltage = decimal_value_array
        resistance: Decimal = decimal_voltage / decimal_current
        return resistance
    except ZeroDivisionError:
        return None

def get_external_resistance_by_dissipated_heat_and_voltage_and_time(*,
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
        resistance: Decimal = decimal_dissipated_heat / (decimal_voltage * decimal_time)
        return resistance
    except ZeroDivisionError:
        return None

def get_external_resistance_by_dissipated_heat_and_current_and_time(*,
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
        resistance: Decimal = decimal_dissipated_heat / (pow(decimal_current, 2) * decimal_time)
        return resistance
    except ZeroDivisionError:
        return None
    
def get_external_resistance_by_electromotive_force_and_current_and_internal_resistance(*,
                                                                                       electromotive_force: str,
                                                                                       current: str,
                                                                                       internal_resistance: str,
                                                                                       ) -> Decimal | None:
    
    string_value_array: list[str] = [electromotive_force, current, internal_resistance]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_electromotive_force, decimal_current, decimal_internal_resistance = decimal_value_array
        resistance: Decimal = (decimal_electromotive_force - (decimal_current * decimal_internal_resistance)) / decimal_current
        return resistance
    except ZeroDivisionError:
        return None
    
