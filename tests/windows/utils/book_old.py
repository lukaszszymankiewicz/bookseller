import os

import pytest
from models import Book

# TODO: move it to some more convinent place
os.environ["RUN_REQUESTS_AT_TEST"] = "False"


class TestBook:
    def test_no_title_is_inputted_if_not_auto_request_is_inputted(self):
        # GIVEN
        code = "979-1-491-91205-8"
        expected_title = None

        # WHEN
        book = Book(code, auto_request=False)
        title = book.title

        # THEN
        assert expected_title == title

    @pytest.mark.skipif(
        os.environ["RUN_REQUESTS_AT_TEST"] == "False", reason="requests test in pipelines only"
    )
    def test_title_is_read_properly(self):
        # GIVEN
        code = "978-1-491-91205-8"
        expected_title = "Python Data Science Handbook: Essential Tools for Working with Data"

        # WHEN
        book = Book(code, auto_request=True)
        title = book.title

        # THEN
        assert expected_title == title
