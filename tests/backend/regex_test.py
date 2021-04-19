import re

import pytest

from backend.regex import (NONDIGITS_REGEX, WHITESPACE_REGEX,
                           clean_string_using_regexes, run_substract_regex)


# fmt: off
@pytest.mark.parametrize(
    "raw_string, expected_results, regex_fun",
    [
        ("     89          1 ", "891",  WHITESPACE_REGEX),
        ("1 89 \t\n      1"   , "1891", WHITESPACE_REGEX),
        ("891"                , "891",  WHITESPACE_REGEX),
        ("aa123bbcc"          , "123",  NONDIGITS_REGEX),
        ("-!123^&*%"          , "123",  NONDIGITS_REGEX),
        ("123"                , "123",  NONDIGITS_REGEX),
    ]
)
# fmt: on
def test_run_substract_regex_function_works_properly(raw_string, expected_results, regex_fun):
    # WHEN
    result = run_substract_regex(regex_fun, raw_string)

    # THEN
    assert result == expected_results


# fmt:off
@pytest.mark.parametrize(
    "raw_string, expected_results",
    [
        ("     89          1 ", "891"),
        ("1 89 \t\n      1"   , "1891"),
        ("891"                , "891"),
        ("aa123 bbcc   "      , "123"),
        ("-!123^&*%     "     , "123"),
        ("123"                , "123"),
    ]
)
# fmt: on
def test_clean_string_using_regexes_function_works_propely(raw_string, expected_results):
    # GIVEN
    cleaner_regexes = [WHITESPACE_REGEX, NONDIGITS_REGEX]

    # WHEN
    result = clean_string_using_regexes(raw_string, cleaner_regexes)

    # THEN
    assert result == expected_results
