from decimal import Decimal


#region Trapezoidal figure area (triangle, parallelogram, trapezoid)

def get_trapezoidal_figure_area_by_trapezoidal_figure_base_and_trapezoidal_figure_height(
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

    semiperimeter: Decimal =  (first_side + second_side + third_side) / Decimal("2")
    triangle_area: Decimal = (semiperimeter * (semiperimeter - first_side) * (semiperimeter - second_side) * (semiperimeter - third_side)).sqrt()
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
