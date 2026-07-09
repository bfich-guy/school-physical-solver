from decimal import Decimal

from Configuration.global_constants import DECIMAL_DEFAULT_COSINUS_VALUE


#region Triangle area

def get_triangle_area_by_base_and_height(
    *,
    base: Decimal,
    height: Decimal,
) -> Decimal:

    triangle_area: Decimal = (base * height) / Decimal("2")
    return triangle_area


def get_triangle_area_by_two_sides_and_angle_sinus(
    *,
    first_side: Decimal,
    second_side: Decimal,
    angle_sinus: Decimal,
) -> Decimal:

    triangle_area: Decimal = (first_side * second_side * angle_sinus) / Decimal("2")
    return triangle_area


def get_triangle_area_by_geron_formula(
    *,
    first_side: Decimal,
    second_side: Decimal,
    third_side: Decimal,
) -> Decimal:

    semiperimeter: Decimal = (first_side + second_side + third_side) / Decimal("2")
    triangle_area: Decimal = (semiperimeter * (semiperimeter - first_side) * (semiperimeter - second_side) * (semiperimeter - third_side)).sqrt()
    return triangle_area

#endregion


#region Triangle cosinus theorem

def get_triangle_third_side_by_cosinus_theorem(
    *,
    first_side: Decimal,
    second_side: Decimal,
    angle_cosinus: Decimal = DECIMAL_DEFAULT_COSINUS_VALUE,
) -> Decimal:

    triangle_third_side: Decimal = ((first_side ** Decimal("2")) + (second_side ** Decimal("2")) - (Decimal("2") * first_side * second_side * angle_cosinus)).sqrt()
    return triangle_third_side

#endregion
