from decimal import Decimal

from utils import get_decimal_array_from_string_array

def get_arithmetic_progression_step_by_first_term_and_last_term_and_term_amount(*,
                                                                                first_term: str,
                                                                                last_term: str,
                                                                                term_amount: str,
                                                                                ) -> Decimal | None:
    
    string_value_array: list[str] = [first_term, last_term, term_amount]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_first_term, decimal_last_term, decimal_term_amount = decimal_value_array
        arithmetic_progression_step: Decimal = (decimal_last_term - decimal_first_term) / (decimal_term_amount - 1)
        return arithmetic_progression_step
    except ZeroDivisionError:
        return None
    
