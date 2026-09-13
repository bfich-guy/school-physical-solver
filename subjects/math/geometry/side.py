from decimal import Decimal
from math import prod


#region Triangle side

def get_triangle_adjacent_side_by_triangle_area_and_triangle_given_adjastend_side_and_angle_sinus(
    *,
    triangle_area: Decimal,
    triangle_given_adjastend_side: Decimal,
    angle_sinus: Decimal,
) -> Decimal:

    triangle_adjacent_side: Decimal = (Decimal("2") * triangle_area) / (triangle_given_adjastend_side * angle_sinus)
    return triangle_adjacent_side


def get_triangle_opposite_side_by_cosine_theorem(
    *,
    first_side: Decimal,
    second_side: Decimal,
    angle_cosinus: Decimal,
) -> Decimal:

    triangle_opposite_side: Decimal = ((first_side ** Decimal("2")) + (second_side ** Decimal("2")) - (Decimal("2") * first_side * second_side * angle_cosinus)).sqrt()
    return triangle_opposite_side


def get_triangle_side_by_triangle_area_and_triangle_given_sides_and_triangle_circumradius(
    *,
    triangle_area: Decimal,
    triangle_given_sides: list[Decimal],
    triangle_circumradius: Decimal,
) -> Decimal:

    triangle_side: Decimal = (triangle_area * Decimal("4") * triangle_circumradius) / Decimal(str(prod(triangle_given_sides)))
    return triangle_side

#endregion
