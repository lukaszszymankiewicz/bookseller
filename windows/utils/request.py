import requests


def make_request_and_serialize_response(url: str) -> dict:
    return requests.get(url).json()


def make_request(url: str) -> dict:
    return requests.get(url)
