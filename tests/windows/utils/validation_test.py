import pytest
from faker import Faker
from windows.utils.validation import number_is_proper_isbn_number

N_PROBES = 100


def test_number_is_proper_isbn_number_sucessfully_recognize_valid_isbn_number_with_10_digits():
    # GIVEN
    faker = Faker()

    for _ in range(N_PROBES):
        isbn_number = faker.isbn10(separator="")

        # WHEN
        message = number_is_proper_isbn_number(isbn_number)

        # THEN
        assert message.validated


def test_number_is_proper_isbn_number_sucessfully_recognize_valid_isbn_number_with_13_digits():
    # GIVEN
    faker = Faker()

    for _ in range(N_PROBES):
        isbn_number = faker.isbn13(separator="")

        # WHEN
        message = number_is_proper_isbn_number(isbn_number)

        # THEN
        assert message.validated


@pytest.mark.parametrize(
    "isbn_number",
    [
        "8305116742",
        "8308017508",
        "9783161484101",
        "9788310133747",
        "9788308043898",
        "9788324054410",
        "9788377313311",
        "9788324034870",
        "9788363944666",
        "9780007547998",
        "9788395243355",
    ],
)
def test_number_is_proper_isbn_number_sucessfully_recognize_nonvalid_isbn_number(isbn_number):
    # WHEN
    message = number_is_proper_isbn_number(isbn_number)

    # THEN
    assert message.validated is False
    assert message.message == "wrong control sum"


@pytest.mark.parametrize(
    "isbn_number",
    [
        "8",
        "83",
        "978",
        "9788",
        "97883",
        "978832",
        "9788371",
        "97883240",
        "978836396",
        "97800075478",
        "978839524335",
        "97883952433589",
    ],
)
def test_number_is_proper_isbn_number_sucessfully_recognize_isbn_number_with_wrong_len(isbn_number):
    # WHEN
    message = number_is_proper_isbn_number(isbn_number)

    # THEN
    assert message.validated is False
    assert message.message == "wrong number length"


@pytest.mark.parametrize(
    "isbn_number",
    [
        "9733161484100",
        "9738310133748",
        "9738308043899",
        "9738324054411",
        "9738377313312",
        "9738324034871",
        "9738363944667",
        "9730007547999",
        "9738395243356",
    ],
)
def test_number_is_proper_isbn_number_sucessfully_recognize_isbn_number_with_wrong_prefix(
    isbn_number,
):
    # WHEN
    message = number_is_proper_isbn_number(isbn_number)

    # THEN
    assert message.validated is False
    assert message.message == "this number has invalid prefix!"
