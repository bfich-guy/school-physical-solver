from fastapi import APIRouter
from fastapi.responses import JSONResponse
from decimal import Decimal

from system.config.constants import Prefix, Endpoints, CalculationSchema, user_input_error_message

from system.utils.systemserverhelpers import parse_quantities, run_solver


calculate_router = APIRouter(prefix=Prefix.INDEX.value)

@calculate_router.post(Endpoints.CALCULATE.value, response_class=JSONResponse)
def calculate(request: CalculationSchema) -> JSONResponse:

    answer: str | None = None

    formula: list[str] = request.formula
    quantities: dict[str, str] = request.quantities

    tupled_formula = tuple(formula)
    cleaned_quantities: dict[str, Decimal | list[Decimal]] | None = parse_quantities(formula=tupled_formula, raw_quantities=quantities)

    user_input_does_is_invalid: bool = cleaned_quantities is None

    if user_input_does_is_invalid:
        answer = user_input_error_message
    else:
        answer = run_solver(
            formula=tupled_formula,
            quantities=cleaned_quantities,
        )

    json_response: JSONResponse = JSONResponse(content={"answer": answer})
    return json_response
