from decimal import Decimal


#region Sensible heat

def get_sensible_heat_by_specific_heat_and_object_mass_and_delta_temperature(
    *,
    specific_heat: Decimal,
    object_mass: Decimal,
    delta_temperature: Decimal,
) -> Decimal:

    quantity_heat: Decimal = specific_heat * object_mass * delta_temperature
    return quantity_heat

#endregion


#region Specific heat

def get_specific_heat_by_sensible_heat_and_object_mass_and_delta_temperature(
    *,
    sensible_heat: Decimal,
    object_mass: Decimal,
    delta_temperature: Decimal,
) -> Decimal:

    specific_heat: Decimal = sensible_heat / (object_mass * delta_temperature)
    return specific_heat

#endregion


#region Combusion heat

def get_combusion_heat_by_object_mass_and_calorific_value(
    *,
    object_mass: Decimal,
    calorific_value: Decimal,
) -> Decimal:

    combusion_heat: Decimal = calorific_value * object_mass
    return combusion_heat

#endregion


#region Calorific value

def get_calorific_value_by_combusion_heat_and_object_mass(
    *,
    combusion_heat: Decimal,
    object_mass: Decimal,
) -> Decimal:

    calorific_value: Decimal = combusion_heat / object_mass
    return calorific_value

#endregion


#region Joule heat

def get_joule_heat_by_electric_power_and_heating_duration(
    *,
    electric_power: Decimal,
    heating_duration: Decimal,
) -> Decimal:

    joule_heat: Decimal = electric_power * heating_duration
    return joule_heat

#endregion
