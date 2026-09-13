from decimal import Decimal


#region Electrical efficiency

def get_electrical_efficiency_by_useful_electric_power_and_spent_electric_power(
    *,
    useful_electric_power: Decimal,
    spent_electric_power: Decimal,
) -> Decimal:

    electrical_efficiency: Decimal = (useful_electric_power / spent_electric_power) * Decimal("100")
    return electrical_efficiency

#endregion
