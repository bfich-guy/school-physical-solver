from decimal import Decimal


#region General acceleration

def get_general_acceleration_by_resultant_force_and_object_mass(
    *,
    resultant_force: Decimal,
    object_mass: Decimal,
) -> Decimal:

    general_acceleration: Decimal = resultant_force / object_mass
    return general_acceleration

#endregion


#region Linear acceleration

def get_linear_acceleration_by_delta_speed_and_delta_time(
    *,
    delta_speed: Decimal,
    delta_time: Decimal,
) -> Decimal:

    linear_acceleration: Decimal = delta_speed / delta_time
    return linear_acceleration

#endregion


#region Centripetal acceleration

def get_centripetal_acceleration_by_linear_velocity_and_radius(
    *,
    linear_velocity: Decimal,
    radius: Decimal,
) -> Decimal:

    centripetal_acceleration: Decimal = (linear_velocity ** Decimal("2")) / radius
    return centripetal_acceleration


def get_centripetal_acceleration_by_angular_velocity_and_radius(
    *,
    angular_velocity: Decimal,
    radius: Decimal,
) -> Decimal:

    centripetal_acceleration: Decimal = (angular_velocity ** Decimal("2")) * radius
    return centripetal_acceleration


def get_centripetal_acceleration_by_linear_and_angular_velocity(
    *,
    linear_velocity: Decimal,
    angular_velocity: Decimal,
) -> Decimal:

    centripetal_acceleration: Decimal = linear_velocity * angular_velocity
    return centripetal_acceleration

#endregion
