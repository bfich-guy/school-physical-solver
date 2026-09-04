from decimal import Decimal


#region XY graphs coordinates

def get_linear_graph_x_coordinate(
    *,
    linear_graph_y_coordinate: Decimal,
    linear_graph_linear_coefficient: Decimal,
    linear_graph_constant_coefficient: Decimal,
) -> Decimal:

    linear_graph_x: Decimal = (linear_graph_y_coordinate - linear_graph_constant_coefficient) / linear_graph_linear_coefficient
    return linear_graph_x


def get_linear_graph_y_coordinate(
    *,
    linear_graph_linear_coefficient: Decimal,
    linear_graph_x_coordinate: Decimal,
    linear_graph_constant_coefficient: Decimal,
) -> Decimal:

    linear_graph_y_coordinate: Decimal = linear_graph_linear_coefficient * linear_graph_x_coordinate + linear_graph_constant_coefficient
    return linear_graph_y_coordinate


def get_quadratic_graph_x_coordinate(
    *,
    quadratic_graph_y_coordinate: Decimal,
    quadratic_graph_quadratic_coefficient: Decimal,
    quadratic_graph_linear_coefficient: Decimal,
    quadratic_graph_constant_coefficient: Decimal,
) -> list[Decimal]:

    discriminant: Decimal = quadratic_graph_linear_coefficient ** Decimal("2") - Decimal("4") * quadratic_graph_quadratic_coefficient * (quadratic_graph_constant_coefficient - quadratic_graph_y_coordinate)
    discriminant_square_root: Decimal = discriminant.sqrt()

    quadratic_graph_first_x_coordinate: Decimal = (-quadratic_graph_linear_coefficient - discriminant_square_root) / (Decimal("2") * quadratic_graph_quadratic_coefficient)
    quadratic_graph_second_x_coordinate: Decimal = (-quadratic_graph_linear_coefficient + discriminant_square_root) / (Decimal("2") * quadratic_graph_quadratic_coefficient)

    quadratic_graph_x_list: list[Decimal] = [quadratic_graph_first_x_coordinate, quadratic_graph_second_x_coordinate]
    return quadratic_graph_x_list


def get_quadratic_graph_y_coordinate(
    *,
    quadratic_graph_quadratic_coefficient: Decimal,
    quadratic_graph_linear_coefficient: Decimal,
    quadratic_graph_x_coordinate: Decimal,
    quadratic_graph_constant_coefficient: Decimal,
) -> Decimal:

    quadratic_graph_y_coordinate: Decimal = ((quadratic_graph_quadratic_coefficient * (quadratic_graph_x_coordinate ** Decimal("2"))) + (quadratic_graph_linear_coefficient * quadratic_graph_x_coordinate) + quadratic_graph_constant_coefficient)
    return quadratic_graph_y_coordinate

#endregion


#region Graphs intersection point coordinates

def get_linear_graphs_intersection_point_coordinates(
    *,
    first_graph_linear_coefficient: Decimal,
    first_graph_constant_term: Decimal,
    second_graph_linear_coefficient: Decimal,
    second_graph_constant_coefficient: Decimal,
) -> list[Decimal]:

    linear_coefficient_delta: Decimal = second_graph_linear_coefficient - first_graph_linear_coefficient
    constant_coefficient_delta: Decimal = second_graph_constant_coefficient - first_graph_constant_term

    linear_graphs_intersection_point_x: Decimal = -constant_coefficient_delta / linear_coefficient_delta
    linear_graphs_intersection_graph_y: Decimal = first_graph_linear_coefficient * linear_graphs_intersection_point_x + first_graph_constant_term

    linear_graphs_intersection_point_coordinates: list[Decimal] = [linear_graphs_intersection_point_x, linear_graphs_intersection_graph_y]
    return linear_graphs_intersection_point_coordinates


def get_quadratic_graphs_intersection_point_coordinates(
    *,
    first_quadratic_graph_quadratic_coefficient: Decimal,
    first_quadratic_graph_linear_coefficient: Decimal,
    first_quadratic_graph_constant_coefficient: Decimal,
    second_quadratic_graph_quadratic_coefficient: Decimal,
    second_quadratic_graph_linear_coefficient: Decimal,
    second_quadratic_graph_constant_coefficient: Decimal,
) -> list[list[Decimal]]:

    quadratic_coefficient_delta: Decimal = second_quadratic_graph_quadratic_coefficient - first_quadratic_graph_quadratic_coefficient
    linear_coefficient_delta: Decimal = second_quadratic_graph_linear_coefficient - first_quadratic_graph_linear_coefficient
    constant_coefficient_delta: Decimal = second_quadratic_graph_constant_coefficient - first_quadratic_graph_constant_coefficient

    discriminant: Decimal = (linear_coefficient_delta ** Decimal("2")) - Decimal("4") * quadratic_coefficient_delta * constant_coefficient_delta
    discriminant_square_root: Decimal = discriminant.sqrt()

    quadratic_graphs_first_intersection_point_x_coordinate: Decimal = (-linear_coefficient_delta - discriminant_square_root) / (Decimal("2") * quadratic_coefficient_delta)
    quadratic_graphs_second_intersection_point_x_coordinate: Decimal = (-linear_coefficient_delta + discriminant_square_root) / (Decimal("2") * quadratic_coefficient_delta)

    quadratic_graphs_first_intersection_point_y_coordinate: Decimal = first_quadratic_graph_quadratic_coefficient * (quadratic_graphs_first_intersection_point_x_coordinate ** Decimal("2")) + first_quadratic_graph_linear_coefficient * quadratic_graphs_first_intersection_point_x_coordinate + first_quadratic_graph_constant_coefficient
    quadratic_graphs_second_intersection_point_y_coordinate: Decimal = second_quadratic_graph_quadratic_coefficient * (quadratic_graphs_second_intersection_point_x_coordinate ** Decimal("2")) + second_quadratic_graph_linear_coefficient * quadratic_graphs_second_intersection_point_x_coordinate + second_quadratic_graph_constant_coefficient

    quadratic_graph_intersection_points_matrix_coordinates: list[list[Decimal]] = [[quadratic_graphs_first_intersection_point_x_coordinate, quadratic_graphs_first_intersection_point_y_coordinate], [quadratic_graphs_second_intersection_point_x_coordinate, quadratic_graphs_second_intersection_point_y_coordinate]]
    return quadratic_graph_intersection_points_matrix_coordinates

#endregion


#region Vector coordinate

def get_vector_coordinates_by_delta_coordinate(
    *,
    end_coordinates_list: list[Decimal],
    start_coordinates_list: list[Decimal],
) -> list[Decimal]:

    vector_coordinates: list[Decimal] = []

    for end_coordinate, start_coordinate in zip(end_coordinates_list, start_coordinates_list):
        delta_coordinate: Decimal = end_coordinate - start_coordinate
        vector_coordinates.append(delta_coordinate)

    return vector_coordinates

#endregion
