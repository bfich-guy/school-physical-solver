from decimal import Decimal, InvalidOperation

from utils import get_decimal_array_from_string_array

def get_geometric_progression_sum_by_first_term_and_last_term_and_ratio(*,
                                                                        first_term: str,
                                                                        last_term: str,
                                                                        ratio: str,
                                                                        ) -> Decimal | None:
    
    string_value_array: list[str] = [first_term, last_term, ratio]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_first_term, decimal_last_term, decimal_ratio = decimal_value_array
        geometric_progression_sum: Decimal = (decimal_last_term * decimal_ratio - decimal_first_term) / (decimal_ratio - 1)
        return geometric_progression_sum
    except (ZeroDivisionError, InvalidOperation):
        return None

def get_geometric_progression_sum_by_first_term_and_step_and_term_amount(*,
                                                                         first_term: str,
                                                                         step: str,
                                                                         term_amount: str,
                                                                         ) -> Decimal | None:
    
    string_value_array: list[str] = [first_term, step, term_amount]
    decimal_value_array: list[Decimal] | None = get_decimal_array_from_string_array(string_array=string_value_array)

    decimal_value_array_is_none: bool = decimal_value_array is None

    if decimal_value_array_is_none:
        return None
    
    try:
        decimal_first_term, decimal_step, decimal_term_amount = decimal_value_array
        decimal_step_equals_one: bool = decimal_step == 1

        if decimal_step_equals_one:
            geometric_progression_sum: Decimal = decimal_first_term * decimal_term_amount
            return geometric_progression_sum
        else:
            geometric_progression_sum: Decimal = decimal_first_term * (pow(decimal_step, decimal_term_amount) - 1) / (decimal_step - 1)
            return geometric_progression_sum
    except (ZeroDivisionError, InvalidOperation):
        return None
    
