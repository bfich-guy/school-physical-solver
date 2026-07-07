from decimal import Decimal

from config import PI


#region Circle area

def get_circle_area_by_radius(
    *,
    pi: Decimal = PI,
    radius: Decimal,
) -> Decimal:

    circle_area: Decimal = pi * (radius ** 2)
    return circle_area

#endregion


#region Circumference

def get_circumference_by_radius(
    *,
    pi: Decimal = PI,
    radius: Decimal,
) -> Decimal:

    circumference: Decimal = 2 * pi * radius
    return circumference

#endregion
