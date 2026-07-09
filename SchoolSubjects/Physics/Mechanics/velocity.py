from decimal import Decimal

#region Linear velocity

def get_linear_velocity_by_momentum_and_object_mass(
    *,
    momentum: Decimal,
    object_mass: Decimal,
) -> Decimal:

    linear_velocity: Decimal = momentum / object_mass
    return linear_velocity


def get_linear_velocity_by_kinetic_energy_and_momentum(
    *,
    kinetic_energy: Decimal,
    momentum: Decimal,
) -> Decimal:

    linear_velocity: Decimal = (Decimal("2") * kinetic_energy) / momentum
    return linear_velocity


def get_linear_velocity_by_angular_velocity_and_radius(
    *,
    angular_velocity: Decimal,
    radius: Decimal,
) -> Decimal:

    linear_velocity: Decimal = angular_velocity * radius
    return linear_velocity


def get_linear_velocity_by_travel_distance_and_motion_duration(
    *,
    travel_distance: Decimal,
    motion_duration: Decimal,
) -> Decimal:

    linear_velocity: Decimal = travel_distance / motion_duration
    return linear_velocity

#endregion


#region Angular velocity

def get_angular_velocity_by_linear_velocity_and_radius(
    *,
    linear_velocity: Decimal,
    radius: Decimal,
) -> Decimal:

    angular_velocity: Decimal = linear_velocity / radius
    return angular_velocity

#endregion
