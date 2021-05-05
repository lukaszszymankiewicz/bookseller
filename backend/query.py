from typing import Dict

from .enums import ResponseFormat
from .request import ALLEGRO_HEADERS, make_request
from .schemas import AllegroSchema, BookfinderSchema, OpenlibarySchema
from .url_constructors import (construct_allegro_book_search_url,
                               construct_bookfinder_search_url,
                               construct_openlibrary_search_url)


def query_title_and_author_in_openlibrary(isbn_string: str) -> Dict[str, str]:
    url = construct_openlibrary_search_url(isbn_string)

    return make_request(
        url=url,
        schema=OpenlibarySchema,
        expected_response_format=ResponseFormat.json,
    )


def query_title_and_author_in_bookfinder(isbn_string: str) -> Dict[str, str]:
    url = construct_bookfinder_search_url(isbn_string)

    return make_request(url=url, schema=BookfinderSchema)


def query_avg_price_and_sold_copies(title: str, author: str) -> Dict[str, str]:
    url = construct_allegro_book_search_url(author, title)

    return make_request(
        url=url,
        schema=AllegroSchema,
        headers=ALLEGRO_HEADERS,
    )
