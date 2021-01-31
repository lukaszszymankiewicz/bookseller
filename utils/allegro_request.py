#  https://allegro.pl/listing?string=henryk%20sienkiewicz%20krzy%C5%BCacy&offerTypeBuyNow=1&bmatch=cx210105ap-enomswp-diwebp-cul-1-3-0129
ALLEGRO_PREFIX = "https://allegro.pl/"
LIST_PREFIX = "listing"
SEARCH_BY_STRING = "?string"
BUYNOW_OPTION = "offerTypeBuyNow"
YES = "1"
EQUAL = "="
SPACE = " "
PARAM_DELIMETER = "&"


def construct_allegro_search_url(author: str, title: str) -> str:
    return "".join(
        [
            ALLEGRO_PREFIX,
            LIST_PREFIX,
            SEARCH_BY_STRING,
            EQUAL,
            author,
            SPACE,
            title,
            PARAM_DELIMETER,
            BUYNOW_OPTION,
            EQUAL,
            YES,
        ]
    )


title = "Krzyżacy"
author = "Henryk Sienkiewicz"
url = construct_allegro_search_url(author, title)
print(url)
