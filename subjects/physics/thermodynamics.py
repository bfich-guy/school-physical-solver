from decimal import Decimal


#region Sensible heat

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
    delta_temperature: Decimal,
) -> Decimal:

    specific_heat: Decimal = sensible_heat / (object_mass * delta_temperature)
    return specific_heat


def get_object_mass_by_sensible_heat_and_specific_heat_and_delta_temperature(
    *,
    sensible_heat: Decimal,
    specific_heat: Decimal,
    delta_temperature: Decimal,
) -> Decimal:

    object_mass: Decimal = sensible_heat / (specific_heat * delta_temperature)
    return object_mass


def get_delta_temperature_by_sensible_heat_and_specific_heat_and_object_mass(
    *,
    sensible_heat: Decimal,
    specific_heat: Decimal,
    object_mass: Decimal,
) -> Decimal:

    delta_temperature: Decimal = sensible_heat / (specific_heat * object_mass)
    return delta_temperature

#endregion


#region Combusion heat

def get_combusion_heat_by_object_mass_and_calorific_value(
    *,
    object_mass: Decimal,
    calorific_value: Decimal,
) -> Decimal:

    combusion_heat: Decimal = calorific_value * object_mass
    return combusion_heat


def get_object_mass_by_combusion_heat_and_calorific_value(
    *,
    combusion_heat: Decimal,
    calorific_value: Decimal,
) -> Decimal:

    object_mass: Decimal = combusion_heat / calorific_value
    return object_mass


def get_calorific_value_by_combusion_heat_and_object_mass(
    *,
    combusion_heat: Decimal,
    object_mass: Decimal,
) -> Decimal:

    calorific_value: Decimal = combusion_heat / object_mass
    return calorific_value

#endregion


#region Mendeleev-Clayperon law

def get_gas_pressure_by_mendeleev_clayperon_law(
    *,
    gas_volume: Decimal,
    gas_moles: Decimal,
    gas_constant: Decimal,
    gas_temperature: Decimal,
) -> Decimal:

    gas_pressure: Decimal = (gas_moles * gas_constant * gas_temperature) / gas_volume
    return gas_pressure


def get_gas_volume_by_mendeleev_clayperon_law(
    *,
    gas_pressure: Decimal,
    gas_moles: Decimal,
    gas_constant: Decimal,
    gas_temperature: Decimal,
) -> Decimal:

    gas_volume: Decimal = (gas_moles * gas_constant * gas_temperature) / gas_pressure
    return gas_volume


def get_gas_moles_by_mendeleev_clayperon_law(
    *,
    gas_pressure: Decimal,
    gas_volume: Decimal,
    gas_constant: Decimal,
    gas_temperature: Decimal,
) -> Decimal:

    gas_moles: Decimal = (gas_pressure * gas_volume) / (gas_constant * gas_temperature)
    return gas_moles


def get_gas_temperature_by_mendeleev_clayperon_law(
    *,
    gas_pressure: Decimal,
    gas_volume: Decimal,
    gas_constant: Decimal,
    gas_moles: Decimal,
) -> Decimal:

    gas_temperature: Decimal = (gas_pressure * gas_volume) / (gas_moles * gas_constant)
    return gas_temperature


def get_object_moles_by_object_mass_and_object_molar_mass(
    *,
    object_mass: Decimal,
    object_molar_mass: Decimal,
) -> Decimal:

    object_moles: Decimal = object_mass / object_molar_mass
    return object_moles


def get_object_mass_by_object_molar_mass_and_object_moles(
    *,
    object_molar_mass: Decimal,
    object_moles: Decimal,
) -> Decimal:

    object_mass: Decimal = object_molar_mass * object_moles
    return object_mass


def get_object_molar_mass_by_object_mass_and_object_moles(
    *,
    object_mass: Decimal,
    object_moles: Decimal,
) -> Decimal:

    object_molar_mass: Decimal = object_mass / object_moles
    return object_molar_mass

#endregion
