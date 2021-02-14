import pytest

from models.isbn_number import ISBNnumber


class TestISBNnumber:
    def test_validation_will_raise_error_if_wrong_len_code_is_inputted(self):
        # GIVEN
        wrong_code = "123456789"

        # WHEN
        with pytest.raises(ValueError):
            ISBNnumber(wrong_code)

    def test_validation_will_raise_error_if_code_without_proper_prefix_is_inputted(
        self,
    ):
        # GIVEN
        wrong_code = "1234567890123"

        # WHEN
        with pytest.raises(ValueError):
            ISBNnumber(wrong_code)

    def test_validation_will_raise_error_if_code_with_bad_control_sum_long_isbn(self):
        # GIVEN
        wrong_code = "978 1234567890"

        # WHEN
        with pytest.raises(ValueError):
            ISBNnumber(wrong_code)

    def test_validation_will_raise_error_if_code_with_bad_control_sum_short_isbn(self):
        # GIVEN
        wrong_code = "1234567890"

        # WHEN
        with pytest.raises(ValueError):
            ISBNnumber(wrong_code)

    def test_control_number_property(self):
        # GIVEN
        code = "978-1-491-91205-8"
        expected_control_number = 8

        # WHEN
        book = ISBNnumber(code)
        control_number = book.control_number

        # THEN
        assert expected_control_number == control_number

    def test_prefix_property(self):
        # GIVEN
        code = "979-1-491-91205-8"
        expected_prefix = 979

        # WHEN
        book = ISBNnumber(code)
        prefix = book.prefix

        # THEN
        assert expected_prefix == prefix
