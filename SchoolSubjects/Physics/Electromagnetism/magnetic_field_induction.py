from decimal import Decimal

from utils import get_decimal_array_from_string_array

def get_magnetic_field_induction_by_ampere_force_and_current_and_length_and_angle_sinus(*,
                                                                                        ampere_force: str,
                                                                                        current: str,
                                                                                        length: str,
                                                                                        angle_sinus: str = "1",
                                                                                        ) -> Decimal | None:
    
    string_value_array: list[str] = [ampere_force, current, length, angle_sinus]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    if decimal_value_array is None:
        return None
    
    try:
        decimal_ampere_force, decimal_current, decimal_length, decimal_angle_sinus = decimal_value_array
        magnetic_field_induction: Decimal = decimal_ampere_force / (decimal_current * decimal_length * decimal_angle_sinus)
        return magnetic_field_induction
    except ZeroDivisionError:
        return None

