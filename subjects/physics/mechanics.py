from decimal import Decimal
from typing import Callable

from config import PhysMathConstants, QuantitiesNames, global_error_message

from utils import clean_trailing_zeros_from_decimal_number


#region Dynamics

def second_newton_law(
    *,
    calculating_target: str,
    resultant_force: Decimal | None = None,
    object_mass: Decimal | None = None,
    object_acceleration: Decimal = PhysMathConstants.EARTH_GRAVITY_ACCELERATION.value,
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.RESULTANT_FORCE.value: lambda: object_mass * object_acceleration, #type: ignore
        QuantitiesNames.OBJECT_MASS.value: lambda: resultant_force / object_acceleration, #type: ignore
        QuantitiesNames.OBJECT_ACCELERATION.value: lambda: resultant_force / object_mass, #type: ignore
    }

    try:
        raw_answer: Decimal = formulas_map[calculating_target]()
        cleaned_answer: str = f"{clean_trailing_zeros_from_decimal_number(decimal_number=raw_answer)}"

        calculations_result: tuple[bool, str] = (True, cleaned_answer)
        return calculations_result

    except (ZeroDivisionError, TypeError):
        calculations_result: tuple[bool, str] = (False, global_error_message)
        return calculations_result


def hookes_law(
    *,
    calculating_target: str,
    hookes_force: Decimal | None = None,
    spring_stiffness: Decimal | None = None,
    spring_elongation: Decimal | None = None,
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.HOOKES_FORCE.value: lambda: spring_stiffness * spring_elongation, #type: ignore
        QuantitiesNames.SPRING_STIFFNESS.value: lambda: hookes_force / spring_elongation, #type: ignore
        QuantitiesNames.SPRING_ELONGATION.value: lambda: hookes_force / spring_stiffness, #type: ignore
    }

    try:
        raw_answer: Decimal = formulas_map[calculating_target]()
        cleaned_answer: str = f"{clean_trailing_zeros_from_decimal_number(decimal_number=raw_answer)}"

        calculations_result: tuple[bool, str] = (True, cleaned_answer)
        return calculations_result
    
    except (ZeroDivisionError, TypeError):
        calculations_result: tuple[bool, str] = (False, global_error_message)
        return calculations_result


def amontons_coulomb_law(
    *,
    calculating_target: str,
    amontons_coulomb_force: Decimal | None = None,
    friction_coefficient: Decimal | None = None,
    normal_force: Decimal | None = None,
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.AMONTONS_COULOMB_FORCE.value: lambda: friction_coefficient * normal_force, #type: ignore
        QuantitiesNames.FRICTION_COEFFICIENT.value: lambda: amontons_coulomb_force / normal_force, #type: ignore
        QuantitiesNames.NORMAL_FORCE.value: lambda: amontons_coulomb_force / friction_coefficient, #type: ignore
    }

    try:
        raw_answer: Decimal = formulas_map[calculating_target]()
        cleaned_answer: str = f"{clean_trailing_zeros_from_decimal_number(decimal_number=raw_answer)}"

        calculations_result: tuple[bool, str] = (True, cleaned_answer)
        return calculations_result

    except (ZeroDivisionError, TypeError):
        calculations_result: tuple[bool, str] = (False, global_error_message)
        return calculations_result


def normal_reaction_law(
    *,
    calculating_target: str,
    normal_force: Decimal | None = None,
    weight_force: Decimal | None = None,
    angle_cosinus: Decimal | None = None,
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.NORMAL_FORCE.value: lambda: weight_force * angle_cosinus, #type: ignore
        QuantitiesNames.WEIGHT_FORCE.value: lambda: normal_force / angle_cosinus, #type: ignore
        QuantitiesNames.ANGLE_COSINUS.value: lambda: normal_force / weight_force, #type: ignore
    }

    try:
        raw_answer: Decimal = formulas_map[calculating_target]()
        cleaned_answer: str = f"{clean_trailing_zeros_from_decimal_number(decimal_number=raw_answer)}"

        calculations_result: tuple[bool, str] = (True, cleaned_answer)
        return calculations_result

    except (ZeroDivisionError, TypeError):
        calculations_result: tuple[bool, str] = (False, global_error_message)
        return calculations_result


def momentum_law(
    *,
    calculating_target: str,
    object_momentum: Decimal | None = None,
    object_mass: Decimal | None = None,
    object_velocity: Decimal | None = None,
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.OBJECT_MOMENTUM.value: lambda: object_mass * object_velocity, #type: ignore
        QuantitiesNames.OBJECT_MASS.value: lambda: object_momentum / object_velocity, #type: ignore
        QuantitiesNames.OBJECT_VELOCITY.value: lambda: object_momentum / object_mass, #type: ignore
    }

    try:
        raw_answer: Decimal = formulas_map[calculating_target]()
        cleaned_answer: str = f"{clean_trailing_zeros_from_decimal_number(decimal_number=raw_answer)}"

        calculations_result: tuple[bool, str] = (True, cleaned_answer)
        return calculations_result

    except (ZeroDivisionError, TypeError):
        calculations_result: tuple[bool, str] = (False, global_error_message)
        return calculations_result


def momentum_conversation_law(
    *,
    calculating_target: str,
    first_initial_momentum: Decimal | None = None,
    second_initial_momentum: Decimal | None = None,
    first_final_momentum: Decimal | None = None,
    second_final_momentum: Decimal | None = None,
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.FIRST_INITIAL_MOMENTUM.value: lambda: first_final_momentum + second_final_momentum - second_initial_momentum, #type: ignore
        QuantitiesNames.FIRST_FINAL_MOMENTUM.value: lambda: first_initial_momentum + second_initial_momentum - second_final_momentum, #type: ignore
        QuantitiesNames.SECOND_INITIAL_MOMENTUM.value: lambda: first_final_momentum + second_final_momentum - first_initial_momentum, #type: ignore
        QuantitiesNames.SECOND_FINAL_MOMENTUM.value: lambda: first_initial_momentum + second_initial_momentum - first_final_momentum, #type: ignore
    }

    try:
        raw_answer: Decimal = formulas_map[calculating_target]()
        cleaned_answer: str = f"{clean_trailing_zeros_from_decimal_number(decimal_number=raw_answer)}"

        calculations_result: tuple[bool, str] = (True, cleaned_answer)
        return calculations_result

    except (ZeroDivisionError, TypeError):
        calculations_result: tuple[bool, str] = (False, global_error_message)
        return calculations_result


def kinetic_energy_law(
    *,
    calculating_target: str,
    kinetic_energy: Decimal | None = None,
    object_momentum: Decimal | None = None,
    object_velocity: Decimal | None = None,
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.KINETIC_ENERGY.value: lambda: (object_momentum + object_velocity) / Decimal("2"), #type: ignore
        QuantitiesNames.OBJECT_MOMENTUM.value: lambda: (Decimal("2") * kinetic_energy) / object_velocity, #type: ignore
        QuantitiesNames.OBJECT_VELOCITY.value: lambda: (Decimal("2") * kinetic_energy) / object_momentum, #type: ignore
    }

    try:
        raw_answer: Decimal = formulas_map[calculating_target]()
        cleaned_answer: str = f"{clean_trailing_zeros_from_decimal_number(decimal_number=raw_answer)}"

        calculations_result: tuple[bool, str] = (True, cleaned_answer)
        return calculations_result

    except (ZeroDivisionError, TypeError):
        calculations_result: tuple[bool, str] = (False, global_error_message)
        return calculations_result


def potential_energy_law(
    *,
    calculating_target: str,
    potential_energy: Decimal | None = None,
    weight_force: Decimal | None = None,
    height_above_surface: Decimal | None = None,
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.POTENTIAL_ENERGY.value: lambda: weight_force * height_above_surface, #type: ignore
        QuantitiesNames.WEIGHT_FORCE.value: lambda: potential_energy / height_above_surface, #type: ignore
        QuantitiesNames.HEIGHT_ABOVE_SURFACE.value: lambda: potential_energy / weight_force, #type: ignore
    }

    try:
        raw_answer: Decimal = formulas_map[calculating_target]()
        cleaned_answer: str = f"{clean_trailing_zeros_from_decimal_number(decimal_number=raw_answer)}"

        calculations_result: tuple[bool, str] = (True, cleaned_answer)
        return calculations_result

    except (ZeroDivisionError, TypeError):
        calculations_result: tuple[bool, str] = (False, global_error_message)
        return calculations_result


def mechanical_work_law(
    *,
    calculating_target: str,
    mechanical_work: Decimal | None = None,
    applied_force: Decimal | None = None,
    covered_distance: Decimal | None = None,
    angle_cosinus: Decimal | None = None,
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.MECHANICAL_WORK.value: lambda: applied_force * covered_distance * angle_cosinus, #type: ignore
        QuantitiesNames.APPLIED_FORCE.value: lambda: mechanical_work / (covered_distance * angle_cosinus), #type: ignore
        QuantitiesNames.COVERED_DISTANCE.value: lambda: mechanical_work / (applied_force * angle_cosinus), #type: ignore
        QuantitiesNames.ANGLE_COSINUS.value: lambda: mechanical_work / (applied_force * covered_distance), #type: ignore
    }

    try:
        raw_answer: Decimal = formulas_map[calculating_target]()
        cleaned_answer: str = f"{clean_trailing_zeros_from_decimal_number(decimal_number=raw_answer)}"

        calculations_result: tuple[bool, str] = (True, cleaned_answer)
        return calculations_result

    except (ZeroDivisionError, TypeError):
        calculations_result: tuple[bool, str] = (False, global_error_message)
        return calculations_result


def mechanical_power_law(
    *,
    calculating_target: str,
    mechanical_power: Decimal | None = None,
    mechanical_work: Decimal | None = None,
    elapsed_time: Decimal | None = None,
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.MECHANICAL_WORK.value: lambda: mechanical_power * elapsed_time, #type: ignore
        QuantitiesNames.MECHANICAL_POWER.value: lambda: mechanical_work / elapsed_time, #type: ignore
        QuantitiesNames.ELAPSED_TIME.value: lambda: mechanical_work / mechanical_power, #type: ignore
    }

    try:
        raw_answer: Decimal = formulas_map[calculating_target]()
        cleaned_answer: str = f"{clean_trailing_zeros_from_decimal_number(decimal_number=raw_answer)}"

        calculations_result: tuple[bool, str] = (True, cleaned_answer)
        return calculations_result

    except (ZeroDivisionError, TypeError):
        calculations_result: tuple[bool, str] = (False, global_error_message)
        return calculations_result

#endregion


#region Kinematics

def linear_acceleration_law(
    *,
    calculating_target: str,
    linear_acceleration: Decimal | None = None,
    delta_velocity: Decimal | None = None,
    delta_time: Decimal | None = None,
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.DELTA_VELOCITY.value: lambda: linear_acceleration * delta_time, #type: ignore
        QuantitiesNames.LINEAR_ACCELERATION.value: lambda: delta_velocity / delta_time, #type: ignore
        QuantitiesNames.DELTA_TIME.value: lambda: delta_velocity / linear_acceleration, #type: ignore
    }

    try:
        raw_answer: Decimal = formulas_map[calculating_target]()
        cleaned_answer: str = f"{clean_trailing_zeros_from_decimal_number(decimal_number=raw_answer)}"

        calculations_result: tuple[bool, str] = (True, cleaned_answer)
        return calculations_result

    except (ZeroDivisionError, TypeError):
        calculations_result: tuple[bool, str] = (False, global_error_message)
        return calculations_result


def centripetal_acceleration_law(
    *,
    calculating_target: str,
    centripetal_acceleration: Decimal | None = None,
    linear_velocity: Decimal | None = None,
    angular_velocity: Decimal | None = None,
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.CENTRIPETAL_ACCELERATION.value: lambda: linear_velocity * angular_velocity, #type: ignore
        QuantitiesNames.LINEAR_VELOCITY.value: lambda: centripetal_acceleration / angular_velocity, #type: ignore
        QuantitiesNames.ANGULAR_VELOCITY.value: lambda: centripetal_acceleration / linear_velocity, #type: ignore
    }

    try:
        raw_answer: Decimal = formulas_map[calculating_target]()
        cleaned_answer: str = f"{clean_trailing_zeros_from_decimal_number(decimal_number=raw_answer)}"

        calculations_result: tuple[bool, str] = (True, cleaned_answer)
        return calculations_result

    except (ZeroDivisionError, TypeError):
        calculations_result: tuple[bool, str] = (False, global_error_message)
        return calculations_result


def trajectory_radius_law(
    *,
    calculating_target: str,
    trajectory_radius: Decimal | None = None,
    linear_velocity: Decimal | None = None,
    angular_velocity: Decimal | None = None,    
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.LINEAR_VELOCITY.value: lambda: angular_velocity * trajectory_radius, #type: ignore
        QuantitiesNames.TRAJECTORY_RADIUS.value: lambda: linear_velocity / trajectory_radius, #type: ignore
        QuantitiesNames.ANGULAR_VELOCITY.value: lambda: linear_velocity / angular_velocity, #type: ignore
    }

    try:
        raw_answer: Decimal = formulas_map[calculating_target]()
        cleaned_answer: str = f"{clean_trailing_zeros_from_decimal_number(decimal_number=raw_answer)}"

        calculations_result: tuple[bool, str] = (True, cleaned_answer)
        return calculations_result

    except (ZeroDivisionError, TypeError):
        calculations_result: tuple[bool, str] = (False, global_error_message)
        return calculations_result

#endregion


#region Statics

def pascals_law(
    *,
    calculating_target: str,
    mechanical_pressure: Decimal | None = None,
    surface_area: Decimal | None = None,
    pressure_force: Decimal | None = None,
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.PRESSURE_FORCE.value: lambda: mechanical_pressure * surface_area, #type: ignore
        QuantitiesNames.MECHANICAL_PRESSURE.value: lambda: pressure_force / surface_area, #type: ignore
        QuantitiesNames.SURFACE_AREA.value: lambda: pressure_force / mechanical_pressure, #type: ignore
    }

    try:
        raw_answer: Decimal = formulas_map[calculating_target]()
        cleaned_answer: str = f"{clean_trailing_zeros_from_decimal_number(decimal_number=raw_answer)}"

        calculations_result: tuple[bool, str] = (True, cleaned_answer)
        return calculations_result

    except (ZeroDivisionError, TypeError):
        calculations_result: tuple[bool, str] = (False, global_error_message)
        return calculations_result


def archimedes_law(
    *,
    calculating_target: str,
    archimedes_force: Decimal | None = None,
    fluid_density: Decimal | None = None,
    submerged_volume: Decimal | None = None,
    gravitational_acceleration: Decimal = PhysMathConstants.EARTH_GRAVITY_ACCELERATION.value,
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.ARCHIMEDES_FORCE.value: lambda: fluid_density * submerged_volume * gravitational_acceleration, #type: ignore
        QuantitiesNames.FLUID_DENSITY.value: lambda: archimedes_force / (submerged_volume * gravitational_acceleration), #type: ignore
        QuantitiesNames.SUBMERGED_VOLUME.value: lambda: archimedes_force / (fluid_density * gravitational_acceleration), #type: ignore
        QuantitiesNames.GRAVITATIONAL_ACCELERATION.value: lambda: archimedes_force / (fluid_density * submerged_volume), #type: ignore
    }
    
    try:
        raw_answer: Decimal = formulas_map[calculating_target]()
        cleaned_answer: str = f"{clean_trailing_zeros_from_decimal_number(decimal_number=raw_answer)}"

        calculations_result: tuple[bool, str] = (True, cleaned_answer)
        return calculations_result

    except (ZeroDivisionError, TypeError):
        calculations_result: tuple[bool, str] = (False, global_error_message)
        return calculations_result


def hydrostatic_pressure_law(
    *,
    calculating_target: str,
    hydrostatic_pressure: Decimal | None = None,
    fluid_density: Decimal | None = None,
    gravitational_acceleration: Decimal = PhysMathConstants.EARTH_GRAVITY_ACCELERATION.value,
    fluid_column_height: Decimal | None = None,
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.HYDROSTATIC_PRESSURE.value: lambda: fluid_density * gravitational_acceleration * fluid_column_height, #type: ignore
        QuantitiesNames.FLUID_DENSITY.value: lambda: hydrostatic_pressure / (gravitational_acceleration * fluid_column_height), #type: ignore
        QuantitiesNames.GRAVITATIONAL_ACCELERATION.value: lambda: hydrostatic_pressure / (fluid_density * fluid_column_height), #type: ignore
        QuantitiesNames.FLUID_COLUMN_HEIGHT.value: lambda: hydrostatic_pressure / (fluid_density * gravitational_acceleration), #type: ignore
    }

    try:
        raw_answer: Decimal = formulas_map[calculating_target]()
        cleaned_answer: str = f"{clean_trailing_zeros_from_decimal_number(decimal_number=raw_answer)}"

        calculations_result: tuple[bool, str] = (True, cleaned_answer)
        return calculations_result

    except (ZeroDivisionError, TypeError):
        calculations_result: tuple[bool, str] = (False, global_error_message)
        return calculations_result

#endregion
