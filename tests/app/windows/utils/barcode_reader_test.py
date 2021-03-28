import pytest
from app.windows.utils.barcode_reader import read_barcodes


@pytest.mark.parametrize(
    "img_number,expected_isbn_number",
    [
        (1, 9788386805433),
        (2, 9788371500480),
        (3, 9788328365032),
        (4, 9788379670499),
        (5, 9788363944667),
    ],
)
def test_reach_barcodes_works_properly(
    img_number,
    expected_isbn_number,
    get_sample_image,
):
    """
    Please note that this sample images are prepared for stricly for this test and does not test
    more high-level functionality!
    """
    # GIVEN
    sample_image = get_sample_image(img_number)

    # WHEN
    barcode = read_barcodes(sample_image)

    # THEN
    assert barcode == expected_isbn_number
