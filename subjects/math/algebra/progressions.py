from decimal import Decimal
from math import log


#region Arithmetic progression

def get_arithmetic_progression_sum_by_arithmetic_progression_first_term_and_arithmetic_progression_last_term_and_arithmetic_progression_terms_amount(
    *,
    arithmetic_progression_first_term: Decimal,
    arithmetic_progression_last_term: Decimal,
    arithmetic_progression_terms_amount: Decimal,
) -> Decimal:

    arithmetic_progression_sum: Decimal = ((arithmetic_progression_first_term + arithmetic_progression_last_term) * arithmetic_progression_terms_amount) / Decimal("2")
    return arithmetic_progression_sum


def get_arithmetic_progression_term_by_arithmetic_progression_first_term_and_arithmetic_progression_step_and_arithmetic_progression_terms_amount(
    *,
    arithmetic_progression_first_term: Decimal,
    arithmetic_progression_step: Decimal,
    arithmetic_progression_terms_amount: Decimal,
) -> Decimal:

    arithmetic_progression_term: Decimal = arithmetic_progression_first_term + (arithmetic_progression_step * (arithmetic_progression_terms_amount - Decimal("1")))
    return arithmetic_progression_term


def get_arithmetic_progression_terms_amount_by_arithmetic_progression_sum_and_arithmetic_progression_last_term_and_arithmetic_progression_last_term(
    *,
    arithmetic_progression_sum: Decimal,
    arithmetic_progression_first_term: Decimal,
    arithmetic_progression_last_term: Decimal,
) -> Decimal:

    arithmetic_progression_terms_amount: Decimal = (Decimal("2") * arithmetic_progression_sum) / (arithmetic_progression_first_term + arithmetic_progression_last_term)
    return arithmetic_progression_terms_amount

#endregion


#region Geometry progressions

def get_geometric_progression_sum_by_geometric_progression_first_term_and_geometric_progression_ratio_and_geometric_progression_terms_amount(
    *,
    geometric_progression_first_term: Decimal,
    geometric_progression_ratio: Decimal,
    geometric_progression_terms_amount: Decimal,
) -> Decimal:

    geometric_progression_sum: Decimal = (geometric_progression_first_term * (pow(geometric_progression_ratio, geometric_progression_terms_amount) - Decimal("1"))) / (geometric_progression_ratio - Decimal("1"))
    return geometric_progression_sum


def get_geometric_progression_term_by_geometric_progression_first_term_and_geometric_progression_ratio_and_geometric_progression_terms_amount(
    *,
    geometric_progression_first_term: Decimal,
    geometric_progression_ratio: Decimal,
    geometric_progression_terms_amount: Decimal,
) -> Decimal:

    geometric_progression_term: Decimal = geometric_progression_first_term * (geometric_progression_ratio ** (geometric_progression_terms_amount - Decimal("1")))
    return geometric_progression_term


def get_geometric_progression_terms_amount_by_geometric_progression_first_term_and_geometric_progression_last_term_and_geometric_progression_ratio(
    *,
    geometric_progression_first_term: Decimal,
    geometric_progression_last_term: Decimal,
    geometric_progression_ratio: Decimal,
) -> Decimal:

    geometric_progression_terms_amount: Decimal = Decimal(str(log((geometric_progression_last_term / geometric_progression_first_term), geometric_progression_ratio))) + Decimal("1")
    return geometric_progression_terms_amount

#endregion
