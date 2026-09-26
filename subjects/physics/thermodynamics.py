from decimal import Decimal
from typing import Callable

from config import PhysMathConstants, QuantitiesNames, global_error_message

from utils import clean_trailing_zeros_from_decimal_number


#region Classic thermodynamics

def sensible_heat_law(
    *,
    calculating_target: str,
    sensible_heat: Decimal | None = None,
    specific_heat: Decimal | None = None,
    object_mass: Decimal | None = None,
    delta_temperature: Decimal | None = None,
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.SPECIFIC_HEAT.value: lambda: specific_heat * object_mass * delta_temperature, #type: ignore
        QuantitiesNames.SPECIFIC_HEAT.value: lambda: sensible_heat / (object_mass * delta_temperature), #type: ignore
        QuantitiesNames.OBJECT_MASS.value: lambda: sensible_heat / (specific_heat * delta_temperature), #type: ignore
        QuantitiesNames.DELTA_TEMPERATURE.value: lambda: sensible_heat / (specific_heat * object_mass), #type: ignore
    }

    try:
        raw_answer: Decimal = formulas_map[calculating_target]()
        cleaned_answer: str = f"{clean_trailing_zeros_from_decimal_number(decimal_number=raw_answer)}"

        calculations_result: tuple[bool, str] = (True, cleaned_answer)
        return calculations_result

    except (ZeroDivisionError, TypeError):
        calculations_result: tuple[bool, str] = (False, global_error_message)
        return calculations_result


def combustion_heat_law(
    *,
    calculating_target: str,
    combustion_heat: Decimal | None = None,
    specific_heat_of_combustion: Decimal | None = None,
    object_mass: Decimal | None = None,
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.COMBUSTION_HEAT.value: lambda: specific_heat_of_combustion * object_mass, #type: ignore
        QuantitiesNames.SPECIFIC_HEAT_OF_COMBUSTION.value: lambda: combustion_heat / object_mass, #type: ignore
        QuantitiesNames.OBJECT_MASS.value: lambda: combustion_heat / specific_heat_of_combustion, #type: ignore
    }

    try:
        raw_answer: Decimal = formulas_map[calculating_target]()
        cleaned_answer: str = f"{clean_trailing_zeros_from_decimal_number(decimal_number=raw_answer)}"

        calculations_result: tuple[bool, str] = (True, cleaned_answer)
        return calculations_result

    except (ZeroDivisionError, TypeError):
        calculations_result: tuple[bool, str] = (False, global_error_message)
        return calculations_result


def fusion_heat_law(
    *,
    calculating_target: str,
    fusion_heat: Decimal | None = None,
    specific_heat_of_fusion: Decimal | None = None,
    object_mass: Decimal | None = None,
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.FUSION_HEAT.value: lambda: specific_heat_of_fusion * object_mass, #type: ignore
        QuantitiesNames.SPECIFIC_HEAT_OF_FUSION.value: lambda: fusion_heat / object_mass, #type: ignore
        QuantitiesNames.OBJECT_MASS.value: lambda: fusion_heat / specific_heat_of_fusion, #type: ignore
    }

    try:
        raw_answer: Decimal = formulas_map[calculating_target]()
        cleaned_answer: str = f"{clean_trailing_zeros_from_decimal_number(decimal_number=raw_answer)}"

        calculations_result: tuple[bool, str] = (True, cleaned_answer)
        return calculations_result

    except (ZeroDivisionError, TypeError):
        calculations_result: tuple[bool, str] = (False, global_error_message)
        return calculations_result


def vaporization_heat_law(
    *,
    calculating_target: str,
    vaporization_heat: Decimal | None = None,
    specific_heat_of_vaporization: Decimal | None = None,
    object_mass: Decimal | None = None,
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.VAPORIZATION_HEAT.value: lambda: specific_heat_of_vaporization * object_mass, #type: ignore
        QuantitiesNames.SPECIFIC_HEAT_OF_VAPORIZATION.value: lambda: vaporization_heat / object_mass, #type: ignore
        QuantitiesNames.OBJECT_MASS.value: lambda: vaporization_heat / specific_heat_of_vaporization, #type: ignore
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


#region Molecular kinetic theory

def mendeleev_clayperon_law(
    *,
    calculating_target: str,
    gas_pressure: Decimal | None = None,
    gas_volume: Decimal | None = None,
    gas_moles: Decimal | None = None,
    gas_constant: Decimal = PhysMathConstants.GAS_CONSTANT.value,
    gas_temperature: Decimal | None = None,     
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.GAS_PRESSURE.value: lambda: (gas_moles * gas_constant * gas_temperature) / gas_volume, #type: ignore
        QuantitiesNames.GAS_VOLUME.value: lambda: (gas_moles * gas_constant * gas_temperature) / gas_pressure, #type: ignore
        QuantitiesNames.GAS_MOLES.value: lambda: (gas_pressure * gas_volume) / (gas_constant * gas_temperature), #type: ignore
        QuantitiesNames.GAS_TEMPERATURE.value: lambda: (gas_pressure * gas_volume) / (gas_constant * gas_moles), #type: ignore
    }

    try:
        raw_answer: Decimal = formulas_map[calculating_target]()
        cleaned_answer: str = f"{clean_trailing_zeros_from_decimal_number(decimal_number=raw_answer)}"

        calculations_result: tuple[bool, str] = (True, cleaned_answer)
        return calculations_result

    except (ZeroDivisionError, TypeError):
        calculations_result: tuple[bool, str] = (False, global_error_message)
        return calculations_result


def molar_mass_law(
    *,
    calculating_target: str,
    object_moles: Decimal | None = None,
    object_mass: Decimal | None = None,
    object_molar_mass: Decimal | None = None,
) -> tuple[bool, str]:

    formulas_map: dict[str, Callable[[], Decimal]] = {
        QuantitiesNames.OBJECT_MASS.value: lambda: object_moles * object_molar_mass, #type: ignore
        QuantitiesNames.OBJECT_MOLAR_MASS.value: lambda: object_mass / object_molar_mass, #type: ignore
        QuantitiesNames.OBJECT_MOLES.value: lambda: object_mass / object_moles, #type: ignore
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
