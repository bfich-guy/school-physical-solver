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

UNKNOWN_ERROR_TYPE: str = "UNKNOWN"
UNKNOWN_ERROR_MESSAGE: str = "ERROR ITSELF IS UNKNOWN"


class ErrorTypes(Enum):
    MathError = "MATH_ERROR"
    LogicError = "LOGIC_ERROR"


class ErrorMessages(Enum):
    ZeroDivision = "На ноль делить нельзя!"
    NegativeRoot = "Подкоренное выражение отрицательным быть не может!"


class Error(Exception):
    def __init__(self, *, error_type: str, error_message: str) -> None:
        super().__init__(error_type, error_message)
        self.error_type: str = error_type
        self.error_message: str = error_message


    def show(self) -> str:
        error_text: str = f"[{self.error_type}]: {self.error_message}"
        return error_text

#endregion
