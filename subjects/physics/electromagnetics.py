from decimal import Decimal
from typing import Callable

from config import PhysMathConstants, QuantitiesNames, global_error_message

from utils import clean_trailing_zeros_from_decimal_number, decimal_product, decimal_power


#region Electricity

def ohms_specific_law(
    *,
    calculating_target: str,
    electric_voltage: Decimal | None = None,
    electric_current: Decimal | None = None,
    electric_resistance: Decimal | None = None,
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.ELECTRIC_VOLTAGE.value: lambda: electric_current * electric_resistance, #type: ignore
        QuantitiesNames.ELECTRIC_CURRENT.value: lambda: electric_voltage / electric_resistance, #type: ignore
        QuantitiesNames.ELECTRIC_RESISTANCE.value: lambda: electric_voltage / electric_current, #type: ignore
    }

    try:
        raw_answer: Decimal = formulas_map[calculating_target]()
        cleaned_answer: str = f"{clean_trailing_zeros_from_decimal_number(decimal_number=raw_answer)}"

        calculations_result: tuple[bool, str] = (True, cleaned_answer)
        return calculations_result

    except (ZeroDivisionError, TypeError):
        calculations_result: tuple[bool, str] = (False, global_error_message)
        return calculations_result    


def ohms_full_law(
    *,
    calculating_target: str,
    electromotive_force: Decimal | None = None,
    electric_voltage: Decimal | None = None,
    electric_current: Decimal | None = None,
    electric_internal_resistance: Decimal | None = None,
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.ELECTROMOTIVE_FORCE.value: lambda: electric_voltage + (electric_current * electric_internal_resistance), #type: ignore
        QuantitiesNames.ELECTRIC_VOLTAGE.value: lambda: electromotive_force - (electric_current * electric_internal_resistance), #type: ignore
        QuantitiesNames.ELECTRIC_CURRENT.value: lambda: (electromotive_force - electric_voltage) / electric_internal_resistance, #type: ignore
        QuantitiesNames.ELECTRIC_INTERNAL_RESISTANCE.value: lambda: (electromotive_force - electric_voltage) / electric_current, #type: ignore
    }

    try:
        raw_answer: Decimal = formulas_map[calculating_target]()
        cleaned_answer: str = f"{clean_trailing_zeros_from_decimal_number(decimal_number=raw_answer)}"

        calculations_result: tuple[bool, str] = (True, cleaned_answer)
        return calculations_result

    except (ZeroDivisionError, TypeError):
        calculations_result: tuple[bool, str] = (False, global_error_message)
        return calculations_result


def watts_law(
    *,
    calculating_target: str,
    electric_power: Decimal | None = None,
    electric_voltage: Decimal | None = None,
    electric_current: Decimal | None = None, 
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.ELECTRIC_POWER.value: lambda: electric_voltage * electric_current, #type: ignore
        QuantitiesNames.ELECTRIC_VOLTAGE.value: lambda: electric_power / electric_current, #type: ignore
        QuantitiesNames.ELECTRIC_CURRENT.value: lambda: electric_power / electric_voltage, #type: ignore
    }

    try:
        raw_answer: Decimal = formulas_map[calculating_target]()
        cleaned_answer: str = f"{clean_trailing_zeros_from_decimal_number(decimal_number=raw_answer)}"

        calculations_result: tuple[bool, str] = (True, cleaned_answer)
        return calculations_result

    except (ZeroDivisionError, TypeError):
        calculations_result: tuple[bool, str] = (False, global_error_message)
        return calculations_result


def joule_lenz_law(
    *,
    calculating_target: str,
    joule_heat: Decimal | None = None,
    electric_power: Decimal | None = None,
    heating_time: Decimal | None = None,
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.JOULE_HEAT.value: lambda: electric_power * heating_time, #type: ignore
        QuantitiesNames.ELECTRIC_POWER.value: lambda: joule_heat / heating_time, #type: ignore
        QuantitiesNames.HEATING_TIME.value: lambda: joule_heat / electric_power, #type: ignore
    }

    try:
        raw_answer: Decimal = formulas_map[calculating_target]()
        cleaned_answer: str = f"{clean_trailing_zeros_from_decimal_number(decimal_number=raw_answer)}"

        calculations_result: tuple[bool, str] = (True, cleaned_answer)
        return calculations_result

    except (ZeroDivisionError, TypeError):
        calculations_result: tuple[bool, str] = (False, global_error_message)
        return calculations_result


def coulombs_law(
    *,
    calculating_target: str,
    electrostatic_force: Decimal | None = None,
    coulomb_constant: Decimal = PhysMathConstants.COULOMB_CONSTANT.value,
    particle_charges: tuple[Decimal, Decimal] | None = None,
    particle_charge: Decimal | None = None,
    distance_between_charges: Decimal | None = None,
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.ELECTROSTATIC_FORCE.value: lambda: (coulomb_constant * decimal_product(particle_charges)) / decimal_power(distance_between_charges, Decimal("2")), #type: ignore
        QuantitiesNames.DISTANCE_BETWEEN_CHARGES.value: lambda: ((coulomb_constant * decimal_product(particle_charges)) / electrostatic_force).sqrt(), #type: ignore
        QuantitiesNames.PARTICLE_CHARGE.value: lambda: (electrostatic_force * decimal_power(distance_between_charges, Decimal("2"))) / (coulomb_constant * particle_charge), #type: ignore
    }

    try:
        raw_answer: Decimal = formulas_map[calculating_target]()
        cleaned_answer: str = f"{clean_trailing_zeros_from_decimal_number(decimal_number=raw_answer)}"

        calculations_result: tuple[bool, str] = (True, cleaned_answer)
        return calculations_result

    except (ZeroDivisionError, TypeError):
        calculations_result: tuple[bool, str] = (False, global_error_message)
        return calculations_result


def conductor_resistance_law(
    *,
    calculating_target: str,
    conductor_electric_resistance: Decimal | None = None,
    conductor_electric_resistivity: Decimal | None = None,
    conductor_length: Decimal | None = None,
    conductor_cross_sectional_area: Decimal | None = None,
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.CONDUCTOR_ELECTRIC_RESISTANCE.value: lambda: (conductor_electric_resistivity * conductor_length) / conductor_cross_sectional_area, #type: ignore
        QuantitiesNames.CONDUCTOR_ELECTRIC_RESISTIVITY.value: lambda: (conductor_electric_resistance * conductor_cross_sectional_area) / conductor_length, #type: ignore
        QuantitiesNames.CONDUCTOR_LENGTH.value: lambda: (conductor_electric_resistance * conductor_cross_sectional_area) / conductor_electric_resistivity, #type: ignore
        QuantitiesNames.CONDUCTOR_CROSS_SECTIONAL_AREA.value: lambda: (conductor_electric_resistivity * conductor_length) / conductor_electric_resistance, #type: ignore
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


#region Magnetism

def amperes_law(
    *,
    calculating_target: str,
    ampere_force: Decimal | None = None,
    electric_current: Decimal | None = None,
    magnetic_induction: Decimal | None = None,
    conductor_length: Decimal | None = None,
    angle_sinus: Decimal | None = None,   
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.AMPERES_FORCE.value: lambda: electric_current * magnetic_induction * conductor_length * angle_sinus, #type: ignore
        QuantitiesNames.ELECTRIC_CURRENT.value: lambda: ampere_force / (magnetic_induction * conductor_length * angle_sinus), #type: ignore
        QuantitiesNames.MAGNETIC_INDUCTION.value: lambda: ampere_force / (electric_current * conductor_length * angle_sinus), #type: ignore
        QuantitiesNames.CONDUCTOR_LENGTH.value: lambda: ampere_force / (electric_current * magnetic_induction * angle_sinus), #type: ignore
        QuantitiesNames.ANGLE_SINUS.value: lambda: ampere_force / (magnetic_induction * electric_current * conductor_length), #type: ignore
    }

    try:
        raw_answer: Decimal = formulas_map[calculating_target]()
        cleaned_answer: str = f"{clean_trailing_zeros_from_decimal_number(decimal_number=raw_answer)}"

        calculations_result: tuple[bool, str] = (True, cleaned_answer)
        return calculations_result

    except (ZeroDivisionError, TypeError):
        calculations_result: tuple[bool, str] = (False, global_error_message)
        return calculations_result


def lorentz_law(
    *,
    calculating_target: str,
    lorentz_force: Decimal | None = None,
    particle_charge: Decimal | None = None,
    particle_velocity: Decimal | None = None,
    magnetic_induction: Decimal | None = None,
    angle_sinus: Decimal | None = None,   
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.LORENTZ_FORCE.value: lambda: particle_charge * particle_velocity * magnetic_induction * angle_sinus, #type: ignore
        QuantitiesNames.PARTICLE_CHARGE.value: lambda: lorentz_force / (particle_velocity * magnetic_induction * angle_sinus), #type: ignore
        QuantitiesNames.PARTICLE_VELOCITY.value: lambda: lorentz_force / (particle_charge * magnetic_induction * angle_sinus), #type: ignore
        QuantitiesNames.MAGNETIC_INDUCTION.value: lambda: lorentz_force / (particle_charge * particle_velocity * angle_sinus), #type: ignore
        QuantitiesNames.ANGLE_SINUS.value: lambda: lorentz_force / (particle_charge * particle_velocity * magnetic_induction), #type: ignore
    }

    try:
        raw_answer: Decimal = formulas_map[calculating_target]()
        cleaned_answer: str = f"{clean_trailing_zeros_from_decimal_number(decimal_number=raw_answer)}"

        calculations_result: tuple[bool, str] = (True, cleaned_answer)
        return calculations_result

    except (ZeroDivisionError, TypeError):
        calculations_result: tuple[bool, str] = (False, global_error_message)
        return calculations_result


def faradays_law(
    *,
    calculating_target: str,
    delta_magnetic_flux: Decimal | None = None,
    electromotive_force: Decimal | None = None,
    delta_time: Decimal | None = None,
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.DELTA_MAGNETIC_FLUX.value: lambda: -(electromotive_force * delta_time), #type: ignore
        QuantitiesNames.PARTICLE_CHARGE.value: lambda: -(delta_magnetic_flux / delta_time), #type: ignore
        QuantitiesNames.PARTICLE_VELOCITY.value: lambda: -(delta_magnetic_flux / electromotive_force), #type: ignore
    }

    try:
        raw_answer: Decimal = formulas_map[calculating_target]()
        cleaned_answer: str = f"{clean_trailing_zeros_from_decimal_number(decimal_number=raw_answer)}"

        calculations_result: tuple[bool, str] = (True, cleaned_answer)
        return calculations_result

    except (ZeroDivisionError, TypeError):
        calculations_result: tuple[bool, str] = (False, global_error_message)
        return calculations_result


def magnetic_flux_law(
    *,
    calculating_target: str,
    magnetic_flux: Decimal | None = None,
    magnetic_induction: Decimal | None = None,
    contour_area: Decimal | None = None,
    angle_cosinus: Decimal | None = None,      
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.MAGNETIC_FLUX.value: lambda: magnetic_induction * contour_area * angle_cosinus, #type: ignore
        QuantitiesNames.MAGNETIC_INDUCTION.value: lambda: magnetic_flux / (contour_area * angle_cosinus), #type: ignore
        QuantitiesNames.CONTOUR_AREA.value: lambda: magnetic_flux / (magnetic_induction * angle_cosinus), #type: ignore
        QuantitiesNames.ANGLE_COSINUS.value: lambda: magnetic_flux / (magnetic_induction * contour_area), #type: ignore
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
