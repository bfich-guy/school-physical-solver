from decimal import Decimal


#region Mechanic power

def get_mechanic_power_by_mechanic_work_and_general_duration(
    *,
    mechanic_work: Decimal,
    general_duration: Decimal,
) -> Decimal:

    mechanic_power: Decimal = mechanic_work / general_duration
    return mechanic_power

#endregion
