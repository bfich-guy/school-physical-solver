from decimal import Decimal


#region Trapezoidal figure base (triangle, parallelogram, trapezoid)

def get_trapezoidal_figure_base_by_trapezoidal_figure_area_and_trapezoidal_figure_given_base_and_trapezoidal_figure_height(
    *,
    trapezoidal_figure_area: Decimal,
    trapezoidal_figure_given_base: Decimal,
    trapezoidal_figure_height: Decimal,
) -> Decimal:

    trapezoidal_figure_base: Decimal = ((Decimal("2") * trapezoidal_figure_area) / trapezoidal_figure_height) - trapezoidal_figure_given_base
    return trapezoidal_figure_base
    
#endregion
