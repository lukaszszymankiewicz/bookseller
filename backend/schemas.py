from abc import ABC, abstractstaticmethod

from .exceptions import (AllegroUnavailableError, BookNotFoundError,
                         WrongResponseError)
from .parsers import (author_search, prices_search, sales_number_search,
                      title_search)
from .soup import create_soup


class Schema(ABC):
    """Yeah. this is just placeholder for marshamallow or other json->object library."""

    @abstractstaticmethod
    def extract(data: dict) -> dict:
        pass


class BookfinderSchema(Schema):
    @staticmethod
    def extract(data: dict):
        if data == {}:
            raise BookNotFoundError("Book not found in Data Base :C")

        try:
            soup = create_soup(data)

            author = author_search(soup=soup)
            title = title_search(soup=soup)

            return {
                "author": author,
                "title": title,
            }

        except Exception:
            raise WrongResponseError("Something went wrong while querying ISBN")


class OpenlibarySchema(Schema):
    @staticmethod
    def extract(data: dict):
        if data == {}:
            raise BookNotFoundError("Book not found in Data Base :C")

        try:
            header = list(data.keys())[0]

            if len(data[header]["authors"]) == 0:
                author = "Unknown"
            else:
                author = data[header]["authors"][0]["name"]

            title = data[header]["title"]

        except Exception:
            raise WrongResponseError("Something went wrong while querying ISBN")

        return {
            "author": author,
            "title": title,
        }


class AllegroSchema(Schema):
    @staticmethod
    def extract(data: dict):

        if data == {}:
            raise AllegroUnavailableError("Allegro is unavailable.")

        try:
            allegro_soup = create_soup(data)

            avg_price = prices_search(soup=allegro_soup)
            sold_copies = sales_number_search(soup=allegro_soup)

            return {
                "avg_prices": round(avg_price, 2),
                "sold_copies": sold_copies,
            }

        except Exception:
            raise WrongResponseError("Something went wrong while querying Allegro")
