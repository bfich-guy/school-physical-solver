from decimal import Decimal

from utils import get_decimal_array_from_string_array

def get_ampere_force_by_magnetic_field_induction_and_current_and_length_and_angle_sinus(*,
                                                                                        magnetic_field_induction: str,
                                                                                        current: str,
                                                                                        length: str,
                                                                                        angle_sinus: str,
                                                                                        ) -> Decimal | None:
    
    string_value_array: list[str] = [magnetic_field_induction, current, length, angle_sinus]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    decimal_magnetic_field_induction, decimal_current, decimal_length, decimal_angle_sinus = decimal_value_array
    ampere_force: Decimal = decimal_magnetic_field_induction * decimal_current * decimal_length * decimal_angle_sinus
    return ampere_force

