from decimal import Decimal


#region Vector dot product

def get_vector_dot_product_by_vectors_coordinates(
    *,
    first_vector_coordinates_list: list[Decimal],
    second_vector_coordinates_list: list[Decimal],
) -> Decimal:

    vector_dot_product: Decimal = Decimal("0")

    for first_vector_coordinate, second_vector_coordinate in zip(first_vector_coordinates_list, second_vector_coordinates_list):
        coordinates_sum: Decimal = first_vector_coordinate * second_vector_coordinate
        vector_dot_product += coordinates_sum

    return vector_dot_product


def get_vector_dot_product_by_vectors_magnitudes_and_angle_cosinus(
    *,
    first_vector_magnitude: Decimal,
    second_vector_magnitude: Decimal,
    angle_cosinus: Decimal,
) -> Decimal:

    vector_dot_product: Decimal = first_vector_magnitude * second_vector_magnitude * angle_cosinus
    return vector_dot_product

#endregion
