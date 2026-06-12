from decimal import Decimal

from utils import get_decimal_array_from_string_array

def get_arithmetic_progression_sum_by_first_term_and_last_term_and_term_amount(*,
                                                                               first_term: str,
                                                                               last_term: str,
                                                                               term_amount: str,
                                                                               ) -> Decimal | None:
    
    string_value_array: list[str] = [first_term, last_term, term_amount]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    decimal_first_term, decimal_last_term, decimal_term_amount = decimal_value_array
    arithmetic_progression_sum: Decimal = (decimal_first_term + decimal_last_term) * (decimal_term_amount / 2)
    return arithmetic_progression_sum

def get_arithmetic_progression_sum_by_first_term_and_step_and_term_amount(*,
                                                                          first_term: str,
                                                                          step: str,
                                                                          term_amount: str,
                                                                          ) -> Decimal | None:
    
    string_value_array: list[str] = [first_term, step, term_amount]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    decimal_first_term, decimal_step, decimal_term_amount = decimal_value_array
    arithmetic_progression_sum: Decimal = (2 * decimal_first_term * (decimal_term_amount - 1) * decimal_step * decimal_term_amount) / 2
    return arithmetic_progression_sum

