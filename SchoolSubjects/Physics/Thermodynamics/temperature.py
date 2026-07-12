from decimal import Decimal


#region Start temperature

def get_start_temperature_by_end_temperature_and_delta_temperature(
    *,
    end_temperature: Decimal,
    delta_temperature: Decimal,
) -> Decimal:

    start_temperature: Decimal = delta_temperature - end_temperature
    return start_temperature

#endregion


#region End temperature

def get_end_temperature_by_delta_temperature_and_start_temperature(
    *,
    delta_temperature: Decimal,
    start_temperature: Decimal,
) -> Decimal:

    end_temperature: Decimal = delta_temperature - start_temperature
    return end_temperature

#endregion


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
