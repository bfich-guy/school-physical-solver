from decimal import Decimal


#region Mechanical work

def get_useful_mechanical_work_by_mechanical_efficiency_and_spent_mechanical_work(
    *,
    mechanical_efficiency: Decimal,
    spent_mechanical_work: Decimal,
) -> Decimal:

    useful_mechanical_work: Decimal = (mechanical_efficiency * spent_mechanical_work) / Decimal("100")
    return useful_mechanical_work


def get_spent_mechanical_work_by_mechanical_efficiency_and_useful_mechanical_work(
    *,
    mechanical_efficiency: Decimal,
    useful_mechanical_work: Decimal,
) -> Decimal:

    spent_mechanical_work: Decimal = (useful_mechanical_work / mechanical_efficiency) * Decimal("100")
    return spent_mechanical_work


def get_mechanical_work_by_general_force_and_general_distance_and_angle_cosinus(
    *,
    general_force: Decimal,
    general_distance: Decimal,
    angle_cosinus: Decimal,
) -> Decimal:

    mechanical_work: Decimal = general_force * general_distance * angle_cosinus
    return mechanical_work

#endregion
