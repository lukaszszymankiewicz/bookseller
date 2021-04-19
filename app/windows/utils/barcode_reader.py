from PIL import Image
from pyzbar import pyzbar
from pyzbar.pyzbar import ZBarSymbol

LEGAL_CODE_TYPES = [ZBarSymbol.EAN13, ZBarSymbol.ISBN13]


def read_barcodes(image: Image):
    barcodes = pyzbar.decode(image)

    if len(barcodes) == 0:
        return None

    if len(barcodes) > 1:
        print(barcodes)
        for barcode in barcodes:
            if barcode.type == ZBarSymbol.EAN13:
                return barcode.data.decode("UTF-8")
            elif barcode.type == ZBarSymbol.ISBN13:
                return barcode.data.decode("UTF-8")
            elif barcode.type == ZBarSymbol.ISBN10:
                return barcode.data.decode("UTF-8")
            else:
                return None

    if len(barcodes) == 1:
        return barcodes[0].data.decode("UTF-8")
