from decimal import Decimal


#region Classic

def get_sensible_heat_by_specific_heat_and_object_mass_and_delta_temperature(
    *,
    specific_heat: Decimal,
    object_mass: Decimal,
    delta_temperature: Decimal,
) -> Decimal:

    sensible_heat: Decimal = specific_heat * object_mass * delta_temperature
    return sensible_heat


def get_specific_heat_by_sensible_heat_and_object_mass_and_delta_temperature(
    *,
    sensible_heat: Decimal,
    object_mass: Decimal,
    delta_temperature: Decimal
) -> Decimal:

    specific_heat: Decimal = sensible_heat / (object_mass * delta_temperature)
    return specific_heat


def get_combusion_heat_by_object_mass_and_calorific_value(
    *,
    object_mass: Decimal,
    calorific_value: Decimal,
) -> Decimal:

    combusion_heat: Decimal = calorific_value * object_mass
    return combusion_heat


def get_calorific_value_by_combusion_heat_and_object_mass(
    *,
    combusion_heat: Decimal,
    object_mass: Decimal,
) -> Decimal:

    calorific_value: Decimal = combusion_heat / object_mass
    return calorific_value


def get_joule_heat_by_electric_power_and_heating_duration(
    *,
    electric_power: Decimal,
    heating_duration: Decimal,
) -> Decimal:

    joule_heat: Decimal = electric_power * heating_duration
    return joule_heat


def get_delta_temperature_by_sensible_heat_and_specific_heat_and_object_mass(
    *,
    sensible_heat: Decimal,
    specific_heat: Decimal,
    object_mass: Decimal,
) -> Decimal:

    delta_temperature: Decimal = sensible_heat / (specific_heat * object_mass)
    return delta_temperature


def get_heating_duration_by_joule_heat_and_electric_power(
    *,
    joule_heat: Decimal,
    electric_power: Decimal,
) -> Decimal:

    heating_duration: Decimal = joule_heat / electric_power
    return heating_duration

#endregion

