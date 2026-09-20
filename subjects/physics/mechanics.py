from decimal import Decimal


#region Dynamics

def get_angle_cosinus_by_mechanic_work_and_object_force_and_object_distance(
    *,
    mechanic_work: Decimal,
    object_force: Decimal,
    object_distance: Decimal,
) -> Decimal:

    angle_cosinus: Decimal = mechanic_work / (object_force * object_distance)
    return angle_cosinus


def get_stiffness_coefficient_by_elastic_force_and_spring_elongation(
    *,
    elastic_force: Decimal,
    spring_elongation: Decimal,
) -> Decimal:

    stiffness_coefficient: Decimal = elastic_force / spring_elongation
    return stiffness_coefficient


def get_object_density_by_object_mass_and_object_volume(
    *,
    object_mass: Decimal,
    object_volume: Decimal,
) -> Decimal:

    object_density: Decimal = object_mass / object_volume
    return object_density


def get_object_density_by_hydrostatic_pressure_and_gravitational_acceleration_and_fluid_height(
    *,
    hydrostatic_pressure: Decimal,
    gravitational_acceleration: Decimal,
    fluid_height: Decimal,
) -> Decimal:

    object_density: Decimal = hydrostatic_pressure / (gravitational_acceleration * fluid_height)
    return object_density


def get_fluid_density_by_archimedes_law(
    *,
    archimedes_force: Decimal,
    submerged_volume: Decimal,
    gravitational_acceleration: Decimal,
) -> Decimal:

    fluid_density: Decimal = archimedes_force / (submerged_volume * gravitational_acceleration)
    return fluid_density


def get_mechanical_efficiency_by_useful_mechanical_work_and_spent_mechanical_work(
    *,
    useful_mechanical_work: Decimal,
    spent_mechanical_work: Decimal,
) -> Decimal:

    mechanical_efficiency: Decimal = (useful_mechanical_work / spent_mechanical_work) * Decimal("100")
    return mechanical_efficiency


def get_kinetic_energy_by_linear_momentum_and_linear_velocity(
    *,
    linear_momentum: Decimal,
    linear_velocity: Decimal,
) -> Decimal:

    kinetic_energy: Decimal = (linear_momentum * linear_velocity) / Decimal("2")
    return kinetic_energy


def get_potential_energy_by_gravitational_force_and_lift_height(
    *,
    gravitational_force: Decimal,
    lift_height: Decimal,
) -> Decimal:

    potential_energy: Decimal = gravitational_force * lift_height
    return potential_energy


def get_object_force_by_mechanical_work_and_object_distance_and_angle_cosinus(
    *,
    mechanical_work: Decimal,
    object_distance: Decimal,
    angle_cosinus: Decimal,
) -> Decimal:

    object_force: Decimal = mechanical_work / (object_distance * angle_cosinus)
    return object_force


def get_object_force_by_mechanic_pressure_and_object_area(
    *,
    mechanic_pressure: Decimal,
    object_area: Decimal,
) -> Decimal:

    object_force: Decimal = mechanic_pressure * object_area
    return object_force


def get_resultant_force_by_newtons_second_law(
    *,
    object_mass: Decimal,
    object_acceleration: Decimal,
) -> Decimal:

    resultant_force: Decimal = object_mass * object_acceleration
    return resultant_force


def get_elastic_force_by_spring_stiffness_and_spring_elongation(
    *,
    spring_stiffness: Decimal,
    spring_elongation: Decimal,
) -> Decimal:

    elastic_force: Decimal = spring_stiffness * spring_elongation
    return elastic_force


def get_normal_force_by_friction_force_and_friction_coefficient(
    *,
    friction_force: Decimal,
    friction_coefficient: Decimal,
) -> Decimal:

    normal_force: Decimal = friction_force / friction_coefficient
    return normal_force


def get_gravitational_force_by_potential_energy_and_lift_height(
    *,
    potential_energy: Decimal,
    lift_height: Decimal,
) -> Decimal:

    gravitational_force: Decimal = potential_energy / lift_height
    return gravitational_force


def get_friction_force_by_friction_coefficient_and_normal_force(
    *,
    friction_coefficient: Decimal,
    normal_force: Decimal,
) -> Decimal:

    friction_force: Decimal = friction_coefficient * normal_force
    return friction_force


def get_lift_height_by_potential_energy_and_gravitational_force(
    *,
    potential_energy: Decimal,
    gravitational_force: Decimal,
) -> Decimal:

    lift_height: Decimal = potential_energy / gravitational_force
    return lift_height


def get_object_mass_by_object_density_and_object_volume(
    *,
    object_density: Decimal,
    object_volume: Decimal,
) -> Decimal:

    object_mass: Decimal = object_density * object_volume
    return object_mass


def get_object_mass_by_newtons_second_law(
    *,
    resultant_force: Decimal,
    object_acceleration: Decimal,
) -> Decimal:

    object_mass: Decimal = resultant_force / object_acceleration
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


def get_linear_momentum_by_object_mass_and_linear_velocity(
    *,
    object_mass: Decimal,
    linear_velocity: Decimal,
) -> Decimal:

    linear_momentum: Decimal = object_mass * linear_velocity
    return linear_momentum


def get_linear_momentum_by_kinetic_energy_and_linear_velocity(
    *,
    kinetic_energy: Decimal,
    linear_velocity: Decimal,
) -> Decimal:

    linear_momentum: Decimal = (Decimal("2") * kinetic_energy) / linear_velocity
    return linear_momentum


def get_mechanic_power_by_mechanic_work_and_object_duration(
    *,
    mechanic_work: Decimal,
    object_duration: Decimal,
) -> Decimal:

    mechanic_power: Decimal = mechanic_work / object_duration
    return mechanic_power


def get_object_volume_by_object_mass_and_object_density(
    *,
    object_mass: Decimal,
    object_density: Decimal,
) -> Decimal:

    object_volume: Decimal = object_mass / object_density
    return object_volume


def get_submerged_volume_by_archimedes_force_and_fluid_density_and_gravitational_acceleration(
    *,
    archimedes_force: Decimal,
    fluid_density: Decimal,
    gravitational_acceleration: Decimal,
) -> Decimal:

    submerged_volume: Decimal = archimedes_force / (fluid_density * gravitational_acceleration)
    return submerged_volume


def get_useful_mechanical_work_by_mechanical_efficiency_and_spent_mechanical_work(
    *,
    mechanical_efficiency: Decimal,
    spent_mechanical_work: Decimal,
) -> Decimal:

    useful_mechanical_work: Decimal = (mechanical_efficiency * spent_mechanical_work) / Decimal("100")
    return useful_mechanical_work


def get_spent_mechanical_work_by_mechanical_efficiency_and_useful_mechanical_work(
    *,
    mechanical_efficiency: Decimal,
    useful_mechanical_work: Decimal,
) -> Decimal:

    spent_mechanical_work: Decimal = (useful_mechanical_work / mechanical_efficiency) * Decimal("100")
    return spent_mechanical_work


def get_mechanical_work_by_object_force_and_object_distance_and_angle_cosinus(
    *,
    object_force: Decimal,
    object_distance: Decimal,
    angle_cosinus: Decimal,
) -> Decimal:

    mechanical_work: Decimal = object_force * object_distance * angle_cosinus
    return mechanical_work


def get_archimedes_force_by_archimedes_law(
    *,
    fluid_density: Decimal,
    submerged_volume: Decimal,
    gravitational_acceleration: Decimal,
) -> Decimal:

    archimedes_force: Decimal = fluid_density * submerged_volume * gravitational_acceleration
    return archimedes_force


def get_object_distance_by_mechanical_work_and_object_force_and_angle_cosinus(
    *,
    mechanical_work: Decimal,
    object_force: Decimal,
    angle_cosinus: Decimal,
) -> Decimal:

    object_distance: Decimal = mechanical_work / (object_force * angle_cosinus)
    return object_distance


def get_object_duration_by_mechanic_work_and_mechanic_power(
    *,
    mechanic_work: Decimal,
    mechanic_power: Decimal,
) -> Decimal:

    object_duration: Decimal = mechanic_work / mechanic_power
    return object_duration


def get_linear_velocity_by_linear_momentum_and_object_mass(
    *,
    linear_momentum: Decimal,
    object_mass: Decimal,
) -> Decimal:

    linear_velocity: Decimal = linear_momentum / object_mass
    return linear_velocity


def get_linear_velocity_by_kinetic_energy_and_momentum(
    *,
    kinetic_energy: Decimal,
    linear_momentum: Decimal,
) -> Decimal:

    linear_velocity: Decimal = (Decimal("2") * kinetic_energy) / linear_momentum
    return linear_velocity

#endregion


#region Kinematics

def get_object_acceleration_by_newtons_second_law(
    *,
    resultant_force: Decimal,
    object_mass: Decimal,
) -> Decimal:

    object_acceleration: Decimal = resultant_force / object_mass
    return object_acceleration


def get_linear_acceleration_by_delta_velocity_and_delta_duration(
    *,
    delta_velocity: Decimal,
    delta_duration: Decimal,
) -> Decimal:

    linear_acceleration: Decimal = delta_velocity / delta_duration
    return linear_acceleration


def get_centripetal_acceleration_by_linear_velocity_and_trajectory_radius(
    *,
    linear_velocity: Decimal,
    trajectory_radius: Decimal,
) -> Decimal:

    centripetal_acceleration: Decimal = (linear_velocity ** Decimal("2")) / trajectory_radius
    return centripetal_acceleration


def get_centripetal_acceleration_by_angular_velocity_and_trajectory_radius(
    *,
    angular_velocity: Decimal,
    trajectory_radius: Decimal,
) -> Decimal:

    centripetal_acceleration: Decimal = (angular_velocity ** Decimal("2")) * trajectory_radius
    return centripetal_acceleration


def get_centripetal_acceleration_by_linear_and_angular_velocity(
    *,
    linear_velocity: Decimal,
    angular_velocity: Decimal,
) -> Decimal:

    centripetal_acceleration: Decimal = linear_velocity * angular_velocity
    return centripetal_acceleration


def get_gravitational_acceleration_by_hydrostatic_pressure_and_object_density_and_fluid_height(
    *,
    hydrostatic_pressure: Decimal,
    object_density: Decimal,
    fluid_height: Decimal,
) -> Decimal:

    gravitational_acceleration: Decimal = hydrostatic_pressure / (object_density * fluid_height)
    return gravitational_acceleration


def get_gravitational_acceleration_by_archimedes_law(
    *,
    archimedes_force: Decimal,
    fluid_density: Decimal,
    submerged_volume: Decimal,
) -> Decimal:

    gravitational_acceleration: Decimal = archimedes_force / (fluid_density * submerged_volume)
    return gravitational_acceleration


def get_object_distance_by_object_velocity_and_motion_duration(
    *,
    object_velocity: Decimal,
    motion_duration: Decimal,
) -> Decimal:

    object_distance: Decimal = object_velocity * motion_duration
    return object_distance


def get_motion_duration_by_object_distance_and_object_velocity(
    *,
    object_distance: Decimal,
    object_velocity: Decimal,
) -> Decimal:

    motion_duration: Decimal = object_distance / object_velocity
    return motion_duration


def get_delta_duration_by_delta_velocity_and_linear_acceleration(
    *,
    delta_velocity: Decimal,
    linear_acceleration: Decimal,
) -> Decimal:

    delta_duration: Decimal = delta_velocity / linear_acceleration
    return delta_duration


def get_object_velocity_by_object_distance_and_motion_duration(
    *,
    object_distance: Decimal,
    motion_duration: Decimal,
) -> Decimal:

    object_velocity: Decimal = object_distance / motion_duration
    return object_velocity


def get_linear_velocity_by_angular_velocity_and_trajectory_radius(
    *,
    angular_velocity: Decimal,
    trajectory_radius: Decimal,
) -> Decimal:

    linear_velocity: Decimal = angular_velocity * trajectory_radius
    return linear_velocity


def get_linear_velocity_by_centripetal_acceleration_and_angular_velocity(
    *,
    centripetal_acceleration: Decimal,
    angular_velocity: Decimal,
) -> Decimal:

    linear_velocity: Decimal = centripetal_acceleration / angular_velocity
    return linear_velocity


def get_angular_velocity_by_linear_velocity_and_trajectory_radius(
    *,
    linear_velocity: Decimal,
    trajectory_radius: Decimal,
) -> Decimal:

    angular_velocity: Decimal = linear_velocity / trajectory_radius
    return angular_velocity


def get_angular_velocity_by_centripetal_acceleration_and_linear_velocity(
    *,
    centripetal_acceleration: Decimal,
    linear_velocity: Decimal,
) -> Decimal:

    angular_velocity: Decimal = centripetal_acceleration / linear_velocity
    return angular_velocity


def get_delta_velocity_by_linear_acceleration_and_delta_duration(
    *,
    linear_acceleration: Decimal,
    delta_duration: Decimal,
) -> Decimal:

    delta_velocity: Decimal = linear_acceleration * delta_duration
    return delta_velocity

#endregion


#region Statics

def get_object_area_by_object_force_and_mechanic_pressure(
    *,
    object_force: Decimal,
    mechanic_pressure: Decimal,
) -> Decimal:

    object_area: Decimal = object_force / mechanic_pressure
    return object_area


def get_friction_coefficient_by_friction_force_and_normal_force(
    *,
    friction_force: Decimal,
    normal_force: Decimal,
) -> Decimal:

    friction_coefficient: Decimal = friction_force / normal_force
    return friction_coefficient


def get_spring_elongation_by_elastic_force_and_stiffness_coefficient(
    *,
    elastic_force: Decimal,
    stiffness_coefficient: Decimal,
) -> Decimal:

    spring_elongation: Decimal = elastic_force / stiffness_coefficient
    return spring_elongation


def get_fluid_height_by_hydrostatic_pressure_and_object_density_and_gravitational_acceleration(
    *,
    hydrostatic_pressure: Decimal,
    object_density: Decimal,
    gravitational_acceleration: Decimal,
) -> Decimal:

    fluid_height: Decimal = hydrostatic_pressure / (object_density * gravitational_acceleration)
    return fluid_height


def get_mechanic_pressure_by_object_force_and_object_area(
    *,
    object_force: Decimal,
    object_area: Decimal,
) -> Decimal:

    mechanic_pressure: Decimal = object_force / object_area
    return mechanic_pressure


def get_hydrostatic_pressure_by_object_density_and_gravitational_acceleration_and_fluid_height(
    *,
    object_density: Decimal,
    gravitational_acceleration: Decimal,
    fluid_height: Decimal,
) -> Decimal:

    hydrostatic_pressure: Decimal = object_density * gravitational_acceleration * fluid_height
    return hydrostatic_pressure

#endregion
