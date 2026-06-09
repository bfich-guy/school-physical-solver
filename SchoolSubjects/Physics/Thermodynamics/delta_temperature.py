from decimal import Decimal

from utils import get_decimal_array_from_string_array

def get_delta_temperature_by_sensible_heat_and_mass_and_specific_heat(*,
                                                                      sensible_heat: str,
                                                                      mass: str,
                                                                      specific_heat: str,
                                                                      ) -> Decimal | None:
    
    string_value_array: list[str] = [sensible_heat, mass, specific_heat]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_sensible_heat, decimal_mass, decimal_specific_heat = decimal_value_array
        delta_temperature: Decimal = decimal_sensible_heat / (decimal_mass * decimal_specific_heat)
        return delta_temperature
    except ZeroDivisionError:
        return None
    
