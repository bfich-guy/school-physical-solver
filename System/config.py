from decimal import Decimal, DivisionByZero, InvalidOperation
from enum import Enum

#region Global constants

DECIMAL_ARRAY_VALID_TYPE: tuple = (list)
DECIMAL_FORMAT_MODE: str = "f"

PI: Decimal = Decimal("3.14159265358979")
DEFAULT_COSINUS_VALUE: Decimal = Decimal("0")
DEFAULT_SINUS_VALUE: Decimal = Decimal("1")

COLOUMB_CONSTANT: Decimal = Decimal("9000000000")
GRAVITATIONAL_ACCELERATION: Decimal = Decimal("10")

#endregion


#region Errors

class ErrorNames(Enum):
    ArrayIsNotDecimal = "ArrayIsNotDecimal"
    ZeroDivision = "ZeroDivision"
    NegativeRoot = "NegativeRoot"


class ErrorMessages(Enum):
    ArrayIsNotDecimal = "Для расчетов ожидались числа. Просим вас вводить числа. Для дробных чисел используйте точку. "
    ZeroDivision = "На ноль делить нельзя! Просим вас выбрать другой делитель, так как правила математики неизменяемы. "
    NegativeRoot = "Невозможно извлечь корень четной степени из отрицательного числа. Просим вас ввести неотрицательное число. "


error_dict: dict[str, str] = {

    ErrorNames.ArrayIsNotDecimal.value: ErrorMessages.ArrayIsNotDecimal.value,
    ErrorNames.ZeroDivision.value: ErrorMessages.ZeroDivision.value,
    ErrorNames.NegativeRoot.value: ErrorMessages.NegativeRoot.value,

}

#endregion
