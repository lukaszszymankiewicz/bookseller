from utils import construct_allegro_search_url


def test_allegro_request_construct_proper_url():
    # GIVEN
    sample_title = "Krzyżacy"
    sample_author = "Henryk Sienkiewicz"
    expected_url = "https://allegro.pl/kategoria/ksiazki-i-komiksy?string=Krzyżacy Henryk Sienkiewicz&offerTypeBuyNow=1&order=qd"

    # WHEN
    url = construct_allegro_search_url(sample_title, sample_author)

    # THEN
    assert url == expected_url
