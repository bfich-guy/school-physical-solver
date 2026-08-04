from enum import Enum

from system.config.constants import SystemConstants


#region Error messages

class Errors(Enum):
    INVALID_USER_INPUT = f"Ожидался ввод в виде текста который не длиннее {SystemConstants.MAX_USER_INPUT_LENGTH.value} символов!"
    ZERO_DIVISION = "На ноль делить нельзя!"
    NEGATIVE_ROOT = "Подкоренное выражение не может быть отрицательным!"
    TRIANGLE_INEQUALITY_IS_BROKEN = "Неравенство треугольника не соблюдается!"

#endregion
