import pytest
from windows.utils.url_constructors import (
    construct_allegro_book_search_url, construct_openlibrary_author_search_url,
    construct_openlibrary_isbn_search_url)


# fmt:off
@pytest.mark.parametrize(
    "title, author, expected_url",
    [
        (
            "Krzyżacy",
            "Henryk Sienkiewicz",
            "https://allegro.pl/kategoria/ksiazki-i-komiksy?string=Krzyżacy Henryk Sienkiewicz&offerTypeBuyNow=1&order=qd"
        ),
        (
            "Pan Tadeusz",
            "Adam Mickiewicz",
            "https://allegro.pl/kategoria/ksiazki-i-komiksy?string=Pan Tadeusz Adam Mickiewicz&offerTypeBuyNow=1&order=qd"
        ),
        (
            "Jebanie Policji",
            "Rychu Peja",
            "https://allegro.pl/kategoria/ksiazki-i-komiksy?string=Jebanie Policji Rychu Peja&offerTypeBuyNow=1&order=qd"
        ),
    ]
)
# fmt: on
def test_allegro_request_construct_proper_url(title, author, expected_url):
    # WHEN
    url = construct_allegro_book_search_url(title, author)

    # THEN
    assert url == expected_url


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
    url = construct_openlibrary_isbn_search_url(isbn)

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
    url = construct_openlibrary_author_search_url(author)

    # THEN
    assert url == expected_url
