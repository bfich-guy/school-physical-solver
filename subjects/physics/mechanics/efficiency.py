from decimal import Decimal


#region Mechanical efficiency

def get_mechanical_efficiency_by_useful_mechanical_work_and_spent_mechanical_work(
    *,
    useful_mechanical_work: Decimal,
    spent_mechanical_work: Decimal,
) -> Decimal:

    mechanical_efficiency: Decimal = (useful_mechanical_work / spent_mechanical_work) * Decimal("100")
    return mechanical_efficiency

#endregion
