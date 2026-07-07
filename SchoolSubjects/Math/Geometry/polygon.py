from decimal import Decimal


# region Genereal Polygon

def get_general_polygon_angles_sum_by_side_amount(
    *,
    side_amount: Decimal,
) -> Decimal:

    general_polygon_angles_sum: Decimal = (side_amount - 2) * 180
    return general_polygon_angles_sum

    
def get_general_polygon_perimeter_by_sides(
    *,
    sides_array: list[Decimal],
) -> Decimal:

    general_polygon_perimeter: Decimal = sum(sides_array)
    return general_polygon_perimeter

# endregion


# region Regular Polygon

def get_regular_polygon_angle_value_by_side_amount(
    *,
    side_amount: Decimal,
) -> Decimal:

    regular_polygon_angle_value: Decimal = ((side_amount - 2) * 180) / side_amount
    return regular_polygon_angle_value

# endregion
