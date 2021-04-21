import re
from typing import List

WHITESPACE_REGEX = {"pattern": r"\s+", "repl": "", "flags": re.UNICODE}
NONDIGITS_REGEX = {"pattern": "\D", "repl": ""}


def run_substract_regex(regex_args: dict, text: str) -> str:
    """
    Runs regex on single string.

    Args:
        regex_args - dict with parameters to be put into re.sub function,
        text - string to be regexed.

    Retuns:
        regexed string.
    """
    return re.sub(**regex_args, string=text)


def clean_string_using_regexes(raw_string: str, cleaner_regexes: List[str]) -> str:
    """
    Perfromes multiple regex on string one after another.

    Args:
        raw_string - python string to be regexed,
        cleaner_regexes - list of regex to be performed on stirng.

    Retuns:
        regexed string.
    """
    string_cleaned = raw_string

    for cleaner_regex in cleaner_regexes:
        string_cleaned = run_substract_regex(regex_args=cleaner_regex, text=string_cleaned)

    return string_cleaned
