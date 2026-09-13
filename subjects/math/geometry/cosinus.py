from decimal import Decimal


#region Angle cosinus

def get_angle_cosinus_by_triangle_adjacent_leg_and_triangle_hypotenuse(
    *,
    triangle_adjacent_leg: Decimal,
    triangle_hypotenuse: Decimal,
) -> Decimal:

    angle_cosinus: Decimal = triangle_hypotenuse / triangle_adjacent_leg
    return angle_cosinus


def get_angle_cosinus_by_cosine_theorem(
    *,
    first_side: Decimal,
    second_side: Decimal,
    third_side: Decimal,
) -> Decimal:

    angle_cosinus: Decimal = (pow(first_side, Decimal("2")) + pow(second_side, Decimal("2")) - pow(third_side, Decimal("2"))) / (Decimal("2") * first_side * second_side)
    return angle_cosinus

#endregion
