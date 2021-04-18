from PIL import Image
from pyzbar import pyzbar


def read_barcodes(image: Image):
    # TODO: add only EAN-13 code to be read!
    barcodes = pyzbar.decode(image)

    if len(barcodes) == 0:
        return None

    if len(barcodes) > 1:
        # TODO: check if any of codes is EAN-13

        import pdb

        pdb.set_trace()
        return [int(barcode.data) for barcode in barcodes]

    if len(barcodes) == 1:
        return int(barcodes[0].data)
