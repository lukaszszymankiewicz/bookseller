ALLEGRO_PREFIX = "https://allegro.pl/"
DELIMETER = "/"
CATEGORY_PREFIX = "kategoria"
BOOK_CATEGORY = "ksiazki-i-komiksy"
LIST_PREFIX = "listing"
SEARCH_BY_STRING = "?string"
BUYNOW_OPTION = "offerTypeBuyNow"
YES = "1"
EQUAL = "="
SPACE = " "
PARAM_DELIMETER = "&"
SORT_BY = "order"
POPULARITY = "qd"


def construct_allegro_search_url(author: str, title: str) -> str:
    return "".join(
        [
            ALLEGRO_PREFIX,
            CATEGORY_PREFIX,
            DELIMETER,
            BOOK_CATEGORY,
            SEARCH_BY_STRING,
            EQUAL,
            author,
            SPACE,
            title,
            PARAM_DELIMETER,
            BUYNOW_OPTION,
            EQUAL,
            YES,
            PARAM_DELIMETER,
            SORT_BY,
            EQUAL,
            POPULARITY,
        ]
    )