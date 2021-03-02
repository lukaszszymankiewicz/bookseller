from .validation_message import ValidationMessage

LEGAL_PREFIX = [978, 979]

number = "9781617293702"


def number_is_proper_isbn_number(number: str):
    if len(number) == 13:
        prefix = int(number[:3])
    else:
        prefix = None

    control_number = int(number[-1])

    if len(number) == 13 and prefix not in LEGAL_PREFIX:
        return ValidationMessage(validated=False, message="this number has invalid prefix!")

    if len(number) == 10:
        control_sum = 0
        for index, number in enumerate(number[:-1]):
            control_sum += int(number) * index

        calculated_control_number = control_sum % 11

        if calculated_control_number != control_number:
            return ValidationMessage(validated=False, message="invalid ISBN")

    if len(number) == 13:
        control_sum = 0

        for index, number in enumerate(number):
            if index % 2 == 0:
                multiplier = 3
            else:
                multiplier = 1
            control_sum += int(number) * multiplier

        calculated_control_number = 10 - (control_sum % 10)

        if calculated_control_number != control_number:
            return ValidationMessage(validated=False, message="invalid ISBN")

    return ValidationMessage(validated=True)
