from decimal import Decimal

from utils import get_decimal_array_from_string_array

def get_total_force_by_mass_and_acceleration(*,
                                             mass: str,
                                             accelearation: str,
                                             ) -> Decimal | None:

    string_value_array: list[str] = [mass, accelearation]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    decimal_mass, decimal_accelearation = decimal_value_array
    total_force: Decimal = decimal_mass * decimal_accelearation
    return total_force

