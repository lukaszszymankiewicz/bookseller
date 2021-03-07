import pytest
from windows.utils.allegro_request import construct_allegro_search_url


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
    url = construct_allegro_search_url(title, author)

    # THEN
    assert url == expected_url
