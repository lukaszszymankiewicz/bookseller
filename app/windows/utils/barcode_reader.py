from pyzbar import pyzbar


def read_barcodes(image):
    barcodes = pyzbar.decode(image)

    if len(barcodes) != 1:
        raise ValueError

    return int(barcodes[0].data)
