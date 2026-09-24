from decimal import Decimal

from system.config.constants import SystemConstants


#region Number helpers

def clean_trailing_zeros_from_decimal_number(
    *,
    decimal_number: Decimal,
    format_mode: str = SystemConstants.DECIMAL_FORMAT_MODE.value,
) -> Decimal:

    cleaned_decimal_number: Decimal = Decimal(format(decimal_number.normalize(), format_mode))
    return cleaned_decimal_number

#endregion


def pydantic_schemas_factory(
    *,
    function_name: str,
) -> None:

    pydantic_schema_name: str = f"class {"".join([word.capitalize() for word in function_name.split("_")])}(BaseModel):"
    pydantic_fields: list[str] = function_name.split("_by_")[1].split("_and_")

    print(pydantic_schema_name)

    for pydantic_field in pydantic_fields:
        print(f"    {pydantic_field}: str")

    print("")
    print("")


functions_names: list[str] = [
    
]

for function_name in functions_names:
    pydantic_schemas_factory(function_name=function_name)

"python -m system.utils.helpers"