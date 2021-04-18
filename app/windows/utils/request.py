import requests

from .schemas import Schema


def construct_headers() -> dict:
    return {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"
    }


def make_request(url: str, schema: Schema, headers: dict = None) -> dict:
    if not headers:
        headers = construct_headers()

    response = requests.get(url=url, headers=headers).json()

    return schema.extract(response)
