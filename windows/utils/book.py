import re

from .allegro_request import construct_allegro_search_url
from .isbn_request import construct_author_request, construct_isbn_url
from .parsers import prices_search, sales_number_search
from .query_message import QueryMessage
from .regex import clean_string_using_regexes
from .request import make_request, make_request_and_serialize_response
from .soup import create_soup

WHITESPACE_REGEX = {"pattern": r"\s+", "repl": "", "flags": re.UNICODE}
NONDIGITS_REGEX = {"pattern": "\D", "repl": ""}


def get_book_data(raw_string: str):
    try:
        code = clean_string_using_regexes(raw_string, [WHITESPACE_REGEX, NONDIGITS_REGEX])

        url = construct_isbn_url(code)
        data = make_request_and_serialize_response(url)

        author_code = _extract_author_code(data)
        author_request_url = construct_author_request(author_code)
        author_data = make_request_and_serialize_response(author_request_url)

        author = _extract_author(author_data)
        title = _extract_title(data)

        allegro_url = construct_allegro_search_url(author, title)
        allegro_content = make_request(allegro_url)
        allegro_soup = create_soup(allegro_content.content)

        avg_price = prices_search(soup=allegro_soup)
        sales_number = sales_number_search(soup=allegro_soup)

    except Exception as e:
        return QueryMessage(completed=False, message=e)

    else:
        return QueryMessage(
            completed=True,
            message={
                "title": title,
                "author": author,
                "avg_prices": avg_price,
                "sales_number": sales_number,
            },
        )


def _extract_author(data: dict) -> str:
    return data.get("name")


def _extract_title(data: dict) -> str:
    raw_title = data.get("title")
    return raw_title.split(":")[0]


def _extract_author_code(data: dict) -> str:
    return data.get("authors")[0]["key"].replace("/authors/", "")
