from decimal import Decimal


#region Thermal efficiency

def get_thermal_efficiency_by_useful_general_heat_and_spent_general_heat(
    *,
    useful_general_heat: Decimal,
    spent_general_heat: Decimal,
) -> Decimal:

    thermal_efficiency: Decimal = (useful_general_heat / spent_general_heat) * Decimal("100")
    return thermal_efficiency

#endregion
