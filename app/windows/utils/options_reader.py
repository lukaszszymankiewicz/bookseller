import json


class OptionsReader:
    OPTIONS_PATH = "static/options.json"

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
