from decimal import Decimal

from utils import get_decimal_array_from_string_array

def get_hardness_coefficient_by_elastic_force_and_elongation(*,
                                                             elastic_force: str,
                                                             elongation: str,
                                                             ) -> Decimal | None:

    string_value_array: list[str] = [elastic_force, elongation]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_elastic_force, decimal_elongation = decimal_value_array
        hardness_coefficient: Decimal = decimal_elastic_force / decimal_elongation
        return hardness_coefficient
    except ZeroDivisionError:
        return None
    
