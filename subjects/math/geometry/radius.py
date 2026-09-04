from decimal import Decimal


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
