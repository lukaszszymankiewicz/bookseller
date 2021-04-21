import requests

from .enums import ResponseFormat
from .exceptions import AllegroUnavailableError, NoInternetConnectionError
from .schemas import Schema

ALLEGRO_HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0",
    "Host": "allegro.pl",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://allegro.pl/",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
}

DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0",
}


def make_request(
    url: str,
    schema: Schema,
    expected_response_format: str = ResponseFormat.raw,
    headers: dict = None,
) -> dict:
    if not headers:
        headers = DEFAULT_HEADERS

    response = requests.get(url=url, headers=headers)

    if response.status_code != 200:
        raise AllegroUnavailableError("Allegro unavailable!")

    if expected_response_format == ResponseFormat.json:
        formatted_response = response.json()
    else:
        formatted_response = response.content

    result = schema.extract(formatted_response)

    return result
