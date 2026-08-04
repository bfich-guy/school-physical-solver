from decimal import Decimal


#region Triangle base

def get_triangle_base_by_triangle_area_and_triangle_height(
    *,
    triangle_area: Decimal,
    triangle_height: Decimal,
) -> Decimal:

    triangle_base: Decimal = (Decimal("2") * triangle_area) / triangle_height
    return triangle_base

#endregion


#region Parallelogram base

def get_parallelogram_base_by_parallelogram_area_and_parallelogram_height(
    *,
    parallelogram_area: Decimal,
    parallelogram_height: Decimal,
) -> Decimal:

    parallelogram_base: Decimal = parallelogram_area / parallelogram_height
    return parallelogram_base

#endregion
