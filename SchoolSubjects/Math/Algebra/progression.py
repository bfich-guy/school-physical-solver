from decimal import Decimal

#region Arithmetic progression

#region Sum

def get_arithmetic_progression_sum_by_first_term_and_last_term_and_term_amount(
    *,
    first_term: Decimal,
    last_term: Decimal,
    term_amount: Decimal,
) -> Decimal:

    arithmetic_progression_sum: Decimal = ((first_term + last_term) * term_amount) / Decimal("2")
    return arithmetic_progression_sum


def get_arithmetic_progression_sum_by_first_term_and_step_and_term_amount(
    *,
    first_term: Decimal,
    step: Decimal,
    term_amount: Decimal,
) -> Decimal:

    arithmetic_progression_sum: Decimal = ((Decimal("2") * first_term + (term_amount - Decimal("1")) * step) * term_amount) / Decimal("2")
    return arithmetic_progression_sum

#endregion


#region Term

def get_arithmetic_progression_term_by_first_term_and_step_and_term_amount(
    *,
    first_term: Decimal,
    step: Decimal,
    term_amount: Decimal,
) -> Decimal:

    arithmetic_progression_term: Decimal = first_term + (step * (term_amount - Decimal("1")))
    return arithmetic_progression_term

#endregion


#endregion


#region Geometric progression


#region Sum

def get_geometric_progression_sum_by_first_term_and_ratio_and_term_amount(
    *,
    first_term: Decimal,
    ratio: Decimal,
    term_amount: Decimal,
) -> Decimal:

    geometric_progression_sum: Decimal = (first_term * (pow(ratio, term_amount) - Decimal("1"))) / (ratio - Decimal("1"))
    return geometric_progression_sum

#endregion


#region Term

def get_geometric_progression_term_by_first_term_and_ratio_and_term_amount(
    *,
    first_term: Decimal,
    ratio: Decimal,
    term_amount: Decimal,
) -> Decimal:

    geometric_progression_term: Decimal = first_term * (ratio ** (term_amount - Decimal("1")))
    return geometric_progression_term

#endregion


#endregion
