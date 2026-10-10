from decimal import Decimal, InvalidOperation
from fastapi import FastAPI, APIRouter
from typing import Callable

from system.config.constants import ErrorMessages, InputMethod
from system.config.formulas import formulas_map

from system.utils.decimalhelpers import clean_trailing_zeros_from_decimal_number, get_decimal_numbers_from_user_input


def include_routers(
    *,
    app: FastAPI,
    routers_list: list[APIRouter],
) -> None:

    for router in routers_list:
        app.include_router(router=router)


def is_user_input_valid(
    *,
    user_input: str,
    input_limit: int = 64,
) -> bool:

    user_input_is_not_a_string: bool = not isinstance(user_input, str)

    if user_input_is_not_a_string:
        return False
    
    user_input_length: int = len(user_input)
    user_input_is_too_long: bool = user_input_length > input_limit

    if user_input_is_too_long:
        return False

    return True


def parse_user_input(
    *,
    user_input: list[Decimal],
    input_mode: str,
) -> list[Decimal] | Decimal:

    mode_map: dict = {
        InputMethod.SCALAR.value: lambda: user_input[0],
        InputMethod.VECTOR.value: lambda: user_input,
    }

    parsed_user_input: list[Decimal] | Decimal = mode_map[input_mode]()
    return parsed_user_input


def parse_quantities(
    *,
    quantities: dict,
) -> dict[str, Decimal | list[Decimal]] | None:

    parsed_quantities: dict[str, Decimal | list[Decimal]] = {}

    try:
        for quantity_name, quantity_data in quantities.items():
            quantity_value: str = quantity_data["value"]
            quantity_mode: str = quantity_data["mode"]

            quantity_value_is_not_valid: bool = not is_user_input_valid(user_input=quantity_value)

            if quantity_value_is_not_valid:
                return None
            
            decimaled_quantities: list[Decimal] = get_decimal_numbers_from_user_input(user_input=quantity_value)
            there_is_no_digit_in_the_input: bool = not decimaled_quantities

            if there_is_no_digit_in_the_input:
                return None
            
            parsed_quantity_value: list[Decimal] | Decimal = parse_user_input(user_input=decimaled_quantities, input_mode=quantity_mode)
            parsed_quantities[quantity_name] = parsed_quantity_value

        return parsed_quantities
    except (TypeError, KeyError):
        return None
    

def run_solver(
    *,
    formula: tuple,
    formulas_map: dict = formulas_map,
    quantities: dict,
) -> str:

    try:
        formula_solver: Callable = formulas_map[formula]
        formula_answer: list[Decimal] | Decimal = formula_solver(**quantities)

        formula_answer_is_vector: bool = isinstance(formula_answer, list)
        formula_answer_is_scalar: bool = isinstance(formula_answer, Decimal)

        if formula_answer_is_vector:
            stringified_answer: str = ", ".join([str(clean_trailing_zeros_from_decimal_number(decimal_number=decimal_number)) for decimal_number in formula_answer])
            return stringified_answer

        if formula_answer_is_scalar:
            stringified_answer = str(clean_trailing_zeros_from_decimal_number(decimal_number=formula_answer))
            return stringified_answer

        return ""

    except KeyError:
        return ErrorMessages.UNKNOWN_FORMULA.value
    except ValueError:
        return ErrorMessages.USER_INPUT.value
    except TypeError:
        return ErrorMessages.TECHNICAL.value
    except (ZeroDivisionError, InvalidOperation):
        return ErrorMessages.CALCULATIONS.value
