from decimal import Decimal


#region Trapezoidal figure base (triangle, parallelogram, trapezoid)

def get_trapezoidal_figure_height_by_trapezoidal_figure_area_and_trapezoidal_figure_upper_base_and_trapezoidal_figure_lower_base(
    *,
    trapezoidal_figure_area: Decimal,
    trapezoidal_figure_upper_base: Decimal,
    trapezoidal_figure_lower_base: Decimal,
) -> Decimal:

    trapezoidal_figure_height: Decimal = (Decimal("2") * trapezoidal_figure_area) / (trapezoidal_figure_upper_base + trapezoidal_figure_lower_base)
    return trapezoidal_figure_height

#endregion
