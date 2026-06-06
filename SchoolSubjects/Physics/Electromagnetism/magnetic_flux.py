from decimal import Decimal

from utils import get_decimal_array_from_string_array

def get_magnetic_flux_by_magnetic_field_induction_and_area_and_angle_cosinus(*,
                                                                             magnetic_field_induction: str,
                                                                             area: str,
                                                                             angle_cosinus: str = "1",
                                                                             ) -> Decimal | None:
    
    string_value_array: list[str] = [magnetic_field_induction, area, angle_cosinus]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    decimal_magnetic_field_induction, decimal_area, decimal_angle_cosinus = decimal_value_array
    magnetic_flux: Decimal = decimal_magnetic_field_induction * decimal_area * decimal_angle_cosinus
    return magnetic_flux

