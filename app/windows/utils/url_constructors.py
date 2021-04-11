ALLEGRO_URL_PREFIX = "https://allegro.pl/"

OPENLIBRARY_URL_PREFIX = "https://openlibrary.org/api/books?bibkeys=ISBN:"
OPENLIBRARY_PARAM_SEPARATOR = "&"
OPENLIBRARY_FULLDATA_OPTION = "jscmd=data"
OPENLIBARY_FORMAT_AS_JSON_OPTION = "format=json"

SEPARATOR = "/"
ALLEGRO_CATEGORY_PREFIX = "kategoria"
ALLEGRO_BOOK_CATEGORY_NAME = "ksiazki-i-komiksy"
ALLEGRO_LIST_PREFIX = "listing"
ALLEGRO_SEARCH_BY_STRING_PREFIX = "?string"
ALLEGRO_BUYNOW_OPTION = "offerTypeBuyNow"
ALLEGRO_TRUE = "1"
ALLEGRO_EQUAL = "="
ALLEGRO_SPACE = " "
ALLEGRO_PARAM_SEPARATOR = "&"
ALLEGRO_SORTBY_OPTION = "order"
ALLEGRO_POPULARITY_OPTION = "qd"


def construct_allegro_book_search_url(author: str, title: str) -> str:
    return "".join(
        [
            ALLEGRO_URL_PREFIX,
            ALLEGRO_CATEGORY_PREFIX,
            SEPARATOR,
            ALLEGRO_BOOK_CATEGORY_NAME,
            ALLEGRO_SEARCH_BY_STRING_PREFIX,
            ALLEGRO_EQUAL,
            author,
            ALLEGRO_SPACE,
            title,
            ALLEGRO_PARAM_SEPARATOR,
            ALLEGRO_BUYNOW_OPTION,
            ALLEGRO_EQUAL,
            ALLEGRO_TRUE,
            ALLEGRO_PARAM_SEPARATOR,
            ALLEGRO_SORTBY_OPTION,
            ALLEGRO_EQUAL,
            ALLEGRO_POPULARITY_OPTION,
        ]
    )


def construct_allegro_headers() -> dict:
    """ Yeah, it is just copied from my browser XD"""

    return {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"
    }


def construct_openlibrary_search_url(isbn: str) -> str:
    return "".join(
        [
            OPENLIBRARY_URL_PREFIX,
            isbn,
            OPENLIBRARY_PARAM_SEPARATOR,
            OPENLIBRARY_FULLDATA_OPTION,
            OPENLIBRARY_PARAM_SEPARATOR,
            OPENLIBARY_FORMAT_AS_JSON_OPTION,
        ]
    )
