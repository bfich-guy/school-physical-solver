from decimal import Decimal


#region Hookes law

def get_stiffness_coefficient_hookes_law(
    *,
    elastic_force: Decimal,
    spring_elongation: Decimal,
) -> Decimal:

    stiffness_coefficient: Decimal = elastic_force / spring_elongation
    return stiffness_coefficient


def get_elastic_force_by_hookes_law(
    *,
    spring_stiffness: Decimal,
    spring_elongation: Decimal,
) -> Decimal:

    elastic_force: Decimal = spring_stiffness * spring_elongation
    return elastic_force


def get_spring_elongation_by_hookes_law(
    *,
    elastic_force: Decimal,
    stiffness_coefficient: Decimal,
) -> Decimal:

    spring_elongation: Decimal = elastic_force / stiffness_coefficient
    return spring_elongation

#endregion


#region Archimedes law

def get_archimedes_force_by_archimedes_law(
    *,
    fluid_density: Decimal,
    submerged_volume: Decimal,
    gravitational_acceleration: Decimal,
) -> Decimal:

    archimedes_force: Decimal = fluid_density * submerged_volume * gravitational_acceleration
    return archimedes_force


def get_fluid_density_by_archimedes_law(
    *,
    archimedes_force: Decimal,
    submerged_volume: Decimal,
    gravitational_acceleration: Decimal,
) -> Decimal:

    fluid_density: Decimal = archimedes_force / (submerged_volume * gravitational_acceleration)
    return fluid_density


def get_submerged_volume_by_archimedes_law(
    *,
    archimedes_force: Decimal,
    fluid_density: Decimal,
    gravitational_acceleration: Decimal,
) -> Decimal:

    submerged_volume: Decimal = archimedes_force / (fluid_density * gravitational_acceleration)
    return submerged_volume


def get_gravitational_acceleration_by_archimedes_law(
    *,
    archimedes_force: Decimal,
    fluid_density: Decimal,
    submerged_volume: Decimal,
) -> Decimal:

    gravitational_acceleration: Decimal = archimedes_force / (fluid_density * submerged_volume)
    return gravitational_acceleration

#endregion


#region Newtons law

def get_resultant_force_by_newtons_second_law(
    *,
    object_mass: Decimal,
    object_acceleration: Decimal,
) -> Decimal:

    resultant_force: Decimal = object_mass * object_acceleration
    return resultant_force


def get_object_mass_by_newtons_second_law(
    *,
    resultant_force: Decimal,
    object_acceleration: Decimal,
) -> Decimal:

    object_mass: Decimal = resultant_force / object_acceleration
    return object_mass


def get_object_acceleration_by_newtons_second_law(
    *,
    resultant_force: Decimal,
    object_mass: Decimal,
) -> Decimal:

    object_acceleration: Decimal = resultant_force / object_mass
    return object_acceleration

#endregion


#region Amonton-Kulons law

def get_normal_force_by_amontons_coulomb_law(
    *,
    friction_force: Decimal,
    friction_coefficient: Decimal,
) -> Decimal:

    normal_force: Decimal = friction_force / friction_coefficient
    return normal_force


def get_friction_force_by_amontons_coulomb_law(
    *,
    friction_coefficient: Decimal,
    normal_force: Decimal,
) -> Decimal:

    friction_force: Decimal = friction_coefficient * normal_force
    return friction_force


def get_friction_coefficient_by_amontons_coulomb_law(
    *,
    friction_force: Decimal,
    normal_force: Decimal,
) -> Decimal:

    friction_coefficient: Decimal = friction_force / normal_force
    return friction_coefficient


def get_weight_force_by_normal_force_and_angle_cosinus(
    *,
    normal_force: Decimal,
    angle_cosinus: Decimal,
) -> Decimal:

    weight_force: Decimal = normal_force / angle_cosinus
    return weight_force


def get_normal_force_by_weight_force_and_angle_cosinus(
    *,
    weight_force: Decimal,
    angle_cosinus: Decimal,
) -> Decimal:

    normal_force: Decimal = weight_force * angle_cosinus
    return normal_force


def get_angle_cosinus_by_normal_force_and_weight_force(
    *,
    normal_force: Decimal,
    weight_force: Decimal,
) -> Decimal:

    angle_cosinus: Decimal = normal_force / weight_force
    return angle_cosinus

#endregion


#region Pascals law

def get_force_by_pascals_law(
    *,
    mechanic_pressure: Decimal,
    object_area: Decimal,
) -> Decimal:

    object_force: Decimal = mechanic_pressure * object_area
    return object_force


def get_object_area_by_pascals_law(
    *,
    object_force: Decimal,
    mechanic_pressure: Decimal,
) -> Decimal:

    object_area: Decimal = object_force / mechanic_pressure
    return object_area


def get_mechanic_pressure_by_pascals_law(
    *,
    object_force: Decimal,
    object_area: Decimal,
) -> Decimal:

    mechanic_pressure: Decimal = object_force / object_area
    return mechanic_pressure


def get_hydrostatic_pressure_by_pascals_law(
    *,
    fluid_density: Decimal,
    gravitational_acceleration: Decimal,
    fluid_height: Decimal,
) -> Decimal:

    hydrostatic_pressure: Decimal = fluid_density * gravitational_acceleration * fluid_height
    return hydrostatic_pressure


def get_fluid_density_by_pascals_law(
    *,
    hydrostatic_pressure: Decimal,
    gravitational_acceleration: Decimal,
    fluid_height: Decimal,
) -> Decimal:

    fluid_density: Decimal = hydrostatic_pressure / (gravitational_acceleration * fluid_height)
    return fluid_density


def get_gravitational_acceleration_by_pascals_law(
    *,
    hydrostatic_pressure: Decimal,
    object_density: Decimal,
    fluid_height: Decimal,
) -> Decimal:

    gravitational_acceleration: Decimal = hydrostatic_pressure / (object_density * fluid_height)
    return gravitational_acceleration


def get_fluid_height_by_pascals_law(
    *,
    hydrostatic_pressure: Decimal,
    fluid_density: Decimal,
    gravitational_acceleration: Decimal,
) -> Decimal:

    fluid_height: Decimal = hydrostatic_pressure / (fluid_density * gravitational_acceleration)
    return fluid_height

#endregion


#region Momentum conversation law

def get_object_momentum_by_object_mass_and_object_velocity(
    *,
    object_mass: Decimal,
    object_velocity: Decimal,
) -> Decimal:

    object_momentum: Decimal = object_mass * object_velocity
    return object_momentum


def get_object_mass_by_object_momentum_and_object_velocity(
    *,
    object_momentum: Decimal,
    object_velocity: Decimal,
) -> Decimal:

    object_mass: Decimal = object_momentum / object_velocity
    return object_mass


def get_object_velocity_by_object_momentum_and_object_mass(
    *,
    object_momentum: Decimal,
    object_mass: Decimal,
) -> Decimal:

    object_velocity: Decimal = object_momentum / object_mass
    return object_velocity


def get_object_mass_by_momentum_conversation_law(
    *,
    first_final_momentum: Decimal,
    second_final_momentum: Decimal,
    second_initial_momentum: Decimal,
    object_initial_velocity: Decimal,
) -> Decimal:

    object_mass: Decimal = (first_final_momentum + second_final_momentum - second_initial_momentum) / object_initial_velocity
    return object_mass


def get_object_initial_velocity_by_momentum_conversation_law(
    *,
    first_final_momentum: Decimal,
    second_final_momentum: Decimal,
    second_initial_momentum: Decimal,
    object_mass: Decimal,
) -> Decimal:

    object_initial_velocity: Decimal = (first_final_momentum + second_final_momentum - second_initial_momentum) / object_mass
    return object_initial_velocity


def get_object_final_velocity_by_momentum_conversation_law(
    *,
    first_initial_momentum: Decimal,
    second_initial_momentum: Decimal,
    second_final_momentum: Decimal,
    object_mass: Decimal,
) -> Decimal:

    object_final_velocity: Decimal = (first_initial_momentum + second_final_momentum - second_initial_momentum) / object_mass
    return object_final_velocity

#endregion


#region Energy

def get_kinetic_energy_by_object_momentum_and_linear_velocity(
    *,
    object_momentum: Decimal,
    linear_velocity: Decimal,
) -> Decimal:

    kinetic_energy: Decimal = (object_momentum * linear_velocity) / Decimal("2")
    return kinetic_energy


def get_object_momentum_by_kinetic_energy_and_linear_velocity(
    *,
    kinetic_energy: Decimal,
    linear_velocity: Decimal,
) -> Decimal:

    object_momentum: Decimal = (Decimal("2") * kinetic_energy) / linear_velocity
    return object_momentum


def get_linear_velocity_by_kinetic_energy_and_momentum(
    *,
    kinetic_energy: Decimal,
    linear_momentum: Decimal,
) -> Decimal:

    linear_velocity: Decimal = (Decimal("2") * kinetic_energy) / linear_momentum
    return linear_velocity


def get_potential_energy_by_weight_force_and_object_height(
    *,
    weight_force: Decimal,
    object_height: Decimal,
) -> Decimal:

    potential_energy: Decimal = weight_force * object_height
    return potential_energy


def get_weight_force_by_potential_energy_and_object_height(
    *,
    potential_energy: Decimal,
    object_height: Decimal,
) -> Decimal:

    weight_force: Decimal = potential_energy / object_height
    return weight_force


def get_object_height_by_potential_energy_and_weight_force(
    *,
    potential_energy: Decimal,
    weight_force: Decimal,
) -> Decimal:

    object_height: Decimal = potential_energy / weight_force
    return object_height


#endregion


#region Mechanical efficiency

def get_mechanical_efficiency_by_useful_mechanical_work_and_spent_mechanical_work(
    *,
    useful_mechanical_work: Decimal,
    spent_mechanical_work: Decimal,
) -> Decimal:

    mechanical_efficiency: Decimal = (useful_mechanical_work / spent_mechanical_work) * Decimal("100")
    return mechanical_efficiency


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

#endregion


#region Mechanical work

def get_mechanical_work_by_object_force_and_object_distance_and_angle_cosinus(
    *,
    object_force: Decimal,
    object_distance: Decimal,
    angle_cosinus: Decimal,
) -> Decimal:

    mechanical_work: Decimal = object_force * object_distance * angle_cosinus
    return mechanical_work


def get_object_force_by_mechanical_work_and_object_distance_and_angle_cosinus(
    *,
    mechanical_work: Decimal,
    object_distance: Decimal,
    angle_cosinus: Decimal,
) -> Decimal:

    object_force: Decimal = mechanical_work / (object_distance * angle_cosinus)
    return object_force


def get_object_distance_by_mechanical_work_and_object_force_and_angle_cosinus(
    *,
    mechanical_work: Decimal,
    object_force: Decimal,
    angle_cosinus: Decimal,
) -> Decimal:

    object_distance: Decimal = mechanical_work / (object_force * angle_cosinus)
    return object_distance


def get_angle_cosinus_by_mechanical_work_and_object_force_and_object_distance(
    *,
    mechanical_work: Decimal,
    object_force: Decimal,
    object_distance: Decimal,
) -> Decimal:

    angle_cosinus: Decimal = mechanical_work / (object_force * object_distance)
    return angle_cosinus


def get_mechanical_work_by_mechanical_power_and_work_duration(
    *,
    mechanical_power: Decimal,
    work_duration: Decimal,
) -> Decimal:

    mechanical_work: Decimal = mechanical_power * work_duration
    return mechanical_work


def get_mechanical_power_by_mechanical_work_and_work_duration(
    *,
    mechanical_work: Decimal,
    work_duration: Decimal,
) -> Decimal:

    mechanical_power: Decimal = mechanical_work / work_duration
    return mechanical_power


def get_work_duration_by_mechanical_work_and_mechanical_power(
    *,
    mechanical_work: Decimal,
    mechanical_power: Decimal,
) -> Decimal:

    work_duration: Decimal = mechanical_work / mechanical_power
    return work_duration

#endregion


#region Object rotating

def get_object_acceleration_by_delta_velocity_and_delta_duration(
    *,
    delta_velocity: Decimal,
    delta_duration: Decimal,
) -> Decimal:

    object_acceleration: Decimal = delta_velocity / delta_duration
    return object_acceleration


def get_delta_velocity_by_object_acceleration_and_delta_duration(
    *,
    object_acceleration: Decimal,
    delta_duration: Decimal,
) -> Decimal:

    delta_velocity: Decimal = object_acceleration * delta_duration
    return delta_velocity


def get_delta_duration_by_delta_velocity_and_object_acceleration(
    *,
    delta_velocity: Decimal,
    object_acceleration: Decimal,
) -> Decimal:

    delta_duration: Decimal = delta_velocity / object_acceleration
    return delta_duration


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


def get_centripetal_acceleration_by_linear_velocity_and_trajectory_radius(
    *,
    linear_velocity: Decimal,
    trajectory_radius: Decimal,
) -> Decimal:

    centripetal_acceleration: Decimal = pow(linear_velocity, Decimal("2")) / trajectory_radius
    return centripetal_acceleration


def get_centripetal_acceleration_by_angular_velocity_and_trajectory_radius(
    *,
    angular_velocity: Decimal,
    trajectory_radius: Decimal,
) -> Decimal:

    centripetal_acceleration: Decimal = pow(angular_velocity, Decimal("2")) * trajectory_radius
    return centripetal_acceleration


def get_centripetal_acceleration_by_linear_velocity_and_angular_velocity(
    *,
    linear_velocity: Decimal,
    angular_velocity: Decimal,
) -> Decimal:

    centripetal_acceleration: Decimal = linear_velocity * angular_velocity
    return centripetal_acceleration


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


def get_trajectory_radius_by_centripetal_acceleration_and_angluar_velocity(
    *,
    centripetal_acceleration: Decimal,
    angluar_velocity: Decimal,
) -> Decimal:

    trajectory_radius: Decimal = centripetal_acceleration / pow(angluar_velocity, Decimal("2"))
    return trajectory_radius


def get_trajectory_radius_by_linear_velocity_and_angluar_velocity(
    *,
    linear_velocity: Decimal,
    angluar_velocity: Decimal,
) -> Decimal:

    trajectory_radius: Decimal = linear_velocity / angluar_velocity
    return trajectory_radius

#endregion
