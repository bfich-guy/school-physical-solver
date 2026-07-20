from decimal import Decimal

from System.config import MathConstants


#region General distance

def get_general_distance_by_general_velocity_and_motion_duration(
    *,
    general_velocity: Decimal,
    motion_duration: Decimal,
) -> Decimal:

    general_distance: Decimal = general_velocity * motion_duration
    return general_distance


def get_general_distance_by_mechanic_work_and_general_force_and_angle_cosinus(
    *,
    mechanic_work: Decimal,
    general_force: Decimal,
    angle_cosinus: Decimal = MathConstants.DEFAULT_COSINUS.value,
) -> Decimal:

    general_distance: Decimal = mechanic_work / (general_force * angle_cosinus)
    return general_distance

#endregion
