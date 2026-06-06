from decimal import Decimal, InvalidOperation

from utils import get_decimal_array_from_string_array

def get_dissipated_heat_by_power_and_time(*,
                                          power: str,
                                          time: str,
                                          ) -> Decimal | None:
    
    string_value_array: list[str] = [power, time]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    decimal_power, decimal_time = decimal_value_array
    dissipated_heat: Decimal = decimal_power * decimal_time
    return dissipated_heat

