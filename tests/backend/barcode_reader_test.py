import pytest

from backend.barcode_reader import decode_binary_string, read_barcodes


@pytest.mark.parametrize(
    "img_number,expected_isbn_number",
    [
        (1, "9788386805433"),
        (2, "9788371500480"),
        (3, "9788328365032"),
        (4, "9788379670499"),
        (5, "9788363944667"),
    ],
)
def test_reach_barcodes_works_properly_for_prepared_images(
    img_number,
    expected_isbn_number,
    get_sample_image,
):
    # GIVEN
    sample_image = get_sample_image(img_number)

    # WHEN
    barcode = read_barcodes(sample_image)

    # THEN
    assert isinstance(barcode, str)
    assert barcode == expected_isbn_number


@pytest.mark.parametrize(
    "binary_string, expected_string",
    [
        (b"9788386805433", "9788386805433"),
        (b"9788371500480", "9788371500480"),
        (b"9788328365032", "9788328365032"),
        (b"9788379670499", "9788379670499"),
        (b"9788363944667", "9788363944667"),
    ],
)
def test_decode_binary_string_works_properly(binary_string, expected_string):
    # WHEN
    decoded_string = decode_binary_string(binary_string)

    # THEN
    assert isinstance(decoded_string, str)
    assert decoded_string == expected_string
