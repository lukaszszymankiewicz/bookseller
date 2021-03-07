import pickle

import bs4
import pytest


@pytest.fixture()
def get_pickled_soup():
    def load_pickled_soup(soup_number: int):
        # TODO: add os counte of pickled soups limit
        file_name = f"pickle_{soup_number}.pkl"
        path = "tests/pickled_soups/"
        file = open(path + file_name, "rb")
        soup = pickle.load(file)

        file.close()

        return bs4.BeautifulSoup(soup, "html.parser")

    return load_pickled_soup
