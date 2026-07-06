from decimal import Decimal

from config import PI

def get_circumference_by_radius(
    *,
    pi: Decimal = PI,
    radius: Decimal,
) -> Decimal:

    circumference: Decimal = 2 * pi * radius
    return circumference

