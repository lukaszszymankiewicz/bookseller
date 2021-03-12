def avg_from_list(x):
    if not x:
        return 0
    if len(x) == 0:
        return 0
    else:
        return sum(x) // len(x)


def force_to_int(value):
    if not value:
        return 0
    else:
        return int(value)


def force_to_float(value):
    if not value:
        return 0
    else:
        return float(value)


def force_sum(x):
    if not x:
        return 0
    if len(x) == 0:
        return 0
    else:
        return sum(x)
