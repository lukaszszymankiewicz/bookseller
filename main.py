from PIL import Image
import re
import pytesseract
import requests

TESSERACT_CONFIG = "--psm 9 --oem 3 -c tessedit_char_whitelist=0123456789"

# FRONTEND (MOBILE APP)
def read_isbn_number_from_image(image_src: str):
    test_image = Image.open(image_src)
    return pytesseract.image_to_string(image=test_image, config=TESSERACT_CONFIG)


# BACKEND (REST API)
WHITESPACE_REGEX = {"pattern": r"\s+", "repl": "", "flags": re.UNICODE}
NONDIGITS_REGEX = {"pattern": "\D", "repl": ""}

REQUEST_PREFIX = "https://openlibrary.org/isbn/"
REQUEST_SUFFIX = ".json"


def construct_url(isbn: str):
    return REQUEST_PREFIX + isbn + REQUEST_SUFFIX


def make_request(url: str):
    return requests.get(request_url).txt


def get_book_data(isbn: str):
    url = construct_url(isbn)
    data = make_request(url)

    return data


def get_data_from_isbn(isbn: str):
    book_data = get_book_data
    return book_data


def get_metadata_from_isbn(isbn: str):
    # ISBN number should start from 978 lub 979
    # detect country
    # check checksum
    # WIP
    return None


def validate(isbn: str):
    if len(isbn) not in [10, 13]:
        raise ValueError("not valid ISBN number!")


def run_substract_regex(regex_args: dict, text: str):
    return re.sub(**regex_args, string=text)


def preprocess_text(isbn: str):
    isbn = run_substract_regex(WHITESPACE_REGEX, isbn)
    isbn = run_substract_regex(NONDIGITS_REGEX, isbn)

    validate(isbn)
    metadata = get_metadata_from_isbn(isbn)

    return isbn


# TEST
string_sample = read_isbn_number_from_image(image_src="test_picture.jpg")
isbn_number = preprocess_text(string_sample)
construct_request(isbn_number)
