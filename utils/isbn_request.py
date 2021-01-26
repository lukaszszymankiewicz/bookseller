import requests

REQUEST_PREFIX = "https://openlibrary.org/isbn/"
REQUEST_SUFFIX = ".json"


def construct_url(isbn: str) -> str:
    return REQUEST_PREFIX + isbn + REQUEST_SUFFIX


def make_request_and_serialize_response(url: str) -> dict:
    return requests.get(url).json()
