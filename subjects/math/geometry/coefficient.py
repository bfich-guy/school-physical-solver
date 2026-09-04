from decimal import Decimal


#region Similarity coefficient

def get_similarity_coefficient_by_general_sides(
    *,
    first_side: Decimal,
    second_side: Decimal,
) -> Decimal:

    similarity_coefficient: Decimal = first_side / second_side
    return similarity_coefficient


def get_similarity_coefficient_by_general_areas(
    *,
    first_general_area: Decimal,
    second_general_area: Decimal,
) -> Decimal:

    similarity_coefficient: Decimal = (first_general_area / second_general_area).sqrt()
    return similarity_coefficient

#endregion
