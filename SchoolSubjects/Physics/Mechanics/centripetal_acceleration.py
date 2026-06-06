from decimal import Decimal

from utils import get_decimal_array_from_string_array

def get_centripetal_acceleration_by_linear_velocity_and_radius(*,
                                                               linear_velocity: str,
                                                               radius: str,
                                                               ) -> Decimal | None:
    
    string_value_array: list[str] = [linear_velocity, radius]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_linear_velocity, decimal_radius = decimal_value_array
        centripetal_acceleration: Decimal = pow(decimal_linear_velocity, 2) / decimal_radius
        return centripetal_acceleration
    except ZeroDivisionError:
        return None
    
def get_centripetal_acceleration_by_angular_velocity_and_radius(*,
                                                                angular_velocity: str,
                                                                radius: str,
                                                                ) -> Decimal | None:
    
    string_value_array: list[str] = [angular_velocity, radius]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    decimal_angular_velocity, decimal_radius = decimal_value_array
    centripetal_acceleration: Decimal = pow(decimal_angular_velocity, 2) * decimal_radius
    return centripetal_acceleration

