from decimal import Decimal

from subjects.math.algebra.functions import get_linear_graph_x_coordinate, get_quadratic_graph_x_coordinate


#region Linear equation

def solve_linear_equation(
    *,
    linear_equation_linear_coefficient: Decimal,
    linear_equation_constant_coefficient: Decimal,
) -> Decimal:

    linear_equation_root: Decimal = get_linear_graph_x_coordinate(
        linear_graph_y_coordinate=Decimal("0"),
        linear_graph_linear_coefficient=linear_equation_linear_coefficient,
        linear_graph_constant_coefficient=linear_equation_constant_coefficient,
    )

    return linear_equation_root

#endregion


#region Quadratic equation

def solve_quadratic_equation(
    *,
    quadraric_equation_quadratic_coefficient: Decimal,
    quadraric_equation_linear_coefficient: Decimal,
    quadraric_equation_constant_coefficient: Decimal,
) -> list[Decimal]:

    quadratic_equation_roots: list[Decimal] = get_quadratic_graph_x_coordinate(
        quadratic_graph_y_coordinate=Decimal("0"),
        quadratic_graph_quadratic_coefficient=quadraric_equation_quadratic_coefficient,
        quadratic_graph_linear_coefficient=quadraric_equation_linear_coefficient,
        quadratic_graph_constant_coefficient=quadraric_equation_constant_coefficient,
    )

    return quadratic_equation_roots

#endregion
