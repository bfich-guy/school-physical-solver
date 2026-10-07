from fastapi import APIRouter
from fastapi.responses import JSONResponse
from decimal import Decimal

from system.config.constants import Prefix, Endpoints, CalculationSchema, ErrorMessages

from system.utils.systemserverhelpers import parse_quantities, run_solver


calculate_router = APIRouter(prefix=Prefix.INDEX.value)

@calculate_router.post(Endpoints.CALCULATE.value, response_class=JSONResponse)
def calculate(request: CalculationSchema) -> JSONResponse:

    answer: str = ErrorMessages.USER_INPUT.value

    formula: list = request.formula
    quantities: dict = request.quantities

    parsed_quantities: dict[str, Decimal | list[Decimal]] | None = parse_quantities(quantities=quantities)
    user_input_is_not_valid: bool = parsed_quantities == None

    if user_input_is_not_valid:
        json_responce = JSONResponse({"answer": answer})
        return json_responce

    tupled_formula = tuple(formula)
    answer: str = run_solver(formula=tupled_formula, quantities=parsed_quantities)
    json_responce = JSONResponse({"answer": answer})
    return json_responce
