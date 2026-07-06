from decimal import Decimal

from config import PI

def get_circle_area_by_radius(
    *,
    pi: Decimal = PI,
    radius: Decimal,
) -> Decimal:

    circle_area: Decimal = pi * (radius ** 2)
    return circle_area

