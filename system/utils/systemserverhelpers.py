from decimal import Decimal, InvalidOperation
from fastapi import FastAPI, APIRouter
from typing import Callable

from system.config.constants import calculations_error_message, unknown_formula_error_message, tecnical_error_message, FormulaMapData, InputMethod
from system.config.formulas import formulas_map

from system.utils.decimalhelpers import clean_trailing_zeros_from_decimal_number, get_decimal_numbers_from_user_input


def include_routers(
    *,
    app: FastAPI,
    routers_list: list[APIRouter],
) -> None:

    for router in routers_list:
        app.include_router(router=router)


def parse_quantities(
    *,
    formula: tuple,
    formulas_map: dict = formulas_map,
    raw_quantities: dict[str, str],
    length_limit: int = 64,
) -> dict[str, Decimal | list[Decimal]] | None:

    parsed_quantities: dict[str, Decimal | list[Decimal]] = {}

    for key, value in raw_quantities.items():
        try:
            value_is_not_string: bool = not isinstance(value, str)

            if value_is_not_string:
                return None

            value_length: int = len(value)
            value_is_too_long: bool = value_length > length_limit

            if value_is_too_long:
                return None

            cleaned_input: list[Decimal] = get_decimal_numbers_from_user_input(user_input=value)
            formula_method: str = formulas_map[formula][FormulaMapData.METHOD.value]

            formula_method_is_first_number: bool = formula_method == InputMethod.FIRST_NUMBER.value
            formula_method_is_all_numbers: bool = formula_method == InputMethod.ALL_NUMBERS.value

            if formula_method_is_first_number:
                cleaned_value: Decimal = cleaned_input[0]
                parsed_quantities[key] = cleaned_value

            if formula_method_is_all_numbers:
                parsed_quantities[key] = cleaned_input

        except IndexError:
            return None
        except KeyError:
            return None

    return parsed_quantities


def run_solver(
    *,
    formula: tuple,
    formulas_map: dict = formulas_map,
    quantities: dict,
) -> str:

    try:
        formula_function: Callable = formulas_map[formula][FormulaMapData.FUNCTION.value]
        formula_answer: Decimal | list[Decimal] = formula_function(**quantities)

        print("ANSWER:", formula_answer)

        formula_answer_is_single_number: bool = isinstance(formula_answer, Decimal)
        formula_answer_is_numbers_array: bool = isinstance(formula_answer, list)

        if formula_answer_is_single_number:
            stringified_answer = str(clean_trailing_zeros_from_decimal_number(decimal_number=formula_answer))
            return stringified_answer

        if formula_answer_is_numbers_array:
            stringified_answer = ", ".join([str(clean_trailing_zeros_from_decimal_number(decimal_number=decimal_number)) for decimal_number in formula_answer])
            return stringified_answer

        return tecnical_error_message
    
    except KeyError:
        return unknown_formula_error_message
    except TypeError:
        return tecnical_error_message
    except (ValueError, ZeroDivisionError, InvalidOperation):
        return calculations_error_message
    