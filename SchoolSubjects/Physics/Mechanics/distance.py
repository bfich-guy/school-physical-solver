from decimal import Decimal


#region Travel distance

def get_travel_distance_by_linear_velocity_and_motion_duration(
    *,
    linear_velocity: Decimal,
    motion_duration: Decimal,
) -> Decimal:

    travel_distance: Decimal = linear_velocity * motion_duration
    return travel_distance

#endregion
