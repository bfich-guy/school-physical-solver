from decimal import Decimal
from math import prod


#region Circle radius

def get_circle_radius_by_circle_area(
    *,
    pi: Decimal,
    circle_area: Decimal,
) -> Decimal:

    circle_radius: Decimal = (circle_area / pi).sqrt()
    return circle_radius


def get_circle_radius_by_circumference(
    *,
    pi: Decimal,
    circumference: Decimal,
) -> Decimal:

    circle_radius: Decimal = circumference / (Decimal("2") * pi)
    return circle_radius

#endregion


#region Triangle inradius

def get_triangle_inradius_by_triangle_area_and_triangle_perimeter(
    *,
    triangle_area: Decimal,
    triangle_perimeter: Decimal,
) -> Decimal:

    triangle_inradius: Decimal = (triangle_area * Decimal("2")) / triangle_perimeter
    return triangle_inradius

#endregion


#region Triangle circumradius

def get_triangle_circumradius_by_triangle_sides_and_triangle_area(
    *,
    triangle_sides: list[Decimal],
    triangle_area: Decimal,
) -> Decimal:

    triangle_circumradius: Decimal = Decimal(str(prod(triangle_sides))) / (Decimal("4") * triangle_area)
    return triangle_circumradius

#endregion
