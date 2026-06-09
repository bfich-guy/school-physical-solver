from decimal import Decimal

from utils import get_decimal_array_from_string_array

def get_calorific_value_by_released_heat_and_mass(*,
                                                  released_heat: str,
                                                  mass: str,
                                                  ) -> Decimal | None:
    
    string_value_array: list[str] = [released_heat, mass]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_released_heat, decimal_mass = decimal_value_array
        calorific_value: Decimal = decimal_released_heat / decimal_mass
        return calorific_value
    except ZeroDivisionError:
        return None
    
