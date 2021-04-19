import pytest

from backend.url_constructors import (construct_allegro_book_search_url,
                                      construct_openlibrary_search_url)


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


@pytest.mark.parametrize(
    "isbn, expected_url",
    [
        (
            "0201558025",
            "https://openlibrary.org/api/books?bibkeys=ISBN:0201558025&jscmd=data&format=json",
        ),
        (
            "9788310133748",
            "https://openlibrary.org/api/books?bibkeys=ISBN:9788310133748&jscmd=data&format=json",
        ),
    ],
)
def test_construct_openlibrary_search_url_fun_construct_proper_url(isbn, expected_url):
    # WHEN
    url = construct_openlibrary_search_url(isbn)

    # THEN

    assert url == expected_url
