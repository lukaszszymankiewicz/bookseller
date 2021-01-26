import re

WHITESPACE_REGEX = {"pattern": r"\s+", "repl": "", "flags": re.UNICODE}
NONDIGITS_REGEX = {"pattern": "\D", "repl": ""}


def run_substract_regex(regex_args: dict, text: str) -> str:
    return re.sub(**regex_args, string=text)
