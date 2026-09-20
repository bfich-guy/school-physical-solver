from decimal import Decimal
from enum import Enum


#region Global constants

class SystemConstants(Enum):
    DECIMAL_ITERABLE_OBJECT_VALID_TYPE = (list,)
    DECIMAL_FORMAT_MODE = "f"
    MAX_USER_INPUT_LENGTH = 32
    MAX_DECIMAL_LIST_LENGTH = 1
    VALID_DIGIT_CHARACTERS = "0123456789-."
    INTEGER_NUMBER = "INTEGER"
    FRACTION_NUMBER = "FRACTION"


class MathConstants(Enum):
    PI = Decimal("3.14")
    DEFAULT_COSINUS = Decimal("0")
    DEFAULT_SINUS = Decimal("1")


class PhysicsConstants(Enum):
    COLOUMB_CONSTANT = Decimal("9000000000")
    GRAVITATIONAL_ACCELERATION = Decimal("10")


class TextCharacters(Enum):
    COMMA = ","
    SPACE = " "
    DOT = "."


class Errors(Enum):
    UNKNOWN_ERROR = "Ошибка неизвестна"

    INVALID_USER_INPUT = f"Ожидался ввод в виде текста который не длиннее {SystemConstants.MAX_USER_INPUT_LENGTH.value} символов!"
    ZERO_DIVISION = "На ноль делить нельзя!"
    NEGATIVE_ROOT = "Подкоренное выражение не может быть отрицательным!"
    TRIANGLE_INEQUALITY_IS_BROKEN = "Неравенство треугольника не соблюдается!"

#endregion
