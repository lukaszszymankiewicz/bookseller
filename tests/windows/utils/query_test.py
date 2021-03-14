import os

import pytest
from app.windows.utils.query import query_book_data

# TODO: move it to some more convinent place
os.environ["RUN_REQUESTS_AT_TEST"] = "False"


@pytest.mark.skipif(
    os.environ["RUN_REQUESTS_AT_TEST"] == "False", reason="requests test in pipelines only"
)
def test_title_is_read_properly(self):
    # GIVEN
    code = "978-1-491-91205-8"
    expected_title = "Python Data Science Handbook: Essential Tools for Working with Data"

    # WHEN
    results = query_book_data(code)
    title = results.content["title"]

    # THEN
    assert expected_title == title
