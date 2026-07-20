from decimal import Decimal

from System.config import MathConstants


#region Mechanic work

def get_mechanic_work_by_general_force_and_general_distance_and_angle_cosinus(
    *,
    general_force: Decimal,
    general_distance: Decimal,
    angle_cosinus: Decimal = MathConstants.DEFAULT_COSINUS.value,
) -> Decimal:

    mechanic_work: Decimal = general_force * general_distance * angle_cosinus
    return mechanic_work

#endregion
