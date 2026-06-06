from decimal import Decimal

from utils import get_decimal_array_from_string_array

def get_elastic_force_by_hardness_coefficient_and_elongation(*,
                                                             hardness_coefficient: str,
                                                             elongation: str,
                                                             ) -> Decimal | None:
    
    string_value_array: list[str] = [hardness_coefficient, elongation]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    decimal_hardness_coefficient, decimal_elongation = decimal_value_array
    elastic_force: Decimal = decimal_hardness_coefficient * decimal_elongation
    return elastic_force

