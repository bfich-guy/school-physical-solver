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

#endregion
