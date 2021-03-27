import json
from shutil import copyfile


class OptionsReader:
    OPTIONS_PATH = "static/options.json"
    DEFAULT_OPTIONS_PATH = "static/default_options.json"

    @staticmethod
    def get_options():
        with open(OptionsReader.OPTIONS_PATH, "r") as file:
            options = json.load(file)
        file.close()

        return options

    @staticmethod
    def save_options(options: dict):
        with open(OptionsReader.OPTIONS_PATH, "w") as file:
            json.dump(options, file)

        file.close()

    @staticmethod
    def recreate_options():
        copyfile(OptionsReader.DEFAULT_OPTIONS_PATH, OptionsReader.OPTIONS_PATH)
