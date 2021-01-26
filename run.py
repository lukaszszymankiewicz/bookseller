import pytesseract
from PIL import Image

from models import Book

TESSERACT_CONFIG = "--psm 9 --oem 3 -c tessedit_char_whitelist=0123456789"


# FRONTEND (MOBILE APP)
def read_isbn_number_from_image(image_src: str):
    test_image = Image.open(image_src)
    return pytesseract.image_to_string(image=test_image, config=TESSERACT_CONFIG)


if __name__ == "__main__":
    isbn_number = read_isbn_number_from_image("test_picture.jpg")
    book = Book(isbn_number)
