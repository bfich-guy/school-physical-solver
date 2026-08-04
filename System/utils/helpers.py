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
