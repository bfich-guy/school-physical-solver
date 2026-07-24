from decimal import Decimal, InvalidOperation
from typing import Callable, Any

from System.config import SystemConstants


#region User input validators

def is_user_input_valid_for_parsing(
    *,
    user_input: str,
    limit_length: int = SystemConstants.MAX_USER_INPUT_LENGTH.value,
    invalid_strings_list: list[str] = SystemConstants.INVALID_STRINGS_FOR_DECIMALING.value,
) -> bool:

    try:
        user_input_length: int = len(user_input)
        user_input_length_is_too_big: bool = user_input_length > limit_length

        if user_input_length_is_too_big:
            return False
            
        user_input_contains_invalid_words: bool = any(invalid_string in user_input for invalid_string in invalid_strings_list)

        if user_input_contains_invalid_words:
            return False

        user_input_does_not_contain_any_digits: bool = not any(character.isdigit() for character in user_input)

        if user_input_does_not_contain_any_digits:
            return False
        
    except (TypeError, AttributeError):
        return False
        
    return True

