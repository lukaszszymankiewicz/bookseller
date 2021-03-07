import pytest
from windows.utils.isbn_request import (construct_author_request,
                                        construct_isbn_url)


# fmt:off
@pytest.mark.parametrize(
    "isbn, expected_url",
    [
        ("9783161484100", "https://openlibrary.org/isbn/9783161484100.json"),
        ("9788310133748", "https://openlibrary.org/isbn/9788310133748.json"),
    ]
)
# fmt: on
def test_construct_isbn_url_construct_proper_url(isbn, expected_url):
    # WHEN
    url = construct_isbn_url(isbn)

    # THEN
    assert url == expected_url


# fmt:off
@pytest.mark.parametrize(
    "author, expected_url",
    [
        ("malcolmxd", "https://openlibrary.org/authors/malcolmxd.json"),
        ("rychupej", "https://openlibrary.org/authors/rychupeja.json"),
    ]
)
# fmt: on
def construct_author_request_construct_proper_url(author, expected_url):
    # WHEN
    url = construct_author_request(author)

    # THEN
    assert url == expected_url
