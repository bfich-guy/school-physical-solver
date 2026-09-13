from decimal import Decimal


#region Angle value

def get_regular_polygon_angle_by_side_amount(
    *,
    regular_polygon_angles_sum: Decimal,
    side_amount: Decimal,
) -> Decimal:

    regular_polygon_angle: Decimal = regular_polygon_angles_sum / side_amount
    return regular_polygon_angle

#endregion
