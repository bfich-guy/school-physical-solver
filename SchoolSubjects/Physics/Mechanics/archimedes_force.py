from decimal import Decimal

from utils import get_decimal_array_from_string_array

def get_archimedes_force_by_fluid_density_and_gravity_acceleration_and_submerged_volume(*,
                                                                                        fluid_density: str,
                                                                                        gravity_acceleration: str,
                                                                                        submerged_volume: str,
                                                                                        ) -> Decimal | None:
    
    string_value_array: list[str] = [fluid_density, gravity_acceleration, submerged_volume]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    decimal_fluid_density, decimal_gravity_acceleration, decimal_submerged_volume = decimal_value_array
    archimedes_force: Decimal = decimal_fluid_density * decimal_gravity_acceleration * decimal_submerged_volume
    return archimedes_force

