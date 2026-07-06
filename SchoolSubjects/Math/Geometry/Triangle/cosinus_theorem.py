from decimal import Decimal

from config import DECIMAL_DEFAULT_COSINUS_VALUE

def get_triangle_third_side_by_cosinus_theorem(
    *,
    first_side: Decimal,
    second_side: Decimal,
    angle_cosiunus: Decimal = DECIMAL_DEFAULT_COSINUS_VALUE,
) -> Decimal:

    triangle_third_side: Decimal = ((first_side ** 2) + (second_side ** 2) - (2 * first_side * second_side * angle_cosiunus)).sqrt()
    return triangle_third_side

