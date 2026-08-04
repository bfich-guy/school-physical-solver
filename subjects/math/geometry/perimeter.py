from decimal import Decimal


#region Polygon area

def get_general_polygon_perimeter_by_sides(
    *,
    sides_list: list[Decimal],
) -> Decimal:

    general_polygon_perimeter: Decimal = sum(sides_list, Decimal("0"))
    return general_polygon_perimeter

#endregion


#region Circumference

def get_circumference_by_radius(
    *,
    pi: Decimal,
    circle_radius: Decimal,
) -> Decimal:

    circumference: Decimal = Decimal("2") * pi * circle_radius
    return circumference

#endregion
