from decimal import Decimal


#region Angle sinus

def get_angle_sinus_by_triangle_area_and_two_sides(
    *,
    triangle_area: Decimal,
    first_side: Decimal,
    second_side: Decimal,
) -> Decimal:

    angle_sinus: Decimal = (Decimal("2") * triangle_area) / (first_side * second_side)
    return angle_sinus


def get_angle_sinus_by_parallelogram_area_and_two_sides(
    *,
    parallelogram_area: Decimal,
    first_side: Decimal,
    second_side: Decimal,
) -> Decimal:

    angle_sinus: Decimal = parallelogram_area / (first_side * second_side)
    return angle_sinus

#endregion


#region Angle value

def get_regular_polygon_angle_value_by_side_amount(
    *,
    side_amount: Decimal,
) -> Decimal:

    regular_polygon_angle_value: Decimal = (side_amount - Decimal("2")) * Decimal("180") / side_amount
    return regular_polygon_angle_value

#endregion


#region Angle sum

def get_general_polygon_angle_sum_by_side_amount(
    *,
    side_amount: Decimal,
) -> Decimal:

    general_polygon_angle_sum: Decimal = (side_amount - Decimal("2")) * Decimal("180")
    return general_polygon_angle_sum

#endregion
