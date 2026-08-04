from decimal import Decimal


#region Triangle height

def get_triangle_height_by_triangle_area_and_triangle_base(
    *,
    triangle_area: Decimal,
    triangle_base: Decimal,
) -> Decimal:

    triangle_height: Decimal = (Decimal("2") * triangle_area) / triangle_base
    return triangle_height

#endregion


#region Parallelogram height

def get_paralellogram_height_by_parallelogram_area_and_parallelogram_base(
    *,
    parallelogram_area: Decimal,
    parallelogram_base: Decimal,
) -> Decimal:

    paralellogram_height: Decimal = parallelogram_area / parallelogram_base
    return paralellogram_height

#endregion
