from decimal import Decimal


#region Triangle area

def get_triangle_area_by_triangle_base_and_triangle_height(
    *,
    triangle_base: Decimal,
    triangle_height: Decimal,
) -> Decimal:

    triangle_area: Decimal = (triangle_base * triangle_height) / Decimal("2")
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

    triangle_semiperimeter: Decimal = (first_side + second_side + third_side) / Decimal("2")
    triangle_area: Decimal = (triangle_semiperimeter * (triangle_semiperimeter - first_side) * (triangle_semiperimeter - second_side) * (triangle_semiperimeter - third_side)).sqrt()
    return triangle_area

#endregion


#region Parallelogram area

def get_parallelogram_area_by_parallelogram_base_and_parallelogram_height(
    *,
    parallelogram_base: Decimal,
    parallelogram_height: Decimal,
) -> Decimal:

    parallelogram_area: Decimal = parallelogram_base * parallelogram_height
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
    parralelogram_diagonal: Decimal,
) -> Decimal:

    parallelogram_semiperimeter: Decimal = (first_side + second_side + parralelogram_diagonal) / Decimal("2")
    parallelogram_area: Decimal = 2 * (parallelogram_semiperimeter * (parallelogram_semiperimeter - first_side) * (parallelogram_semiperimeter - second_side) * (parallelogram_semiperimeter - parralelogram_diagonal)).sqrt()
    return parallelogram_area

#endregion


#region Circle area

def get_circle_area_by_circle_radius(
    *,
    pi: Decimal,
    circle_radius: Decimal,
) -> Decimal:

    circle_area: Decimal = pi * (circle_radius ** Decimal("2"))
    return circle_area

#endregion
