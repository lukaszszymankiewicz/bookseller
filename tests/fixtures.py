import os
import pickle

import bs4
import pytest
from PIL import Image

pickled_soups_path = "tests/pickled_soups/"
sample_images_path = "tests/sample_images/"


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


@pytest.fixture()
def get_sample_image():
    def load_sample_image(image_number: int):
        if image_number > len(os.listdir(sample_images_path)):
            raise ValueError("this image number does not exist!")

        file_path = sample_images_path + f"sample_image_{image_number}.jpg"
        image = Image.open(file_path)

        return image

    return load_sample_image
