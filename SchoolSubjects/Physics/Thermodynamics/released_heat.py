from decimal import Decimal

from utils import get_decimal_array_from_string_array

def get_released_heat_by_calorific_value_and_mass(*,
                                                  calorific_value: str,
                                                  mass: str,
                                                  ) -> Decimal | None:
    
    string_value_array: list[str] = [calorific_value, mass]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    decimal_calorific_value, decimal_mass = decimal_value_array
    released_heat: Decimal = decimal_calorific_value * decimal_mass
    return released_heat

