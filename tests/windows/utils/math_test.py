from windows.utils.math import avg_from_list


def test_avg_from_list_works_poperly_for_zero_length_list():
    # GIVEN
    zero_length_list = []
    expected_result = 0

    # WHEN
    result = avg_from_list(zero_length_list)

    # THEN
    assert result == expected_result


def test_avg_from_list_works_poperly():
    # GIVEN
    sample_list = [1, 2, 3]
    expected_result = 2

    # WHEN
    result = avg_from_list(sample_list)

    # THEN
    assert result == expected_result
