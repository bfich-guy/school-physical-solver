from decimal import Decimal

from utils import get_decimal_array_from_string_array

def get_linear_acceleration_by_total_force_and_mass(*,
                                                    total_force: str,
                                                    mass: str,
                                                    ) -> Decimal | None:
    
    string_value_array: list[str] = [total_force, mass]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_total_force, decimal_mass = decimal_value_array
        linear_acceleration: Decimal = decimal_total_force / decimal_mass
        return linear_acceleration
    except ZeroDivisionError:
        return None
    
def get_linear_acceleration_by_delta_velocity_and_delta_time(*,
                                                             delta_velocity: str,
                                                             delta_time: str,
                                                             ) -> Decimal | None:
    
    string_value_array: list[str] = [delta_velocity, delta_time]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_delta_velocity, decimal_delta_time = decimal_value_array
        linear_acceleration: Decimal = decimal_delta_velocity / decimal_delta_time
        return linear_acceleration
    except ZeroDivisionError:
        return None
    
