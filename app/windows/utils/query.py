import re

from .parsers import prices_search, sales_number_search
from .regex import clean_string_using_regexes
from .request import make_request, make_request_and_serialize_response
from .soup import create_soup
from .url_constructors import (construct_allegro_book_search_url,
                               construct_allegro_headers,
                               construct_openlibrary_author_search_url,
                               construct_openlibrary_isbn_search_url)

WHITESPACE_REGEX = {"pattern": r"\s+", "repl": "", "flags": re.UNICODE}
NONDIGITS_REGEX = {"pattern": "\D", "repl": ""}


def query_book_data(raw_string: str):
    code = clean_string_using_regexes(raw_string, [WHITESPACE_REGEX, NONDIGITS_REGEX])
    url = construct_openlibrary_isbn_search_url(code)
    data = make_request_and_serialize_response(url)
    headers = construct_allegro_headers()

    author_code = _extract_author_code(data)
    author_request_url = construct_openlibrary_author_search_url(author_code)
    author_data = make_request_and_serialize_response(author_request_url)

    author = _extract_author(author_data)
    title = _extract_title(data)

    allegro_url = construct_allegro_book_search_url(author, title)
    allegro_content = make_request(allegro_url, headers).content
    allegro_soup = create_soup(allegro_content)

    avg_price = prices_search(soup=allegro_soup)
    sales_number = sales_number_search(soup=allegro_soup)

    return {
        "title": title,
        "author": author,
        "avg_prices": str(round(avg_price, 2)) + " PLN",
        "sales_number": sales_number,
    }


def _extract_author(data: dict) -> str:
    return data.get("name")


def _extract_title(data: dict) -> str:
    raw_title = data.get("title")
    return raw_title.split(":")[0]


def _extract_author_code(data: dict) -> str:
    return data.get("authors")[0]["key"].replace("/authors/", "")
