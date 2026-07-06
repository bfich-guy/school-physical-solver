from decimal import Decimal

def get_triangle_area_by_base_and_height(
    *,
    base: Decimal,
    height: Decimal,
) -> Decimal:

    triangle_area: Decimal = (base * height) / 2
    return triangle_area

def get_triangle_area_by_two_sides_and_angle_sinus(
    *,
    first_side: Decimal,
    second_side: Decimal,
    angle_sinus: Decimal,
) -> Decimal:

    triangle_area: Decimal = (first_side * second_side * angle_sinus) / 2
    return triangle_area

def get_triangle_area_by_geron_formula(
    *,
    first_side: Decimal,
    second_side: Decimal,
    third_side: Decimal,
) -> Decimal:

    semiperimeter: Decimal = (first_side + second_side + third_side) / 2
    triangle_area: Decimal = (semiperimeter * (semiperimeter - first_side) * (semiperimeter - second_side) * (semiperimeter - third_side)).sqrt()
    return triangle_area

