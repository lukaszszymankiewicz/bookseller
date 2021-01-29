import requests

REQUEST_PREFIX = "https://openlibrary.org"
REQUEST_SUFFIX = ".json"
ISBN_CODE = "isbn"
AUTHOR_CODE = "authors"

SEPARATOR = "/"


def construct_isbn_url(isbn: str) -> str:
    return REQUEST_PREFIX + SEPARATOR + ISBN_CODE + SEPARATOR + isbn + REQUEST_SUFFIX


def construct_author_request(author: str) -> dict:
    return REQUEST_PREFIX + SEPARATOR + AUTHOR_CODE + SEPARATOR + author + REQUEST_SUFFIX


def make_request_and_serialize_response(url: str) -> dict:
    return requests.get(url).json()
