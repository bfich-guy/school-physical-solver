from decimal import Decimal

#region Object mass

def get_object_mass_by_material_density_and_object_volume(
    *,
    material_density: Decimal,
    object_volume: Decimal,
) -> Decimal:

    object_mass: Decimal = material_density * object_volume
    return object_mass


def get_object_mass_by_resultant_force_and_general_acceleration(
    *,
    resultant_force: Decimal,
    general_acceleration: Decimal,
) -> Decimal:

    object_mass: Decimal = resultant_force / general_acceleration
    return object_mass


def get_object_mass_by_momentum_and_linear_velocity(
    *,
    momentum: Decimal,
    linear_velocity: Decimal,
) -> Decimal:

    object_mass: Decimal = momentum / linear_velocity
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
