from decimal import Decimal


#region Angle cosinus

def get_angle_cosinus_by_mechanic_work_and_general_force_and_general_distance(
    *,
    mechanic_work: Decimal,
    general_force: Decimal,
    general_distance: Decimal,
) -> Decimal:

    angle_cosinus: Decimal = mechanic_work / (general_force * general_distance)
    return angle_cosinus

#endregion
