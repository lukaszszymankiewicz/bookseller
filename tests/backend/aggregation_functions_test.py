import pytest

from backend.aggregation_functions import (avg_from_list, force_sum,
                                           force_to_float, force_to_int)


# fmt: off
@pytest.mark.parametrize(
    "input, expected_result",
    [
        (None     , 0),
        ([0]      , 0),
        ([1, 2, 3], 2),
    ]
)
# fmt: on
def test_avg_from_list_works_poperly(input, expected_result):
    # WHEN
    result = avg_from_list(input)

    # THEN
    assert result == expected_result


# fmt: off
@pytest.mark.parametrize(
    "input, expected_result",
    [
        (None , 0),
        (0.0  , 0),
        (1    , 1),
    ]
    )
# fmt: on
def test_force_to_int_works_poperly(input, expected_result):
    # WHEN
    result = force_to_int(input)

    # THEN
    assert result == expected_result


# fmt: off
@pytest.mark.parametrize(
    "input, expected_result",
    [
        (None , 0.0),
        (0    , 0.0),
        (1.0  , 1.0),
    ]
)
# fmt: on
def test_force_to_float_works_poperly(input, expected_result):
    # WHEN
    result = force_to_float(input)

    # THEN
    assert result == expected_result


# fmt: off
@pytest.mark.parametrize(
    "input, expected_result",
    [
        (None      , 0),
        ([0]       , 0),
        ([1, 2, 3] , 6),
    ]
)
# fmt: on
def test_force_sum_works_poperly(input, expected_result):
    # WHEN
    result = force_sum(input)

    # THEN
    assert result == expected_result
