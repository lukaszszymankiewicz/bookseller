import warnings

from utils import (NONDIGITS_REGEX, WHITESPACE_REGEX,
                   construct_allegro_search_url, create_soup, make_request)

from .htmlsearch import (number_of_result_pages, prices_search,
                         sales_number_search)
from .isbn_number import ISBNnumber


class Book:
    CLEANERS = [WHITESPACE_REGEX, NONDIGITS_REGEX]
    LEGAL_PREFIX = [978, 979]

    def __init__(self, raw_string: str, auto_request: bool = False):
        self.title = None
        self.author = None
        self.isbn = ISBNnumber(raw_string)
        self.requested = False

        if auto_request:
            self.get_book_data()

    def __len__(self):
        return len(self.code)

    @property
    def data(self):
        return {
            "isbn": self.code,
            "title": self.title,
            "author": self.author,
            "requested": self.requested,
        }

    def get_book_data(self):
        if self.requested:
            raise warnings.warn("Book data was requested already! Aborting!")
            return None

        isbn_data = self.isbn.get_book_data()
        self.author = isbn_data["author"]
        self.title = isbn_data["title"]

        allegro_url = construct_allegro_search_url(self.author, self.title)
        allegro_content = make_request(allegro_url)
        allegro_soup = create_soup(allegro_content.content)

        avg_prices = prices_search.search(allegro_soup)
        sales_number = sales_number_search.search(allegro_soup)
        n_pages = number_of_result_pages.search(allegro_soup)

        print(f"avg price: {avg_prices}")
        print(f"number: {sales_number}")
        print(f"number of results pages: {n_pages}")

        self.requested = True
