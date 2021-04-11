import os

import pytest
from app.windows.utils.query import (extract_author, extract_title,
                                     query_avg_price_and_sold_copies,
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


def test_extract_author_works_properly():
    # GIVEN
    expected_author = "Lukasz Luczaj"

    response = {
        "ISBN:9788310133748": {
            "url": "https://openlibrary.org/books/OL31959638M/Dzika_kuchnia",
            "key": "/books/OL31959638M",
            "title": "Dzika kuchnia",
            "authors": [
                {
                    "url": "https://openlibrary.org/authors/OL9104796A/Lukasz_Luczaj",
                    "name": "Lukasz Luczaj",
                }
            ],
            "number_of_pages": 320,
            "identifiers": {
                "isbn_10": ["831013374X"],
                "isbn_13": ["9788310133748"],
                "openlibrary": ["OL31959638M"],
            },
            "publishers": [{"name": "Nasza Ksiegarnia"}],
            "publish_date": "Feb 14, 2018",
            "cover": {
                "small": "https://covers.openlibrary.org/b/id/10639572-S.jpg",
                "medium": "https://covers.openlibrary.org/b/id/10639572-M.jpg",
                "large": "https://covers.openlibrary.org/b/id/10639572-L.jpg",
            },
        }
    }

    # WHEN
    author = extract_author(response)

    # THEN
    assert author == expected_author


def test_extract_title_works_properly():
    # GIVEN
    expected_title = "Dzika kuchnia"

    response = {
        "ISBN:9788310133748": {
            "url": "https://openlibrary.org/books/OL31959638M/Dzika_kuchnia",
            "key": "/books/OL31959638M",
            "title": "Dzika kuchnia",
            "authors": [
                {
                    "url": "https://openlibrary.org/authors/OL9104796A/Lukasz_Luczaj",
                    "name": "Lukasz Luczaj",
                }
            ],
            "number_of_pages": 320,
            "identifiers": {
                "isbn_10": ["831013374X"],
                "isbn_13": ["9788310133748"],
                "openlibrary": ["OL31959638M"],
            },
            "publishers": [{"name": "Nasza Ksiegarnia"}],
            "publish_date": "Feb 14, 2018",
            "cover": {
                "small": "https://covers.openlibrary.org/b/id/10639572-S.jpg",
                "medium": "https://covers.openlibrary.org/b/id/10639572-M.jpg",
                "large": "https://covers.openlibrary.org/b/id/10639572-L.jpg",
            },
        }
    }

    # WHEN
    title = extract_title(response)

    # THEN
    assert title == expected_title
