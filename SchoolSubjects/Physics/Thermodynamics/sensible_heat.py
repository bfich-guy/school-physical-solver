from decimal import Decimal

from utils import get_decimal_array_from_string_array

def get_sensible_heat_by_specific_heat_and_mass_and_delta_temperature(*,
                                                                      specific_heat: str,
                                                                      mass: str,
                                                                      delta_temperature: str,
                                                                      ) -> Decimal | None:
    
    string_value_array: list[str] = [specific_heat, mass, delta_temperature]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    decimal_specific_heat, decimal_mass, decimal_delta_temperature = decimal_value_array
    sensible_heat: Decimal = decimal_specific_heat * decimal_mass * decimal_delta_temperature
    return sensible_heat

