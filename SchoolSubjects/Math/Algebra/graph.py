from decimal import Decimal


#region Linear graphics

def get_intersection_point_of_two_linear_graphs(
    *,
    first_point_linear_coefficient: Decimal,
    first_point_constant_term: Decimal,
    second_point_linear_coefficient: Decimal,
    second_point_constant_term: Decimal,
) -> list[Decimal]:

    linear_coefficient_delta: Decimal = second_point_linear_coefficient - first_point_linear_coefficient
    constant_term_delta: Decimal = second_point_constant_term - first_point_constant_term

    intersection_point_x: Decimal = -constant_term_delta / linear_coefficient_delta
    intersection_point_y: Decimal = first_point_linear_coefficient * intersection_point_x + first_point_constant_term

    intersection_point_coordinates: list[Decimal] = [intersection_point_x, intersection_point_y]
    return intersection_point_coordinates

#endregion
