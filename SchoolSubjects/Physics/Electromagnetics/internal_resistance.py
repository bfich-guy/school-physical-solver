from decimal import Decimal

from utils import get_decimal_array_from_string_array

def get_external_resistance_by_electromotive_force_and_current_and_external_resistance(*,
                                                                                       electromotive_force: str,
                                                                                       current: str,
                                                                                       external_resistance: str,
                                                                                       ) -> Decimal | None:
    
    string_value_array: list[str] = [electromotive_force, current, external_resistance]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_electromotive_force, decimal_current, decimal_external_resistance = decimal_value_array
        resistance: Decimal = (decimal_electromotive_force - (decimal_current * decimal_external_resistance)) / decimal_current
        return resistance
    except ZeroDivisionError:
        return None
    
