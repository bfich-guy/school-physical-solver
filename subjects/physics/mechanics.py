from decimal import Decimal


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


#region Hookes law

def get_hookes_force_by_hookes_law(
    *,
    spring_stiffness: Decimal,
    spring_elongation: Decimal,
) -> Decimal:

    hookes_force: Decimal = spring_stiffness * spring_elongation
    return hookes_force


def get_spring_stiffness_by_hookes_law(
    *,
    hookes_force: Decimal,
    spring_elongation: Decimal,
) -> Decimal:

    spring_stiffness: Decimal = hookes_force / spring_elongation
    return spring_stiffness


def get_spring_elongation_by_hookes_law(
    *,
    hookes_force: Decimal,
    spring_stiffness: Decimal,
) -> Decimal:

    spring_elongation: Decimal = hookes_force / spring_stiffness
    return spring_elongation

#endregion


#region Amontons-Coloumb law

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


def get_normal_force_by_amontons_coulomb_law(
    *,
    friction_force: Decimal,
    friction_coefficient: Decimal,
) -> Decimal:

    normal_force: Decimal = friction_force / friction_coefficient
    return normal_force

#endregion


#region Pascals law

def get_applied_force_by_pascals_law(
    *,
    mechanical_pressure: Decimal,
    object_area: Decimal,
) -> Decimal:

    applied_force: Decimal = mechanical_pressure * object_area
    return applied_force


def get_object_area_by_pascals_law(
    *,
    applied_force: Decimal,
    mechanical_pressure: Decimal,
) -> Decimal:

    object_area: Decimal = applied_force / mechanical_pressure
    return object_area


def get_mechanical_pressure_by_pascals_law(
    *,
    applied_force: Decimal,
    object_area: Decimal,
) -> Decimal:

    mechanical_pressure: Decimal = applied_force / object_area
    return mechanical_pressure

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


#region Normal reaction law

def get_normal_force_by_normal_reaction_law(
    *,
    weight_force: Decimal,
    angle_cosinus: Decimal,
) -> Decimal:

    normal_force: Decimal = weight_force * angle_cosinus
    return normal_force


def get_weight_force_by_normal_reaction_law(
    *,
    normal_force: Decimal,
    angle_cosinus: Decimal,
) -> Decimal:

    weight_force: Decimal = normal_force / angle_cosinus
    return weight_force


def get_angle_cosinus_by_normal_reaction_law(
    *,
    normal_force: Decimal,
    weight_force: Decimal,
) -> Decimal:

    angle_cosinus: Decimal = normal_force / weight_force
    return angle_cosinus

#endregion


#region Momentum law

def get_object_momentum_by_momentum_law(
    *,
    object_mass: Decimal,
    object_velocity: Decimal,
) -> Decimal:

    object_momentum: Decimal = object_mass * object_velocity
    return object_momentum


def get_object_mass_by_momentum_law(
    *,
    object_momentum: Decimal,
    object_velocity: Decimal,
) -> Decimal:

    object_mass: Decimal = object_momentum / object_velocity
    return object_mass


def get_object_velocity_by_momentum_law(
    *,
    object_momentum: Decimal,
    object_mass: Decimal,
) -> Decimal:

    object_velocity: Decimal = object_momentum / object_mass
    return object_velocity

#endregion


#region Momentum conversation law

def get_object_mass_by_momentum_conversation_law(
    *,
    given_momentums: list[Decimal],
    object_initial_velocity: Decimal,
) -> Decimal:

    object_mass: Decimal = (given_momentums[0] + given_momentums[1] - given_momentums[2]) / object_initial_velocity
    return object_mass


def get_object_initial_velocity_by_momentum_conversation_law(
    *,
    given_momentums: list[Decimal],
    object_mass: Decimal,
) -> Decimal:

    object_initial_velocity: Decimal = (given_momentums[0] + given_momentums[1] - given_momentums[2]) / object_mass
    return object_initial_velocity


def get_object_final_velocity_by_momentum_conversation_law(
    *,
    given_momentums: list[Decimal],
    object_mass: Decimal,
) -> Decimal:

    object_final_velocity: Decimal = (given_momentums[0] + given_momentums[1] - given_momentums[2]) / object_mass
    return object_final_velocity

#endregion


#region Kinetic energy law

def get_kinetic_energy_by_kinetic_energy_law(
    *,
    object_momentum: Decimal,
    object_velocity: Decimal,
) -> Decimal:

    kinetic_energy: Decimal = (object_momentum * object_velocity) / Decimal("2")
    return kinetic_energy


def get_object_momentum_by_kinetic_energy_law(
    *,
    kinetic_energy: Decimal,
    object_velocity: Decimal,
) -> Decimal:

    object_momentum: Decimal = (Decimal("2") * kinetic_energy) / object_velocity
    return object_momentum


def get_object_velocity_by_kinetic_energy_law(
    *,
    kinetic_energy: Decimal,
    linear_momentum: Decimal,
) -> Decimal:

    object_velocity: Decimal = (Decimal("2") * kinetic_energy) / linear_momentum
    return object_velocity

#endregion


#region Potential energy law

def get_potential_energy_by_potential_energy_law(
    *,
    weight_force: Decimal,
    object_height: Decimal,
) -> Decimal:

    potential_energy: Decimal = weight_force * object_height
    return potential_energy


def get_weight_force_by_potential_energy_law(
    *,
    potential_energy: Decimal,
    object_height: Decimal,
) -> Decimal:

    weight_force: Decimal = potential_energy / object_height
    return weight_force


def get_object_height_by_potential_energy_law(
    *,
    potential_energy: Decimal,
    weight_force: Decimal,
) -> Decimal:

    object_height: Decimal = potential_energy / weight_force
    return object_height

#endregion


#region Hydrostatic pressure law 

def get_hydrostatic_pressure_by_hydrostatic_pressure_law(
    *,
    fluid_density: Decimal,
    gravitational_acceleration: Decimal,
    fluid_height: Decimal,
) -> Decimal:

    hydrostatic_pressure: Decimal = fluid_density * gravitational_acceleration * fluid_height
    return hydrostatic_pressure


def get_fluid_density_by_hydrostatic_pressure_law(
    *,
    hydrostatic_pressure: Decimal,
    gravitational_acceleration: Decimal,
    fluid_height: Decimal,
) -> Decimal:

    fluid_density: Decimal = hydrostatic_pressure / (gravitational_acceleration * fluid_height)
    return fluid_density


def get_gravitational_acceleration_by_hydrostatic_pressure_law(
    *,
    hydrostatic_pressure: Decimal,
    object_density: Decimal,
    fluid_height: Decimal,
) -> Decimal:

    gravitational_acceleration: Decimal = hydrostatic_pressure / (object_density * fluid_height)
    return gravitational_acceleration


def get_fluid_height_by__hydrostatic_pressure_law(
    *,
    hydrostatic_pressure: Decimal,
    fluid_density: Decimal,
    gravitational_acceleration: Decimal,
) -> Decimal:

    fluid_height: Decimal = hydrostatic_pressure / (fluid_density * gravitational_acceleration)
    return fluid_height

#endregion


#region Mechanical work law

def get_mechanical_work_by_mechanical_work_law(
    *,
    applied_force: Decimal,
    object_distance: Decimal,
    angle_cosinus: Decimal,
) -> Decimal:

    mechanical_work: Decimal = applied_force * object_distance * angle_cosinus
    return mechanical_work


def get_applied_force_by_mechanical_work_law(
    *,
    mechanical_work: Decimal,
    object_distance: Decimal,
    angle_cosinus: Decimal,
) -> Decimal:

    applied_force: Decimal = mechanical_work / (object_distance * angle_cosinus)
    return applied_force


def get_object_distance_by_mechanical_work_law(
    *,
    mechanical_work: Decimal,
    applied_force: Decimal,
    angle_cosinus: Decimal,
) -> Decimal:

    object_distance: Decimal = mechanical_work / (applied_force * angle_cosinus)
    return object_distance


def get_angle_cosinus_by_mechanical_work_law(
    *,
    mechanical_work: Decimal,
    applied_force: Decimal,
    object_distance: Decimal,
) -> Decimal:

    angle_cosinus: Decimal = mechanical_work / (applied_force * object_distance)
    return angle_cosinus

#endregion


#region Mechanical power law

def get_mechanical_power_by_mechanical_power_law(
    *,
    mechanical_work: Decimal,
    work_duration: Decimal,
) -> Decimal:

    mechanical_power: Decimal = mechanical_work / work_duration
    return mechanical_power


def get_mechanical_work_by_mechanical_power_law(
    *,
    mechanical_power: Decimal,
    work_duration: Decimal,
) -> Decimal:

    mechanical_work: Decimal = mechanical_power * work_duration
    return mechanical_work


def get_work_duration_by_mechanical_power_law(
    *,
    mechanical_work: Decimal,
    mechanical_power: Decimal,
) -> Decimal:

    work_duration: Decimal = mechanical_work / mechanical_power
    return work_duration

#endregion


#region Linear acceleration law

def get_delta_velocity_by_linear_acceleration_law(
    *,
    object_linear_acceleration: Decimal,
    delta_time_duration: Decimal,
) -> Decimal:

    delta_object_velocity: Decimal = object_linear_acceleration * delta_time_duration
    return delta_object_velocity


def get_object_linear_acceleration_by_linear_acceleration_law(
    *,
    delta_object_velocity: Decimal,
    delta_time_duration: Decimal,
) -> Decimal:

    object_linear_acceleration: Decimal = delta_object_velocity / delta_time_duration
    return object_linear_acceleration


def get_delta_time_duration_by_linear_acceleration_law(
    *,
    delta_object_velocity: Decimal,
    object_linear_acceleration: Decimal,
) -> Decimal:

    delta_time_duration: Decimal = delta_object_velocity / object_linear_acceleration
    return delta_time_duration

#endregion


#region Centripetal acceleration law

def get_centripetal_acceleration_by_centripetal_acceleration_law(
    *,
    linear_velocity: Decimal,
    angular_velocity: Decimal,
) -> Decimal:

    centripetal_acceleration: Decimal = linear_velocity * angular_velocity
    return centripetal_acceleration


def get_linear_velocity_by_centripetal_acceleration_law(
    *,
    centripetal_acceleration: Decimal,
    angular_velocity: Decimal,
) -> Decimal:

    linear_velocity: Decimal = centripetal_acceleration / angular_velocity
    return linear_velocity


def get_angular_velocity_by_centripetal_acceleration_law(
    *,
    centripetal_acceleration: Decimal,
    linear_velocity: Decimal,
) -> Decimal:

    angular_velocity: Decimal = centripetal_acceleration / linear_velocity
    return angular_velocity

#endregion
