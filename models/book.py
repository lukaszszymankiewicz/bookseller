import warnings

from utils import (NONDIGITS_REGEX, WHITESPACE_REGEX, Rating,
                   construct_allegro_search_url, create_soup, make_request)

from .htmlsearch import (number_of_result_pages, prices_search,
                         sales_number_search)
from .isbn_number import ISBNnumber

# test it with: 9781449340377


class Book:
    CLEANERS = [WHITESPACE_REGEX, NONDIGITS_REGEX]
    LEGAL_PREFIX = [978, 979]

    def __init__(self, raw_string: str, auto_request: bool = False):
        self.isbn = ISBNnumber(raw_string)
        self.requested = False
        self.data = None

        if auto_request:
            self.get_book_data()

    def get_book_data(self):
        if self.requested:
            raise warnings.warn("Book data was requested already! Aborting!")
            return None

        isbn_data = self.isbn.get_book_data()
        author = isbn_data["author"]
        title = isbn_data["title"]

        allegro_url = construct_allegro_search_url(author, title)
        allegro_content = make_request(allegro_url)
        allegro_soup = create_soup(allegro_content.content)

        self.data = {
            "title": title,
            "author": author,
            "avg_prices": prices_search.search(allegro_soup),
            "sales_number": sales_number_search.search(allegro_soup),
            "n_pages": number_of_result_pages.search(allegro_soup),
        }

        self.requested = True

    def calculate_score(self):
        if not self.requested:
            raise warnings.warn("Book data wasn`t requested yet! Aborting!")
            return None

        if self.data["sales_number"] == 0:
            return Rating.unsellable

        elif self.data["sales_number"] > 5 and self.data["avg_prices"] > 10:
            return Rating.promising

        elif self.data["sales_number"] > 10 and self.data["avg_prices"] > 20:
            return Rating.worth_it

        elif self.data["sales_number"] > 20 and self.data["avg_prices"] > 30:
            return Rating.treasure
