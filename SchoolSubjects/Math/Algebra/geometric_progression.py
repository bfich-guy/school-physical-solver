from decimal import Decimal


#region Geometric progression sum

def get_geometric_progression_sum_by_first_term_and_ratio_and_term_amount(
    *,
    first_term: Decimal,
    ratio: Decimal,
    term_amount: Decimal,
) -> Decimal:

    geometric_progression_sum: Decimal = (first_term * (pow(ratio, term_amount) - 1)) / (ratio - 1)
    return geometric_progression_sum

#endregion


#region Geometric progression term

def get_geometric_progression_term_by_first_term_and_ratio_and_term_amount(
    *,
    first_term: Decimal,
    ratio: Decimal,
    term_amount: Decimal,
) -> Decimal:

    geometric_progression_term: Decimal = first_term * (ratio ** (term_amount - 1))
    return geometric_progression_term

#endregion
