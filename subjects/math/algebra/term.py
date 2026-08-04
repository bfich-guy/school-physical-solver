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


#region Constant term

def get_linear_graph_constant_term(
    linear_graph_y: Decimal,
    linear_graph_linear_coefficient: Decimal,
    linear_graph_x: Decimal,
) -> Decimal:

    linear_graph_constant_term: Decimal = linear_graph_y - (linear_graph_linear_coefficient * linear_graph_x)
    return linear_graph_constant_term


def get_quadratic_graph_constant_term(
    *,
    quadratic_graph_y: Decimal,
    quadratic_graph_quadratic_coefficient: Decimal,
    quadratic_graph_linear_coefficient: Decimal,
    quadratic_graph_x: Decimal,
) -> Decimal:

    quadratic_graph_constant_term: Decimal = (quadratic_graph_y - (quadratic_graph_quadratic_coefficient * (quadratic_graph_x ** Decimal("2"))) - (quadratic_graph_linear_coefficient * quadratic_graph_x))
    return quadratic_graph_constant_term

#endregion
