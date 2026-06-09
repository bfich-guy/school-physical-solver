from decimal import Decimal

from utils import get_decimal_array_from_string_array

def get_density_by_mass_and_volume(*,
                                   mass: str,
                                   volume: str,
                                   ) -> Decimal | None:
    
    string_value_array: list[str] = [mass, volume]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_mass, decimal_volume = decimal_value_array
        density: Decimal = decimal_mass / decimal_volume
        return density
    except ZeroDivisionError:
        return None
    
def get_density_by_total_force_and_volume_and_acceleration(*,
                                                           total_force: str,
                                                           volume: str,
                                                           acceleration: str,
                                                           ) -> Decimal | None:
    
    string_value_array: list[str] = [total_force, volume, acceleration]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_total_force, decimal_volume, decimal_acceleration = decimal_value_array
        density: Decimal = decimal_total_force / (decimal_volume * decimal_acceleration)
        return density
    except ZeroDivisionError:
        return None
    
