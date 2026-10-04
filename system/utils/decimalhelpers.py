from decimal import Decimal, InvalidOperation


#region Decimal calculators

def decimal_sum(decimal_numbers: list[Decimal] | tuple[Decimal]) -> Decimal:
    decimal_sum = Decimal("0")

    for decimal_number in decimal_numbers:
        decimal_sum += decimal_number

    return decimal_sum


def decimal_product(decimal_numbers: list[Decimal] | tuple[Decimal]) -> Decimal:
    decimal_product = Decimal("1")

    for decimal_number in decimal_numbers:
        decimal_product *= decimal_number

    return decimal_product


def decimal_logarithm(decimal_value: Decimal, decimal_base: Decimal) -> Decimal:
    decimal_logarithm: Decimal = (decimal_value.ln() / decimal_base.ln()).quantize(Decimal("1"))
    return decimal_logarithm


def get_quadratic_equation_roots(
    *,
    a: Decimal,
    b: Decimal,
    c: Decimal,
) -> list[Decimal]:

    D: Decimal = ((b ** Decimal("2")) - ((Decimal("4") * a * c))).sqrt()

    x1: Decimal = (-b - D) / (Decimal("2") * a)
    x2: Decimal = (-b + D) / (Decimal("2") * a)

    quadratic_equation_roots: list[Decimal] = [x1, x2]
    return quadratic_equation_roots

#endregion


#region Decimal parsers

def clean_trailing_zeros_from_decimal_number(
    *,
    decimal_number: Decimal,
    format_mode: str = "f",
) -> Decimal:

    cleaned_decimal_number: Decimal = Decimal(format(decimal_number.normalize(), format_mode))
    return cleaned_decimal_number


def decimal_zip(list1: list[Decimal], list2: list[Decimal]) -> list:
    list1_length: int = len(list1)
    list2_length: int = len(list2)

    both_lists_are_empty: bool = not list1 and not list2
    lengths_are_mismached: bool = list1_length != list2_length

    if both_lists_are_empty or lengths_are_mismached:
        raise ValueError
    else:
        lists_zip: list = list(zip(list1, list2))
        return lists_zip


def get_decimal_numbers_from_user_input(
    *,
    user_input: str,
    valid_characters: str = "0123456789-.",
) -> list[Decimal]:

    valid_characters_matrix: list[list[str]] = []
    valid_characters_list: list[str] = []

    user_input_length: int = len(user_input)

    for index, character in enumerate(user_input):
        character_is_valid: bool = character in valid_characters

        if character_is_valid:
            valid_characters_list.append(character)
            cycle_is_over: bool = index == user_input_length - 1

            if cycle_is_over:
                valid_characters_matrix.append(valid_characters_list)
                valid_characters_list: list[str] = []

        else:
            valid_characters_list_is_empty: bool = not valid_characters_list

            if valid_characters_list_is_empty:
                continue

            valid_characters_matrix.append(valid_characters_list)
            valid_characters_list: list[str] = []

    decimal_numbers_list: list[Decimal] = []

    for valid_characters_list in valid_characters_matrix:
        potential_decimal_number: str = "".join(valid_characters_list)
    
        try:
            raw_decimal_number: Decimal = Decimal(potential_decimal_number)
            cleaned_decimal_number: Decimal = clean_trailing_zeros_from_decimal_number(decimal_number=raw_decimal_number)
            decimal_numbers_list.append(cleaned_decimal_number)
        except InvalidOperation:
            continue

    return decimal_numbers_list

#endregion
