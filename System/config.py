from decimal import Decimal, DivisionByZero, InvalidOperation
from enum import Enum


#region Global constants

class SystemConstants(Enum):
    DECIMAL_ITERABLE_OBJECT_VALID_TYPE = (list,)
    DECIMAL_FORMAT_MODE = "f"
    MAX_INPUT_LENGTH = 32
    VALID_DIGIT_CHARACTERS = "0123456789-."


class MathConstants(Enum):
    PI = Decimal("3.14159265358979")
    DEFAULT_COSINUS = Decimal("0")
    DEFAULT_SINUS = Decimal("1")


class PhysicsConstants(Enum):
    COLOUMB_CONSTANT = Decimal("9000000000")
    GRAVITATIONAL_ACCELERATION = Decimal("10")


class TextCharacters(Enum):
    COMMA = ","
    SPACE = " "
    DOT = "."


class ComparingMarks(Enum):
    LESS = "<"
    LESS_OR_EQUAL = "<="
    EQUAL = "=="
    GREATER_OR_EQUAL = ">="
    GREATER = ">"
    NOT_EQUAL = "!="

#endregion


#region Errors

class ErrorTypes(Enum):
    UNKNOWN_ERROR = "UNKNOWN"

    MATH_ERROR = "MATH_ERROR"
    LOGIC_ERROR = "LOGIC_ERROR"
    INPUT_ERROR = "INPUT_ERROR"


class ErrorMessages(Enum):
    UNKNOWN_ERROR = "Извините, произошла неизвестная ошибка."

    ZERO_DIVISION = "На ноль делить нельзя!"
    NEGATIVE_ROOT = "Подкоренное выражение отрицательным быть не может!"
    INCORRECT_INPUT = "На вход ожидалось одно число, не меньше и не больше!"


class Error():
    def __init__(self, *, error_type: str, error_message: str) -> None:
        self.error_type: str = error_type
        self.error_message: str = error_message

    def show(self) -> tuple:
        error_data: tuple = (self.error_type, self.error_message)
        return error_data

#endregion
