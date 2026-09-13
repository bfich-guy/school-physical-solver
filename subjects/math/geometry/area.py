from decimal import Decimal
from math import prod


#region Trapezoidal figure area (triangle, parallelogram, trapezoid)

def get_trapezoidal_figure_area_by_trapezoidal_figure_bases_and_trapezoidal_figure_height(
    *,
    trapezoidal_figure_upper_base: Decimal,
    trapezoidal_figure_lower_base: Decimal,
    trapezoidal_figure_height: Decimal,
) -> Decimal:

    trapezoidal_figure_area: Decimal = ((trapezoidal_figure_upper_base + trapezoidal_figure_lower_base) / Decimal("2")) * trapezoidal_figure_height
    return trapezoidal_figure_area

#endregion


#region Triangle area

def get_triangle_area_by_heron_formula(
    *,
    first_side: Decimal,
    second_side: Decimal,
    third_side: Decimal,
) -> Decimal:

    semiperimeter: Decimal = (first_side + second_side + third_side) / Decimal("2")
    triangle_area: Decimal = (semiperimeter * (semiperimeter - first_side) * (semiperimeter - second_side) * (semiperimeter - third_side)).sqrt()
    return triangle_area


def get_triangle_area_by_adjastend_sides_and_angle_sinus(
    *,
    adjastend_sides: list[Decimal],
    angle_sinus: Decimal,
) -> Decimal:

    triangle_area: Decimal = (Decimal(str(prod(adjastend_sides))) * angle_sinus) / Decimal("2")
    return triangle_area


def get_triangle_area_by_triangle_perimeter_and_triangle_inradius(
    *,
    triangle_perimeter: Decimal,
    triangle_inradius: Decimal,
) -> Decimal:

    triangle_area: Decimal = (triangle_perimeter * triangle_inradius) / Decimal("2")
    return triangle_area


def get_triangle_area_by_triangle_sides_and_triangle_circumradius(
    *,
    triangle_sides: list[Decimal],
    triangle_circumradius: Decimal,
) -> Decimal:

    triangle_area: Decimal = Decimal(str(prod(triangle_sides))) / (Decimal("4") * triangle_circumradius)
    return triangle_area

#endregion


#region Circle area

def get_circle_area_by_circle_radius(
    *,
    pi: Decimal,
    circle_radius: Decimal,
) -> Decimal:

    circle_area: Decimal = pi * pow(circle_radius, Decimal("2"))
    return circle_area

#endregion
