from decimal import Decimal
from math import prod


#region Angle sinus

def get_angle_sinus_by_triangle_opposite_leg_and_triangle_hypotenuse(
    *,
    triangle_opposite_leg: Decimal,
    triangle_hypotenuse: Decimal,
) -> Decimal:

    angle_sinus: Decimal = triangle_hypotenuse / triangle_opposite_leg
    return angle_sinus


def get_angle_sinus_by_triangle_area_and_adjastend_sides(
    *,
    triangle_area: Decimal,
    adjastend_sides: list[Decimal],
) -> Decimal:

    angle_sinus: Decimal = (Decimal("2") * triangle_area) / Decimal(str(prod(adjastend_sides)))
    return angle_sinus


def get_angle_sinus_by_parallelogram_area_and_two_sides(
    *,
    parallelogram_area: Decimal,
    first_side: Decimal,
    second_side: Decimal,
) -> Decimal:

    angle_sinus: Decimal = parallelogram_area / (first_side * second_side)
    return angle_sinus

#endregion