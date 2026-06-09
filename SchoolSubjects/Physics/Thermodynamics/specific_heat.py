from decimal import Decimal

from utils import get_decimal_array_from_string_array

def get_specific_heat_by_sensible_heat_and_mass_and_delta_temperature(*,
                                                                      sensible_heat: str,
                                                                      mass: str,
                                                                      delta_temperature: str,
                                                                      ) -> Decimal | None:
    
    string_value_array: list[str] = [sensible_heat, mass, delta_temperature]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_sensible_heat, decimal_mass, decimal_delta_temperature = decimal_value_array
        specific_heat: Decimal = decimal_sensible_heat / (decimal_mass * decimal_delta_temperature)
        return specific_heat
    except ZeroDivisionError:
        return None
    
