from pyzbar import pyzbar


def read_barcodes(image):
    barcodes = pyzbar.decode(image)

    if len(barcodes) == 0:
        return None

    if len(barcodes) > 1:
        return [int(barcode.data) for barcode in barcodes]

    if len(barcodes) == 1:
        return int(barcodes[0].data)
