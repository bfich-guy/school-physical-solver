from decimal import Decimal

from utils import get_decimal_array_from_string_array

def get_elongation_by_elastic_force_and_hardness_coefficient(*,
                                                             elastic_force: str,
                                                             hardness_coefficient: str,
                                                             ) -> Decimal | None:

    string_value_array: list[str] = [elastic_force, hardness_coefficient]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_elastic_force, decimal_elastic_force = decimal_value_array
        elongation: Decimal = decimal_elastic_force / decimal_elastic_force
        return elongation
    except ZeroDivisionError:
        return None
    
