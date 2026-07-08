from decimal import Decimal


#region Parallelogram area

def get_parallelogram_area_by_base_and_height(
    *,
    base: Decimal,
    height: Decimal,
) -> Decimal:

    parallelogram_area: Decimal = base * height
    return parallelogram_area


def get_parallelogram_area_by_two_sides_and_angle_sinus(
    *,
    first_side: Decimal,
    second_side: Decimal,
    angle_sinus: Decimal,
) -> Decimal:

    parallelogram_area: Decimal = first_side * second_side * angle_sinus
    return parallelogram_area


def get_parallelogram_area_by_geron_formula(
    *,
    first_side: Decimal,
    second_side: Decimal,
    diagonal: Decimal,
) -> Decimal:

    semiperimeter: Decimal = (first_side + second_side + diagonal) / Decimal("2")
    parallelogram_area: Decimal = 2 * (semiperimeter * (semiperimeter - first_side) * (semiperimeter - second_side) * (semiperimeter - diagonal)).sqrt()
    return parallelogram_area

#endregion
