from decimal import Decimal


#region Angle sum

def get_general_polygon_angle_sum_by_side_amount(
    *,
    side_amount: Decimal,
) -> Decimal:

    general_polygon_angle_sum: Decimal = (side_amount - Decimal("2")) * Decimal("180")
    return general_polygon_angle_sum

#endregion