from decimal import Decimal


#region Progression term

def get_arithmetic_progression_term_by_first_term_and_step_and_term_amount(
    *,
    first_term: Decimal,
    step: Decimal,
    term_amount: Decimal,
) -> Decimal:

    arithmetic_progression_term: Decimal = first_term + (step * (term_amount - Decimal("1")))
    return arithmetic_progression_term


def get_geometric_progression_term_by_first_term_and_ratio_and_term_amount(
    *,
    first_term: Decimal,
    ratio: Decimal,
    term_amount: Decimal,
) -> Decimal:

    geometric_progression_term: Decimal = first_term * (ratio ** (term_amount - Decimal("1")))
    return geometric_progression_term

#endregion
