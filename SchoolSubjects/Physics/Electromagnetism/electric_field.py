from decimal import Decimal

from utils import get_decimal_array_from_string_array
from config.physics import COULOMB_CONSTANT

def get_electric_field_strength_by_force_and_charge(*,
                                                    force: str,
                                                    charge: str,
                                                    ) -> Decimal | None:
    
    string_value_array: list[str] = [force, charge]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_force, decimal_charge = decimal_value_array
        electric_field_strength: Decimal = decimal_force / decimal_charge
        return electric_field_strength
    except ZeroDivisionError:
        return None
    
def get_electric_field_strength_by_voltage_and_distance(*,
                                                        voltage: str,
                                                        distance: str,
                                                        ) -> Decimal | None:
    
    string_value_array: list[str] = [voltage, distance]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_voltage, decimal_distance = decimal_value_array
        electric_field_strength: Decimal = decimal_voltage / decimal_distance
        return electric_field_strength
    except ZeroDivisionError:
        return None
    
def get_electric_field_strength_by_charge_and_distance(*,
                                                       charge: str,
                                                       distance: str,
                                                       ) -> Decimal | None:
    
    string_value_array: list[str] = [charge, distance]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_charge, decimal_distance = decimal_value_array
        electric_field_strength: Decimal = (COULOMB_CONSTANT * decimal_charge) / pow(decimal_distance, 2)
        return electric_field_strength
    except ZeroDivisionError:
        return None
    
