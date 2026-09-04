from decimal import Decimal


#region Quadratic coefficient

def get_quadratic_graph_quadratic_coefficient(
    *,
    quadratic_graph_y_coordinate: Decimal,
    quadratic_graph_linear_coefficient: Decimal,
    quadratic_graph_x_coordinate: Decimal,
    quadratic_graph_constant_coefficient: Decimal,
) -> Decimal:

    quadratic_graph_quadratic_coefficient: Decimal = (quadratic_graph_y_coordinate - (quadratic_graph_linear_coefficient * quadratic_graph_x_coordinate) - quadratic_graph_constant_coefficient) / (quadratic_graph_x_coordinate ** Decimal("2"))
    return quadratic_graph_quadratic_coefficient


def get_quadratic_graph_linear_coefficient(
    *,
    quadratic_graph_y_coordinate: Decimal,
    quadratic_graph_quadratic_coefficient: Decimal,
    quadratic_graph_x_coordinate: Decimal,
    quadratic_graph_constant_coefficient: Decimal,
) -> Decimal:

    quadratic_graph_linear_coefficient: Decimal = (quadratic_graph_y_coordinate - (quadratic_graph_quadratic_coefficient * (quadratic_graph_x_coordinate ** Decimal("2"))) - quadratic_graph_constant_coefficient) / quadratic_graph_x_coordinate
    return quadratic_graph_linear_coefficient

#endregion


#region Linear coefficient

def get_linear_graph_linear_coefficient(
    *,
    linear_graph_y_coordinate: Decimal,
    linear_graph_constant_coefficient: Decimal,
    linear_graph_x_coordinate: Decimal,
) -> Decimal:

    linear_graph_linear_coefficient: Decimal = (linear_graph_y_coordinate - linear_graph_constant_coefficient) / linear_graph_x_coordinate
    return linear_graph_linear_coefficient

#endregion


#region Constant coefficient

def get_linear_graph_constant_coefficient(
    linear_graph_y_coordinate: Decimal,
    linear_graph_linear_coefficient: Decimal,
    linear_graph_x_coordinate: Decimal,
) -> Decimal:

    linear_graph_constant_coefficient: Decimal = linear_graph_y_coordinate - (linear_graph_linear_coefficient * linear_graph_x_coordinate)
    return linear_graph_constant_coefficient


def get_quadratic_graph_constant_coefficient(
    *,
    quadratic_graph_y_coordinate: Decimal,
    quadratic_graph_quadratic_coefficient: Decimal,
    quadratic_graph_linear_coefficient: Decimal,
    quadratic_graph_x_coordinate: Decimal,
) -> Decimal:

    quadratic_graph_constant_coefficient: Decimal = (quadratic_graph_y_coordinate - (quadratic_graph_quadratic_coefficient * (quadratic_graph_x_coordinate ** Decimal("2"))) - (quadratic_graph_linear_coefficient * quadratic_graph_x_coordinate))
    return quadratic_graph_constant_coefficient

#endregion
