import cv2
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
def test_reach_barcodes_works_properly_for_prepared_images(
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


@pytest.mark.parametrize(
    "img_number,expected_isbn_number",
    [
        (1, 9788386805433),
        (2, 9788371500480),
        (3, 9788328365032),
        (4, 9788379670499),
        (5, 9788363944667),
        (6, 9788386805433),
        (7, 9788371500480),
        (8, 9788328365032),
        (9, 9788379670499),
        (10, 9788363944667),
        (11, 9788363944667),
        (12, 9788363944667),
    ],
)
def test_reach_barcodes_works_properly_for_sample_camera_images(
    img_number,
    expected_isbn_number,
    get_sample_camera_image,
):
    # GIVEN
    image_path = get_sample_camera_image(img_number)

    im = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    blur = cv2.GaussianBlur(im, (5, 5), 0)
    ret, bw_im = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # WHEN
    barcode = read_barcodes(bw_im)

    # THEN
    if not barcode:
        assert False
    else:
        assert True
