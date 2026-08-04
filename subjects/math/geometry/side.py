from decimal import Decimal


#region Triangle side

def get_second_side_by_triangle_area_and_first_side_and_angle_sinus(
    *,
    triangle_area: Decimal,
    first_side: Decimal,
    angle_sinus: Decimal,
) -> Decimal:

    second_side: Decimal = (Decimal("2") * triangle_area) / (first_side * angle_sinus)
    return second_side


def get_third_side_by_cosine_theorem(
    *,
    first_side: Decimal,
    second_side: Decimal,
    angle_cosinus: Decimal,
) -> Decimal:

    triangle_third_side: Decimal = ((first_side ** Decimal("2")) + (second_side ** Decimal("2")) - (Decimal("2") * first_side * second_side * angle_cosinus)).sqrt()
    return triangle_third_side

#endregion


#region Parallelogram side

def get_second_side_by_parallelogram_area_and_first_side_and_angle_sinus(
    *,
    parallelogram_area: Decimal,
    first_side: Decimal,
    angle_sinus: Decimal,
) -> Decimal:

    second_side: Decimal = parallelogram_area / (first_side * angle_sinus)
    return second_side

#endregion
