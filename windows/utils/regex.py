import re
from typing import List


def run_substract_regex(regex_args: dict, text: str) -> str:
    return re.sub(**regex_args, string=text)


def clean_string_using_regexes(raw_string: str, cleaner_regexes: List[str]) -> str:
    string_cleaned = raw_string

    for cleaner_regex in cleaner_regexes:
        string_cleaned = run_substract_regex(regex_args=cleaner_regex, text=string_cleaned)

    return string_cleaned
