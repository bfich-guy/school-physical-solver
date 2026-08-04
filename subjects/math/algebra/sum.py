from decimal import Decimal


#region Progression sum

def get_arithmetic_progression_sum_by_first_term_and_last_term_and_term_amount(
    *,
    first_term: Decimal,
    last_term: Decimal,
    term_amount: Decimal,
) -> Decimal:

    arithmetic_progression_sum: Decimal = ((first_term + last_term) * term_amount) / Decimal("2")
    return arithmetic_progression_sum


def get_geometric_progression_sum_by_first_term_and_ratio_and_term_amount(
    *,
    first_term: Decimal,
    ratio: Decimal,
    term_amount: Decimal,
) -> Decimal:

    geometric_progression_sum: Decimal = (first_term * (pow(ratio, term_amount) - Decimal("1"))) / (ratio - Decimal("1"))
    return geometric_progression_sum

#endregion


#region Vector sum

def get_vector_sum_by_vectors_coordinates(
    *,
    first_vector_coordinates_list: list[Decimal],
    second_vector_coordinates_list: list[Decimal],
) -> list[Decimal]:

    vector_sum: list[Decimal] = []

    for first_vector_coordinate, second_vector_coordinate in zip(first_vector_coordinates_list, second_vector_coordinates_list):
        coordinates_sum: Decimal = first_vector_coordinate + second_vector_coordinate
        vector_sum.append(coordinates_sum)

    return vector_sum

#endregion
