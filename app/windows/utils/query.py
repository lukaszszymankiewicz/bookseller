from typing import Dict

from .request import make_request
from .schemas import AllegroSchema, BookSchema
from .url_constructors import (construct_allegro_book_search_url,
                               construct_openlibrary_search_url)


def query_title_and_author(isbn_string: str) -> Dict[str, str]:
    openlibrary_url = construct_openlibrary_search_url(isbn_string)

    return make_request(url=openlibrary_url, schema=BookSchema)


def query_avg_price_and_sold_copies(title: str, author: str) -> Dict[str, str]:
    allegro_url = construct_allegro_book_search_url(author, title)

    return make_request(url=allegro_url, schema=AllegroSchema)
