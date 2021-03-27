import os
import pickle

import bs4
import pytest

pickled_soups_path = "tests/pickled_soups/"


@pytest.fixture()
def get_pickled_soup():
    def load_pickled_soup(soup_number: int):

        if soup_number > len(os.listdir(pickled_soups_path)):
            raise ValueError("this soup number does not exist!")

        file_name = f"pickle_{soup_number}.pkl"
        file = open(pickled_soups_path + file_name, "rb")
        soup = pickle.load(file)

        file.close()

        return bs4.BeautifulSoup(soup, "html.parser")

    return load_pickled_soup


@pytest.fixture()
def get_sample_proper_settings():
    def load_pickled_soup(soup_number: int):

        if soup_number > len(os.listdir(pickled_soups_path)):
            raise ValueError("this soup number does not exist!")

        file_name = f"pickle_{soup_number}.pkl"
        file = open(pickled_soups_path + file_name, "rb")
        soup = pickle.load(file)

        file.close()

        return bs4.BeautifulSoup(soup, "html.parser")

    return load_pickled_soup
