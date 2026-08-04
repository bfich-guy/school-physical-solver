from decimal import Decimal


#region Mechanic work

def get_mechanic_work_by_general_force_and_general_distance_and_angle_cosinus(
    *,
    general_force: Decimal,
    general_distance: Decimal,
    angle_cosinus: Decimal,
) -> Decimal:

    mechanic_work: Decimal = general_force * general_distance * angle_cosinus
    return mechanic_work

#endregion
