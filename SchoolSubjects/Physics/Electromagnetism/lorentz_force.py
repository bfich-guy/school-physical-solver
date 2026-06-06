from decimal import Decimal

from utils import get_decimal_array_from_string_array

def get_lorentz_force_by_charge_and_velocity_and_magnetic_field_induction_and_angle_sinus(*,
                                                                                          charge: str,
                                                                                          velocity: str,
                                                                                          magnetic_field_induction: str,
                                                                                          angle_sinus: str,
                                                                                          ) -> Decimal | None:
    
    string_value_array: list[str] = [charge, velocity, magnetic_field_induction, angle_sinus]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    decimal_charge, decimal_velocity, decimal_magnetic_field_induction, decimal_angle_sinus = decimal_value_array
    lorentz_force: Decimal = decimal_charge * decimal_velocity * decimal_magnetic_field_induction * decimal_angle_sinus
    return lorentz_force

