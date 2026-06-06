from decimal import Decimal

from utils import get_decimal_array_from_string_array

def get_kinetic_energy_by_mass_and_velocity(*,
                                            mass: str,
                                            velocity: str,
                                            ) -> Decimal | None:
    
    string_value_array: list[str] = [mass, velocity]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    decimal_mass, decimal_velocity = decimal_value_array
    kinetic_energy: Decimal = (decimal_mass * (decimal_velocity ** 2)) / 2
    return kinetic_energy

