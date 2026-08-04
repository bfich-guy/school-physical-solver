from decimal import Decimal


#region General mass

def get_general_mass_by_general_density_and_general_volume(
    *,
    general_density: Decimal,
    general_volume: Decimal,
) -> Decimal:

    general_mass: Decimal = general_density * general_volume
    return general_mass

#endregion


#region Object mass

def get_object_mass_by_resultant_force_and_general_acceleration(
    *,
    resultant_force: Decimal,
    general_acceleration: Decimal,
) -> Decimal:

    object_mass: Decimal = resultant_force / general_acceleration
    return object_mass


def get_object_mass_by_linear_momentum_and_linear_velocity(
    *,
    linear_momentum: Decimal,
    linear_velocity: Decimal,
) -> Decimal:

    object_mass: Decimal = linear_momentum / linear_velocity
    return object_mass


def get_object_mass_by_sensible_heat_and_specific_heat_and_delta_temperature(
    *,
    sensible_heat: Decimal,
    specific_heat: Decimal,
    delta_temperature: Decimal,
) -> Decimal:

    object_mass: Decimal = sensible_heat / (specific_heat * delta_temperature)
    return object_mass


def get_object_mass_by_combusion_heat_and_calorific_value(
    *,
    combusion_heat: Decimal,
    calorific_value: Decimal,
) -> Decimal:

    object_mass: Decimal = combusion_heat / calorific_value
    return object_mass

#endregion
