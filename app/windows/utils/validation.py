LEGAL_PREFIX = [978, 979]


class ValidationMessage:
    def __init__(self, success: bool, content: dict = None):
        self.success = success
        self.content = content


def code_is_proper_isbn(code: str) -> ValidationMessage:
    """
    Function validates if inputted number is proper ISBN. Validation is checking both if number can
    be even considered as one (wrong length) with checking if number is properly constructed.

    For better readability and ability to testing, function is divided into smaller ones.

    Args:
        code: string representing number to validate.

    Returns:
        ValidationMessage instance with information if validation passed and optional message about
            why it failed.

    """
    if len(code) == 10:
        control_sum = 0

        for index, number in enumerate(iterable=code[:-1], start=1):
            control_sum += int(number) * index

        calculated_control_number = control_sum % 11

        if calculated_control_number != _control_number(code):
            return ValidationMessage(success=False, content="wrong control sum")
        else:
            return ValidationMessage(success=True, content="proper ISBN")

    elif len(code) == 13:
        control_sum = 0

        if _prefix(code) not in LEGAL_PREFIX:
            return ValidationMessage(success=False, content="this number has invalid prefix!")

        for index, digit in enumerate(iterable=code[:-1], start=1):
            if index % 2 == 0:
                multiplier = 3
            else:
                multiplier = 1
            control_sum += int(digit) * multiplier

        if (control_sum % 10) == 0:
            calculated_control_number = 0
        else:
            calculated_control_number = 10 - (control_sum % 10)

        if calculated_control_number != _control_number(code):
            return ValidationMessage(success=False, content="wrong control sum")
        else:
            return ValidationMessage(success=True, content="proper ISBN")

    elif len(code) < 10:
        return ValidationMessage(success=False, content="number is too short")

    elif len(code) > 13:
        return ValidationMessage(success=False, content="number is too long")

    else:
        return ValidationMessage(success=False, content="wrong number length")


def _prefix(code: str) -> int:
    return int(code[:3])


def _control_number(code: str) -> int:
    if code[-1] == "X":
        return 10
    else:
        return int(code[-1])
