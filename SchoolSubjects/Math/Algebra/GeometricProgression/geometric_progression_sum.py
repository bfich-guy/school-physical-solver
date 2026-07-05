from decimal import Decimal

def get_geometric_progression_sum_by_first_term_and_ratio_and_term_amount(
    *,
    first_term: Decimal,
    ratio: Decimal,
    term_amount: Decimal,
) -> Decimal:

    geometric_progression_sum: Decimal = (first_term * (pow(ratio, term_amount) - 1)) / (ratio - 1)
    return geometric_progression_sum

