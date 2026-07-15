from decimal import Decimal


#region Delta temperature

def get_delta_temperature_by_sensible_heat_and_specific_heat_and_object_mass(
    *,
    sensible_heat: Decimal,
    specific_heat: Decimal,
    object_mass: Decimal,
) -> Decimal:

    delta_temperature: Decimal = sensible_heat / (specific_heat * object_mass)
    return delta_temperature

#endregion
