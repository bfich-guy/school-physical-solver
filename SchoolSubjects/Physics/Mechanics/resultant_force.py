from decimal import Decimal

#region Resultive force

def get_resultant_force_by_mass_and_acceleration(
    *,
    mass: Decimal,
    acceleration: Decimal,
) -> Decimal:

    resultant_force: Decimal = mass * acceleration
    return resultant_force

#endregion
