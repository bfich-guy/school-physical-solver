from decimal import Decimal


#region General distance

def get_general_distance_by_general_velocity_and_motion_duration(
    *,
    general_velocity: Decimal,
    motion_duration: Decimal,
) -> Decimal:

    general_distance: Decimal = general_velocity * motion_duration
    return general_distance


def get_general_distance_by_mechanical_work_and_general_force_and_angle_cosinus(
    *,
    mechanical_work: Decimal,
    general_force: Decimal,
    angle_cosinus: Decimal,
) -> Decimal:

    general_distance: Decimal = mechanical_work / (general_force * angle_cosinus)
    return general_distance

#endregion
