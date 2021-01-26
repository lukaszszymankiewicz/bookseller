import pytest

from utils import NONDIGITS_REGEX, WHITESPACE_REGEX, run_substract_regex


class TestRegexUtilFunctions:
    # fmt:off
    @pytest.mark.parametrize(
        "raw_string, expected_code, regex_fun",
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
    def test_regexes_work_properly(self, raw_string, expected_code, regex_fun):
        # WHEN
        code = run_substract_regex(regex_fun, raw_string)

        # THEN
        assert code == expected_code
