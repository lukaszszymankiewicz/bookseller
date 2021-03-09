from .validation_message import ValidationMessage

LEGAL_PREFIX = [978, 979]


def number_is_proper_isbn_number(number: str) -> ValidationMessage:
    if number[-1] == "X":
        control_number = 10
    else:
        control_number = int(number[-1])

    control_sum = 0

    if len(number) == 10:
        for index, number in enumerate(iterable=number[:-1], start=1):
            control_sum += int(number) * index

        calculated_control_number = control_sum % 11

        if calculated_control_number != control_number:
            return ValidationMessage(validated=False, message="wrong control sum")
        else:
            return ValidationMessage(validated=True)

    elif len(number) == 13:
        if int(number[:3]) not in LEGAL_PREFIX:
            return ValidationMessage(validated=False, message="this number has invalid prefix!")

        for index, digit in enumerate(iterable=number[:-1], start=1):
            if index % 2 == 0:
                multiplier = 3
            else:
                multiplier = 1
            control_sum += int(digit) * multiplier

        if (control_sum % 10) == 0:
            calculated_control_number = 0
        else:
            calculated_control_number = 10 - (control_sum % 10)

        if calculated_control_number != control_number:
            return ValidationMessage(validated=False, message="wrong control sum")
        else:
            return ValidationMessage(validated=True)

    else:
        return ValidationMessage(validated=False, message="wrong number length")
