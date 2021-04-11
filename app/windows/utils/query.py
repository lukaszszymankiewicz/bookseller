import re
from typing import Dict

from .parsers import prices_search, sales_number_search
from .regex import clean_string_using_regexes
from .request import make_request, make_request_and_serialize_response
from .soup import create_soup
from .url_constructors import (construct_allegro_book_search_url,
                               construct_allegro_headers,
                               construct_openlibrary_search_url)

# TODO: maybe move it to regex module diectly?
WHITESPACE_REGEX = {"pattern": r"\s+", "repl": "", "flags": re.UNICODE}
NONDIGITS_REGEX = {"pattern": "\D", "repl": ""}


def query_title_and_author(raw_isbn_string: str) -> Dict[str, str]:
    isbn_string = clean_string_using_regexes(raw_isbn_string, [WHITESPACE_REGEX, NONDIGITS_REGEX])
    openlibrary_url = construct_openlibrary_search_url(isbn_string)
    data = make_request_and_serialize_response(openlibrary_url)

    return {"title": extract_title(data), "author": extract_author(data)}


def query_avg_price_and_sold_copies(title: str, author: str) -> Dict[str, str]:
    headers = construct_allegro_headers()
    allegro_url = construct_allegro_book_search_url(author, title)
    allegro_content = make_request(allegro_url, headers).content
    allegro_soup = create_soup(allegro_content)

    avg_price = prices_search(soup=allegro_soup)
    sold_copies = sales_number_search(soup=allegro_soup)

    return {
        "avg_prices": round(avg_price, 2),
        "sold_copies": sold_copies,
    }


def extract_author(data: dict) -> str:
    isbns = list(data.keys())[0]

    # TODO: add moe authors options
    return data[isbns].get("authors")[0].get("name")


def extract_title(data: dict) -> str:
    isbns = list(data.keys())[0]

    return data[isbns].get("title")
