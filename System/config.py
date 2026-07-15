from decimal import Decimal, DivisionByZero, InvalidOperation
from enum import Enum

#region Global constants

class SystemConstants(Enum):
    DECIMAL_ARRAY_VALID_TYPE = (list,)
    DECIMAL_FORMAT_MODE = "f"


class MathConstants(Enum):
    PI = Decimal("3.14159265358979")
    DEFAULT_COSINUS = Decimal("0")
    DEFAULT_SINUS = Decimal("1")


class PhysicsConstants(Enum):
    COLOUMB_CONSTANT = Decimal("9000000000")
    GRAVITATIONAL_ACCELERATION = Decimal("10")


class TextConstants(Enum):
    COMMA = ","
    SPACE = " "

#endregion


#region Errors

class ErrorTypes(Enum):
    UNKNOWN_ERROR = "UNKNOWN"

    MATH_ERROR = "MATH_ERROR"
    LOGIC_ERROR = "LOGIC_ERROR"


class ErrorMessages(Enum):
    UNKNOWN_ERROR = "Извините, произошла неизвестная ошибка."

    ZERO_DIVISION = "На ноль делить нельзя!"
    NEGATIVE_ROOT = "Подкоренное выражение отрицательным быть не может!"


class Error(Exception):
    def __init__(self, *, error_type: str, error_message: str) -> None:
        super().__init__(error_type, error_message)
        self.error_type: str = error_type
        self.error_message: str = error_message

    def show(self) -> str:
        error_data: tuple = (self.error_type, self.error_message)
        return error_data

#endregion
