from typing import BinaryIO

from PIL import Image
from pyzbar import pyzbar
from pyzbar.pyzbar import ZBarSymbol

LEGAL_CODE_TYPES = [ZBarSymbol.EAN13, ZBarSymbol.ISBN13]
ENCODING = "UTF-8"


def read_barcodes(image: Image) -> str:
    """
    Read all barcode on inputted image.

    Args:
        image: Pillow Image format containing (or not barcode/s).

    Returns:
        string representing ISBN. If on image there are multiple barcodes, first one which can be
            interpreted as book barcode is returned. Of there is not any barcode None is returned.
    """
    barcodes = pyzbar.decode(image)

    if len(barcodes) == 0:
        return None

    if len(barcodes) > 1:

        for barcode in barcodes:
            if barcode.type == ZBarSymbol.EAN13:
                return decode_binary_string(barcode.data)
            elif barcode.type == ZBarSymbol.ISBN13:
                return decode_binary_string(barcode.data)
            elif barcode.type == ZBarSymbol.ISBN10:
                return decode_binary_string(barcode.data)
            else:
                return None

    if len(barcodes) == 1:
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
