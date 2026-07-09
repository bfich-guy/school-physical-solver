from decimal import Decimal

from Configuration.global_constants import PI


#region Circle area

def get_circle_area_by_circle_radius(
    *,
    pi: Decimal = PI,
    circle_radius: Decimal,
) -> Decimal:

    circle_area: Decimal = pi * (circle_radius ** Decimal("2"))
    return circle_area

#endregion


#region Circumference

def get_circumference_by_radius(
    *,
    pi: Decimal = PI,
    circle_radius: Decimal,
) -> Decimal:

    circumference: Decimal = Decimal("2") * pi * circle_radius
    return circumference

#endregion
