from decimal import Decimal

#region Math validators

def compare_two_numbers(
    *,
    number_1: Decimal,
    number_2: Decimal,
    comparing_mark: str,
) -> bool:

    result_dict: dict[str, bool] = {
        "<": lambda: number_1 < number_2,
        "<=": lambda: number_1 <= number_2,
        "==": lambda: number_1 == number_2,
        ">=": lambda: number_1 >= number_2,
        ">": lambda: number_1 > number_2,
    }

    result: bool = result_dict[comparing_mark]
    return result

#endregion
