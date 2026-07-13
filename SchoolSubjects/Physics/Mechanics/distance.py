from decimal import Decimal


#region General distance

def get_general_distance_by_general_velocity_and_motion_duration(
    *,
    general_velocity: Decimal,
    motion_duration: Decimal,
) -> Decimal:

    general_distance: Decimal = general_velocity * motion_duration
    return general_distance

#endregion
