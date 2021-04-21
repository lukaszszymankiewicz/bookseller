import json


class OptionsReader:
    """
    Wrapper for options file read/write. Options are gathered as widgets "state" (or more preceisely
    specific attribute value) so at next start of application all widgets can be put into same state
    as before.

    """

    OPTIONS_PATH = "static/options.json"

    def __init__(self):
        pass

    def get_options(self):
        with open(OptionsReader.OPTIONS_PATH, "r") as file:
            options = json.load(file)
        file.close()

        return options

    def save_options(self, widgets_state: dict):
        with open(OptionsReader.OPTIONS_PATH, "w") as file:
            json.dump(widgets_state, file)

        file.close()
