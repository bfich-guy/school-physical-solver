from decimal import Decimal


#region Polygon perimeter

def get_general_polygon_perimeter_by_general_polygon_sides(
    *,
    general_polygon_sides: list[Decimal],
) -> Decimal:

    general_polygon_perimeter: Decimal = sum(general_polygon_sides, Decimal("0"))
    return general_polygon_perimeter

#endregion


#region Triangle perimeter

def get_triangle_perimeter_by_triangle_area_and_triangle_inradius(
    *,
    triangle_area: Decimal,
    triangle_inradius: Decimal,
) -> Decimal:

    triangle_perimeter: Decimal = (triangle_area * Decimal("2")) / triangle_inradius
    return triangle_perimeter

#endregion


#region Circumference

def get_circumference_by_circle_radius(
    *,
    pi: Decimal,
    circle_radius: Decimal,
) -> Decimal:

    circumference: Decimal = Decimal("2") * pi * circle_radius
    return circumference

#endregion
