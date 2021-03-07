import pytest
from windows.utils.parsers import (number_of_result_pages, prices_search,
                                   sales_number_search)


# fmt:off
@pytest.mark.parametrize(
    "soup_number, expected_number_of_results_pages",
    [
        (1, 68),
        (2, 68),
        (3, 0),
    ]
)
# fmt: on
def test_number_of_result_pages_works_properly(
    soup_number,
    expected_number_of_results_pages,
    get_pickled_soup,
):
    # GIVEN
    soup = get_pickled_soup(soup_number)

    # WHEN
    parsed_number_of_results_pages = number_of_result_pages(soup=soup)

    # THEN
    assert parsed_number_of_results_pages == expected_number_of_results_pages


# fmt:off
@pytest.mark.parametrize(
    "soup_number, expected_avg_price",
    [
        (1, 19.0),
        (2, 28.0),
        (3, 0.0),
    ]
)
# fmt: on
def test_prices_search_works_properly(
    soup_number,
    expected_avg_price,
    get_pickled_soup,
):
    # GIVEN
    soup = get_pickled_soup(soup_number)

    # WHEN
    parsed_avg_price = prices_search(soup=soup)

    # THEN
    assert parsed_avg_price == expected_avg_price


# fmt:off
@pytest.mark.parametrize(
    "soup_number, expected_sales_number",
    [
        (1, 162),
        (2, 515),
        (3, 0.0),
    ]
)
# fmt: on
def test_sales_number_search_works_properly(
    soup_number,
    expected_sales_number,
    get_pickled_soup,
):
    # GIVEN
    soup = get_pickled_soup(soup_number)

    # WHEN
    parsed_avg_price = sales_number_search(soup=soup)

    # THEN
    assert parsed_avg_price == expected_sales_number
