from decimal import decimal


#region Vectors

def get_vector_sum_by_vectors_coordinates(
    *,
    first_vector_coordinates_list: list[Decimal],
    second_vector_coordinates_list: list[Decimal],
) -> list[Decimal]

    vector_sum: list[Decimal] = []

    for first_vector_coordinate, second_vector_coordinate in zip(first_vector_coordinates_list, second_vector_coordinates_list):
        coordinates_sum: Decimal = first_vector_coordinate + second_vector_coordinate
        vector_sum.append(coordinates_sum)

    return vector_sum


def get_vector_magnitude_by_delta_coordinates_sum(
    *,
    delta_coordinates_list: list[Decimal],
) -> Decimal:

    squared_vector_magnitude: Decimal = Decimal("0")

    for delta_coordinate in delta_coordinates_list:
        squared_delta_coordinate: Decimal = delta_coordinate ** Decimal("2")
        vector_magnitude += squared_delta_coordinate

    vector_magnitude: Decimal = squared_vector_magnitude.sqrt()
    return vector_magnitude


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

#endregion
