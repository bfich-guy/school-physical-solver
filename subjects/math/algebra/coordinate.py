from decimal import Decimal


#region XY graphs coordinates

def get_linear_graph_x(
    *,
    linear_graph_y: Decimal,
    linear_graph_linear_coefficient: Decimal,
    linear_graph_constant_term: Decimal,
) -> Decimal:

    linear_graph_x: Decimal = (linear_graph_y - linear_graph_constant_term) / linear_graph_linear_coefficient
    return linear_graph_x


def get_linear_graph_y(
    *,
    linear_graph_linear_coefficient: Decimal,
    linear_graph_x: Decimal,
    linear_graph_constant_term: Decimal,
) -> Decimal:

    linear_graph_y: Decimal = linear_graph_linear_coefficient * linear_graph_x + linear_graph_constant_term
    return linear_graph_y


def get_quadratic_graph_x(
    *,
    quadratic_graph_y: Decimal,
    quadratic_graph_quadratic_coefficient: Decimal,
    quadratic_graph_linear_coefficient: Decimal,
    quadratic_graph_constant_term: Decimal,
) -> list[Decimal]:

    discriminant: Decimal = quadratic_graph_linear_coefficient ** Decimal("2") - Decimal("4") * quadratic_graph_quadratic_coefficient * (quadratic_graph_constant_term - quadratic_graph_y)
    discriminant_square_root: Decimal = discriminant.sqrt()

    quadratic_graph_first_x: Decimal = (-quadratic_graph_linear_coefficient - discriminant_square_root) / (Decimal("2") * quadratic_graph_quadratic_coefficient)
    quadratic_graph_second_x: Decimal = (-quadratic_graph_linear_coefficient + discriminant_square_root) / (Decimal("2") * quadratic_graph_quadratic_coefficient)

    quadratic_graph_x_list: list[Decimal] = [quadratic_graph_first_x, quadratic_graph_second_x]
    return quadratic_graph_x_list


def get_quadratic_graph_y(
    *,
    quadratic_graph_quadratic_coefficient: Decimal,
    quadratic_graph_linear_coefficient: Decimal,
    quadratic_graph_x: Decimal,
    quadratic_graph_constant_term: Decimal,
) -> Decimal:

    quadratic_graph_y: Decimal = ((quadratic_graph_quadratic_coefficient * (quadratic_graph_x ** Decimal("2"))) + (quadratic_graph_linear_coefficient * quadratic_graph_x) + quadratic_graph_constant_term)
    return quadratic_graph_y

#endregion


#region Graphs intersection point coordinates

def get_linear_graphs_intersection_point_coordinates(
    *,
    first_graph_linear_coefficient: Decimal,
    first_graph_constant_term: Decimal,
    second_graph_linear_coefficient: Decimal,
    second_graph_constant_term: Decimal,
) -> list[Decimal]:

    linear_coefficient_delta: Decimal = second_graph_linear_coefficient - first_graph_linear_coefficient
    constant_term_delta: Decimal = second_graph_constant_term - first_graph_constant_term

    linear_graphs_intersection_point_x: Decimal = -constant_term_delta / linear_coefficient_delta
    linear_graphs_intersection_graph_y: Decimal = first_graph_linear_coefficient * linear_graphs_intersection_point_x + first_graph_constant_term

    linear_graphs_intersection_point_coordinates: list[Decimal] = [linear_graphs_intersection_point_x, linear_graphs_intersection_graph_y]
    return linear_graphs_intersection_point_coordinates


def get_quadratic_graphs_intersection_point_coordinates(
    *,
    first_quadratic_graph_quadratic_coefficient: Decimal,
    first_quadratic_graph_linear_coefficient: Decimal,
    first_quadratic_graph_constant_term: Decimal,
    second_quadratic_graph_quadratic_coefficient: Decimal,
    second_quadratic_graph_linear_coefficient: Decimal,
    second_quadratic_graph_constant_term: Decimal,
) -> list[list[Decimal]]:

    quadratic_coefficient_delta: Decimal = second_quadratic_graph_quadratic_coefficient - first_quadratic_graph_quadratic_coefficient
    linear_coefficient_delta: Decimal = second_quadratic_graph_linear_coefficient - first_quadratic_graph_linear_coefficient
    constant_term_delta: Decimal = second_quadratic_graph_constant_term - first_quadratic_graph_constant_term

    discriminant: Decimal = (linear_coefficient_delta ** Decimal("2")) - Decimal("4") * quadratic_coefficient_delta * constant_term_delta
    discriminant_square_root: Decimal = discriminant.sqrt()

    quadratic_graphs_first_intersection_point_x: Decimal = (-linear_coefficient_delta - discriminant_square_root) / (Decimal("2") * quadratic_coefficient_delta)
    quadratic_graphs_second_intersection_point_x: Decimal = (-linear_coefficient_delta + discriminant_square_root) / (Decimal("2") * quadratic_coefficient_delta)

    quadratic_graphs_first_intersection_point_y: Decimal = first_quadratic_graph_quadratic_coefficient * (quadratic_graphs_first_intersection_point_x ** Decimal("2")) + first_quadratic_graph_linear_coefficient * quadratic_graphs_first_intersection_point_x + first_quadratic_graph_constant_term
    quadratic_graphs_second_intersection_point_y: Decimal = second_quadratic_graph_quadratic_coefficient * (quadratic_graphs_second_intersection_point_x ** Decimal("2")) + second_quadratic_graph_linear_coefficient * quadratic_graphs_second_intersection_point_x + second_quadratic_graph_constant_term

    quadratic_graph_intersection_points_matrix_coordinates: list[list[Decimal]] = [[quadratic_graphs_first_intersection_point_x, quadratic_graphs_first_intersection_point_y], [quadratic_graphs_second_intersection_point_x, quadratic_graphs_second_intersection_point_y]]
    return quadratic_graph_intersection_points_matrix_coordinates

#endregion
