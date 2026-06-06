from decimal import Decimal

from utils import get_decimal_array_from_string_array

def get_potential_energy_by_total_force_and_height(*,
                                                   total_force: str,
                                                   height: str,
                                                   ) -> Decimal | None:
    
    string_value_array: list[str] = [total_force, height]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    decimal_total_force, decimal_height = decimal_value_array
    potential_energy: Decimal = decimal_total_force * decimal_height
    return potential_energy

