from decimal import Decimal, InvalidOperation
from fastapi import FastAPI, APIRouter
from typing import Callable

from system.config.constants import ErrorMessages, InputMethod
from system.config.formulas import formulas_map

from system.utils.decimalhelpers import clean_decimal_number, get_decimal_numbers_from_user_input


def include_routers(
    *,
    app: FastAPI,
    routers: list[APIRouter],
) -> None:

    for router in routers:
        app.include_router(router=router)


def is_user_input_valid(
    *,
    user_input: str,
    input_limit: int = 16,
) -> bool:

    user_input_is_not_a_string: bool = not isinstance(user_input, str)

    if user_input_is_not_a_string:
        return False
    
    user_input_length: int = len(user_input)
    user_input_is_not_in_range: bool = user_input_length not in range(1, input_limit + 1)

    if user_input_is_not_in_range:
        return False

    return True


def parse_user_quantity_input(
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


def parse_user_formula_input(
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
            parsed_quantity_value: list[Decimal] | Decimal = parse_user_quantity_input(user_input=decimaled_quantities, input_mode=quantity_mode)
            parsed_quantities[quantity_name] = parsed_quantity_value

        return parsed_quantities
    except (TypeError, KeyError, IndexError):
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

        stringified_answer: str = ", ".join([str(clean_decimal_number(decimal_number=decimal_number)) for decimal_number in formula_answer]) if isinstance(formula_answer, list) else str(clean_decimal_number(decimal_number=formula_answer))
        return stringified_answer

    except KeyError:
        return ErrorMessages.UNKNOWN_FORMULA.value
    except ValueError:
        return ErrorMessages.USER_INPUT.value
    except TypeError:
        return ErrorMessages.TECHNICAL.value
    except (ZeroDivisionError, InvalidOperation):
        return ErrorMessages.CALCULATIONS.value
