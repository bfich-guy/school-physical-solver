from decimal import Decimal

from system.utils.calculators import decimal_logarithm


#region Equations

def get_linear_equation_root(
    *,
    linear_equation_linear_coefficient: Decimal,
    linear_equation_constant_coefficient: Decimal,
) -> Decimal:

    linear_equation_root: Decimal = -linear_equation_constant_coefficient / linear_equation_linear_coefficient
    return linear_equation_root


def get_quadratic_equation_roots(
    *,
    quadraric_equation_quadratic_coefficient: Decimal,
    quadraric_equation_linear_coefficient: Decimal,
    quadraric_equation_constant_coefficient: Decimal,
) -> list[Decimal]:

    discriminant: Decimal = pow(quadraric_equation_linear_coefficient, Decimal("2")) - (Decimal("4") * quadraric_equation_quadratic_coefficient * quadraric_equation_constant_coefficient)
    quadratic_equation_roots: list[Decimal] = [((-quadraric_equation_linear_coefficient - discriminant.sqrt()) / (Decimal("2") * quadraric_equation_quadratic_coefficient)), ((-quadraric_equation_linear_coefficient + discriminant.sqrt()) / (Decimal("2") * quadraric_equation_quadratic_coefficient))]
    return quadratic_equation_roots

#endregion


#region Functions

def get_quadratic_graph_y_coordinate(
    *,
    quadratic_graph_quadratic_coefficient: Decimal,
    quadratic_graph_linear_coefficient: Decimal,
    quadratic_graph_x_coordinate: Decimal,
    quadratic_graph_constant_coefficient: Decimal,
) -> Decimal:

    quadratic_graph_y_coordinate: Decimal = ((quadratic_graph_quadratic_coefficient * (quadratic_graph_x_coordinate ** Decimal("2"))) + (quadratic_graph_linear_coefficient * quadratic_graph_x_coordinate) + quadratic_graph_constant_coefficient)
    return quadratic_graph_y_coordinate


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


def get_quadratic_graph_constant_coefficient(
    *,
    quadratic_graph_y_coordinate: Decimal,
    quadratic_graph_quadratic_coefficient: Decimal,
    quadratic_graph_linear_coefficient: Decimal,
    quadratic_graph_x_coordinate: Decimal,
) -> Decimal:

    quadratic_graph_constant_coefficient: Decimal = (quadratic_graph_y_coordinate - (quadratic_graph_quadratic_coefficient * (quadratic_graph_x_coordinate ** Decimal("2"))) - (quadratic_graph_linear_coefficient * quadratic_graph_x_coordinate))
    return quadratic_graph_constant_coefficient


def get_linear_graph_y_coordinate(
    *,
    linear_graph_linear_coefficient: Decimal,
    linear_graph_x_coordinate: Decimal,
    linear_graph_constant_coefficient: Decimal,
) -> Decimal:

    linear_graph_y_coordinate: Decimal = linear_graph_linear_coefficient * linear_graph_x_coordinate + linear_graph_constant_coefficient
    return linear_graph_y_coordinate


def get_linear_graph_x_coordinate(
    *,
    linear_graph_y_coordinate: Decimal,
    linear_graph_linear_coefficient: Decimal,
    linear_graph_constant_coefficient: Decimal,
) -> Decimal:

    linear_graph_x: Decimal = (linear_graph_y_coordinate - linear_graph_constant_coefficient) / linear_graph_linear_coefficient
    return linear_graph_x


def get_linear_graph_linear_coefficient(
    *,
    linear_graph_y_coordinate: Decimal,
    linear_graph_constant_coefficient: Decimal,
    linear_graph_x_coordinate: Decimal,
) -> Decimal:

    linear_graph_linear_coefficient: Decimal = (linear_graph_y_coordinate - linear_graph_constant_coefficient) / linear_graph_x_coordinate
    return linear_graph_linear_coefficient


def get_linear_graph_constant_coefficient(
    linear_graph_y_coordinate: Decimal,
    linear_graph_linear_coefficient: Decimal,
    linear_graph_x_coordinate: Decimal,
) -> Decimal:

    linear_graph_constant_coefficient: Decimal = linear_graph_y_coordinate - (linear_graph_linear_coefficient * linear_graph_x_coordinate)
    return linear_graph_constant_coefficient


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


#region Mean

def get_arithmetic_mean_by_numbers_sum_and_numbers_amount(
    *,
    numbers_sum: Decimal, 
    numbers_amount: Decimal
) -> Decimal:

    arithmetic_mean: Decimal = numbers_sum / numbers_amount
    return arithmetic_mean


def get_geometric_mean_by_numbers_product_and_numbers_amount(
    *,
    numbers_product: Decimal,
    numbers_amount: Decimal,
) -> Decimal:

    geometric_mean: Decimal = pow(numbers_product, (Decimal("1") / numbers_amount))
    return geometric_mean

#endregion


#region Progressions

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


def get_arithmetic_progression_step_by_arithmetic_progression_last_term_arithmetic_progression_first_term_and_arithmetic_progression_terms_amount(
    *,
    arithmetic_progression_last_term: Decimal,
    arithmetic_progression_first_term: Decimal,
    arithmetic_progression_terms_amount: Decimal,
) -> Decimal:

    arithmetic_progression_step: Decimal = (arithmetic_progression_last_term - arithmetic_progression_first_term) / (arithmetic_progression_terms_amount - Decimal("1"))
    return arithmetic_progression_step


def get_arithmetic_progression_terms_amount_by_arithmetic_progression_sum_and_arithmetic_progression_last_term_and_arithmetic_progression_last_term(
    *,
    arithmetic_progression_sum: Decimal,
    arithmetic_progression_first_term: Decimal,
    arithmetic_progression_last_term: Decimal,
) -> Decimal:

    arithmetic_progression_terms_amount: Decimal = (Decimal("2") * arithmetic_progression_sum) / (arithmetic_progression_first_term + arithmetic_progression_last_term)
    return arithmetic_progression_terms_amount


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


def get_geometric_progression_ratio_by_geometric_progression_last_term_and_geometric_progression_first_term_and_geometric_progression_terms_amount(
    *,
    geometric_progression_last_term: Decimal,
    geometric_progression_first_term: Decimal,
    geometric_progression_terms_amount: Decimal,
) -> Decimal:

    geometric_progression_ratio: Decimal = pow((geometric_progression_last_term / geometric_progression_first_term), (Decimal("1") / (geometric_progression_terms_amount - Decimal("1"))))
    return geometric_progression_ratio


def get_geometric_progression_terms_amount_by_geometric_progression_first_term_and_geometric_progression_last_term_and_geometric_progression_ratio(
    *,
    geometric_progression_first_term: Decimal,
    geometric_progression_last_term: Decimal,
    geometric_progression_ratio: Decimal,
) -> Decimal:

    geometric_progression_terms_amount: Decimal = decimal_logarithm((geometric_progression_last_term / geometric_progression_first_term), geometric_progression_ratio) + Decimal("1")
    return geometric_progression_terms_amount

#endregion


#region Vectors

def get_vector_coordinates_by_delta_scalar_coordinates(
    *,
    end_coordinates_list: list[Decimal],
    start_coordinates_list: list[Decimal],
) -> list[Decimal]:

    vector_coordinates: list[Decimal] = [end_coordinate - start_coordinate for end_coordinate, start_coordinate in zip(end_coordinates_list, start_coordinates_list)]
    return vector_coordinates


def get_vectors_sum_by_vectors_coordinates(
    *,
    first_vector_coordinates_list: list[Decimal],
    second_vector_coordinates_list: list[Decimal],
) -> list[Decimal]:

    vectors_sum: list[Decimal] = [first_vector_coordinate + second_vector_coordinate for first_vector_coordinate, second_vector_coordinate in zip(first_vector_coordinates_list, second_vector_coordinates_list)]
    return vectors_sum


def get_vectors_difference_by_vectors_coordinates(
    *,
    first_vector_coordinates_list: list[Decimal],
    second_vector_coordinates_list: list[Decimal],
) -> list[Decimal]:

    vectors_difference: list[Decimal] = [first_vector_coordinate - second_vector_coordinate for first_vector_coordinate, second_vector_coordinate in zip(first_vector_coordinates_list, second_vector_coordinates_list)]
    return vectors_difference


def get_vectors_dot_product_by_vectors_coordinates(
    *,
    first_vector_coordinates: list[Decimal],
    second_vector_coordinates: list[Decimal],
) -> Decimal:

    vectors_dot_product: Decimal = Decimal(sum(first_vector_coordinate * second_vector_coordinate for first_vector_coordinate, second_vector_coordinate in zip(first_vector_coordinates, second_vector_coordinates)))
    return vectors_dot_product


def get_vectors_dot_product_by_vectors_magnitudes_and_angle_cosinus(
    *,
    first_vector_magnitude: Decimal,
    second_vector_magnitude: Decimal,
    angle_cosinus: Decimal,
) -> Decimal:

    vectors_dot_product: Decimal = first_vector_magnitude * second_vector_magnitude * angle_cosinus
    return vectors_dot_product


def get_scaled_vector_by_vectors_coordinates_and_scalar_coefficient(
    *,
    vectors_coordinates: list[Decimal],
    scalar_coefficient: Decimal,
) -> list[Decimal]:

    scaled_vector: list[Decimal] = [vector_coordinate * scalar_coefficient for vector_coordinate in vectors_coordinates]
    return scaled_vector


def get_vector_magnitude_by_vector_coordinates(
    *,
    vector_coordinates: list[Decimal],
) -> Decimal:

    vector_magnitude: Decimal = Decimal(sum(pow(delta_coordinate, Decimal("2")) for delta_coordinate in vector_coordinates)).sqrt()
    return vector_magnitude


def get_vector_magnitude_by_vector_dot_product_and_given_vector_magnitudes_and_angle_cosinus(
    *,
    vector_dot_product: Decimal,
    given_vector_magnitude: Decimal,
    angle_cosinus: Decimal,
) -> Decimal:

    vector_magnitude: Decimal = vector_dot_product / (given_vector_magnitude * angle_cosinus)
    return vector_magnitude


def get_angle_cosinus_by_vector_dot_product_and_vectors_magnitudes(
    *,
    vector_dot_product: Decimal,
    first_vector_magnitude: Decimal,
    second_vector_magnitude: Decimal,
) -> Decimal:

    angle_cosinus: Decimal = vector_dot_product / (first_vector_magnitude * second_vector_magnitude)
    return angle_cosinus

#endregion
