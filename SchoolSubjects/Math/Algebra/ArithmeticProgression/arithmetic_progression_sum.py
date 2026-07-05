from decimal import Decimal

def get_arithmetic_progression_sum_by_first_term_and_last_term_and_term_amount(
    *,
    first_term: Decimal,
    last_term: Decimal,
    term_amount: Decimal,
) -> Decimal:

    arithmetic_progression_sum: Decimal = ((first_term + last_term) * term_amount) / 2
    return arithmetic_progression_sum

def get_arithmetic_progression_sum_by_first_term_and_step_and_term_amount(
    *,
    first_term: Decimal,
    step: Decimal,
    term_amount: Decimal,
) -> Decimal:

    arithmetic_progression_sum: Decimal = ((2 * first_term + (term_amount - 1) * step) * term_amount) / 2
    return arithmetic_progression_sum

