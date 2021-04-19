import os

import pytest

from backend.query import (query_avg_price_and_sold_copies,
                           query_title_and_author)

# TODO: move it to some more convinent place
os.environ["RUN_REQUESTS_AT_TEST"] = "False"


@pytest.mark.skipif(
    os.environ["RUN_REQUESTS_AT_TEST"] == "False", reason="requests test in pipelines only"
)
def test_query_title_and_author_works_properly():
    # GIVEN
    code = "978-1-491-91205-8"
    expected_title_and_author = {
        "title": "Python Data Science Handbook",
        "author": "Jake VanderPlas",
    }

    # WHEN
    title_and_author = query_title_and_author(code)

    # THEN
    assert title_and_author == expected_title_and_author


@pytest.mark.skipif(
    os.environ["RUN_REQUESTS_AT_TEST"] == "False", reason="requests test in pipelines only"
)
def test_query_avg_price_and_sold_copies_works_properly():
    # GIVEN
    title = "Python Data Science Handbook"
    author = "Jake VanderPlas"

    # WHEN
    avg_price_and_sold_copies = query_avg_price_and_sold_copies(title, author)

    # THEN
    assert "avg_prices" in avg_price_and_sold_copies.keys()
    assert "sold_copies" in avg_price_and_sold_copies.keys()
    assert isinstance(avg_price_and_sold_copies["avg_prices"], float)
    assert isinstance(avg_price_and_sold_copies["sold_copies"], int)
