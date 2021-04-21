from typing import BinaryIO

from PIL import Image
from pyzbar import pyzbar
from pyzbar.pyzbar import ZBarSymbol

from backend.exceptions import NoBarcodeFoundError

LEGAL_CODE_TYPES = [ZBarSymbol.EAN13, ZBarSymbol.ISBN10, ZBarSymbol.ISBN13]
ENCODING = "UTF-8"


def read_barcodes(image: Image) -> str:
    """
    Read barcodes from image.

    Args:
        image: Pillow Image.

    Returns:
        string representing ISBN. If on image there are multiple barcodes, first one which can be
        interpreted as book barcode is returned.

    Raises:
        NoBarcodeFoundError - if function does not found any barcode on image,

    """
    barcodes = pyzbar.decode(image, symbols=LEGAL_CODE_TYPES)

    if len(barcodes) == 0:
        raise NoBarcodeFoundError("No sufficient barcode found")

    else:
        return decode_binary_string(barcodes[0].data)


def decode_binary_string(binary_string: BinaryIO, encoding: str = ENCODING) -> str:
    """Encodes binary string.

    Args:
        binary_string: binary string representing ISBN,
        encoding: legal encoding type.

    Returns:
        Python string object representing ISBN.

    """
    return binary_string.decode(encoding)
