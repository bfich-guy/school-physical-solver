from decimal import Decimal

from utils import get_decimal_array_from_string_array

def get_volume_by_mass_and_density(*,
                                   mass: str,
                                   density: str,
                                   ) -> Decimal | None:
    
    string_value_array: list[str] = [mass, density]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_mass, decimal_density = decimal_value_array
        volume: Decimal = decimal_mass / decimal_density
        return volume
    except ZeroDivisionError:
        return None
    
def get_volume_by_total_force_and_density_and_acceleration(*,
                                                           total_force: str,
                                                           density: str,
                                                           acceleration: str,
                                                           ) -> Decimal | None:
    
    string_value_array: list[str] = [total_force, density, acceleration]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_total_force, decimal_density, decimal_acceleration = decimal_value_array
        volume: Decimal = decimal_total_force / (decimal_density * decimal_acceleration)
        return volume
    except ZeroDivisionError:
        return None
    
def get_volume_by_sensible_heat_and_specific_heat_and_density_and_delta_temperature(*,
                                                                                    sensible_heat: str,
                                                                                    specific_heat: str,
                                                                                    density: str,
                                                                                    delta_temperature: str,
                                                                                    ) -> Decimal | None:
    
    string_value_array: list[str] = [sensible_heat, specific_heat, density, delta_temperature]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_sensible_heat, decimal_specific_heat, decimal_density, decimal_delta_temperature = decimal_value_array
        volume: Decimal = decimal_sensible_heat / (decimal_specific_heat * decimal_density * decimal_delta_temperature)
        return volume
    except ZeroDivisionError:
        return None

