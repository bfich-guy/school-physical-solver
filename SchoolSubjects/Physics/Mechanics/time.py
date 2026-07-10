from decimal import Decimal


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

def get_motion_duration_by_travel_distance_and_linear_velocity(
    *,
    travel_distance: Decimal,
    linear_velocity: Decimal,
) -> Decimal:

    motion_duration: Decimal = travel_distance / linear_velocity
    return motion_duration

#endregion
