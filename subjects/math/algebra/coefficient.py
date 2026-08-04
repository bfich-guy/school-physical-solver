from decimal import Decimal


#region Linear coefficient

def get_linear_graph_linear_coefficient(
    *,
    linear_graph_y: Decimal,
    linear_graph_constant_term: Decimal,
    linear_graph_x: Decimal,
) -> Decimal:

    linear_graph_linear_coefficient: Decimal = (linear_graph_y - linear_graph_constant_term) / linear_graph_x
    return linear_graph_linear_coefficient

#endregion


#region Quadratic coefficient

def get_quadratic_graph_quadratic_coefficient(
    *,
    quadratic_graph_y: Decimal,
    quadratic_graph_linear_coefficient: Decimal,
    quadratic_graph_x: Decimal,
    quadratic_graph_constant_term: Decimal,
) -> Decimal:

    quadratic_graph_quadratic_coefficient: Decimal = (quadratic_graph_y - (quadratic_graph_linear_coefficient * quadratic_graph_x) - quadratic_graph_constant_term) / (quadratic_graph_x ** Decimal("2"))
    return quadratic_graph_quadratic_coefficient


def get_quadratic_graph_linear_coefficient(
    *,
    quadratic_graph_y: Decimal,
    quadratic_graph_quadratic_coefficient: Decimal,
    quadratic_graph_x: Decimal,
    quadratic_graph_constant_term: Decimal,
) -> Decimal:

    quadratic_graph_linear_coefficient: Decimal = (quadratic_graph_y - (quadratic_graph_quadratic_coefficient * (quadratic_graph_x ** Decimal("2"))) - quadratic_graph_constant_term) / quadratic_graph_x
    return quadratic_graph_linear_coefficient

#endregion
