import json


class OptionsReader:
    """
    Wapper for options file read/write.

    Primarly it just iteate over option buttons, check whether its state should be perseved and save
    it state if needed.

    """

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
