from decimal import Decimal


#region General duration

def get_general_duration_by_mechanic_work_and_mechanic_power(
    *,
    mechanic_work: Decimal,
    mechanic_power: Decimal,
) -> Decimal:

    general_duration: Decimal = mechanic_work / mechanic_power
    return general_duration


#endregion


#region Heating duration

def get_heating_duration_by_joule_heat_and_electric_power(
    *,
    joule_heat: Decimal,
    electric_power: Decimal,
) -> Decimal:

    heating_duration: Decimal = joule_heat / electric_power
    return heating_duration

#endregion


#region Motion duration

def get_motion_duration_by_general_distance_and_general_velocity(
    *,
    general_distance: Decimal,
    general_velocity: Decimal,
) -> Decimal:

    motion_duration: Decimal = general_distance / general_velocity
    return motion_duration

#endregion


#region Delta duration

def get_delta_duration_by_delta_velocity_and_linear_acceleration(
    *,
    delta_velocity: Decimal,
    linear_acceleration: Decimal,
) -> Decimal:

    delta_duration: Decimal = delta_velocity / linear_acceleration
    return delta_duration

#endregion
