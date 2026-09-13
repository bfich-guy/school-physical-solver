from decimal import Decimal


#region Vector coordinates

def get_vector_coordinates_by_delta_scalar_coordinates(
    *,
    end_coordinates_list: list[Decimal],
    start_coordinates_list: list[Decimal],
) -> list[Decimal]:

    vector_coordinates: list[Decimal] = [end_coordinate - start_coordinate for end_coordinate, start_coordinate in zip(end_coordinates_list, start_coordinates_list)]
    return vector_coordinates

#endregion


#region Vectors sum

def get_vectors_sum_by_vectors_coordinates(
    *,
    first_vector_coordinates_list: list[Decimal],
    second_vector_coordinates_list: list[Decimal],
) -> list[Decimal]:

    vectors_sum: list[Decimal] = [first_vector_coordinate + second_vector_coordinate for first_vector_coordinate, second_vector_coordinate in zip(first_vector_coordinates_list, second_vector_coordinates_list)]
    return vectors_sum

#endregion


#region Vectors dot product

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

#endregion


#region Scaled vector

def get_scaled_vector_by_vectors_coordinates_and_scalar_coefficient(
    *,
    vectors_coordinates: list[Decimal],
    scalar_coefficient: Decimal,
) -> list[Decimal]:

    scaled_vector: list[Decimal] = [vector_coordinate * scalar_coefficient for vector_coordinate in vectors_coordinates]
    return scaled_vector

#endregion


#region Vector magnitude

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

#endregion


#region Vector angles

def get_angle_cosinus_by_vector_dot_product_and_vectors_magnitudes(
    *,
    vector_dot_product: Decimal,
    first_vector_magnitude: Decimal,
    second_vector_magnitude: Decimal,
) -> Decimal:

    angle_cosinus: Decimal = vector_dot_product / (first_vector_magnitude * second_vector_magnitude)
    return angle_cosinus

#endregion
