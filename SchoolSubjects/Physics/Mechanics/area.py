from decimal import Decimal


#region General area

def get_general_area_by_general_force_and_mechanic_pressure(
    *,
    general_force: Decimal,
    mechanic_pressure: Decimal,
) -> Decimal:

    general_area: Decimal = general_force / mechanic_pressure
    return general_area

#endregion
