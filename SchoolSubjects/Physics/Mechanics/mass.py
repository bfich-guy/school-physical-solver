from decimal import Decimal

from utils import get_decimal_array_from_string_array

def get_mass_by_density_and_volume(*,
                                   density: str,
                                   volume: str,
                                   ) -> Decimal | None:
    
    string_value_array: list[str] = [density, volume]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    decimal_density, decimal_volume = decimal_value_array
    mass: Decimal = decimal_density * decimal_volume
    return mass
    
def get_mass_by_total_force_and_acceleration(*,
                                             total_force: str,
                                             acceleration: str,
                                             ) -> Decimal | None:
    
    string_value_array: list[str] = [total_force, acceleration]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_total_force, decimal_acceleration = decimal_value_array
        mass: Decimal = decimal_total_force / decimal_acceleration
        return mass
    except ZeroDivisionError:
        return None
    
def get_mass_by_sensible_heat_and_specific_heat_and_delta_temperature(*,
                                                                      sensible_heat: str,
                                                                      specific_heat: str,
                                                                      delta_temperature: str,
                                                                      ) -> Decimal | None:
    
    string_value_array: list[str] = [sensible_heat, specific_heat, delta_temperature]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_sensible_heat, decimal_specific_heat, decimal_delta_temperature = decimal_value_array
        mass: Decimal = decimal_sensible_heat / (decimal_specific_heat * decimal_delta_temperature)
        return mass
    except ZeroDivisionError:
        return None

