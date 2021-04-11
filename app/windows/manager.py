from app.windows.utils.job import JobManager
from app.windows.utils.options_reader import OptionsReader
from kivy.uix.screenmanager import ScreenManager


class Manager(ScreenManager):
    job_manager = JobManager()

    def _save_settings(self):
        settings = {}

        for name, widget in self.get_screen("settings").ids.items():
            if hasattr(widget, "save_in_settings") and getattr(widget, "save_in_settings") != "":
                settings[name] = {widget.save_in_settings: getattr(widget, widget.save_in_settings)}

        OptionsReader.save_options(settings)

    def _fill_up_settings(self):
        options = OptionsReader.get_options()

        for widget_id, settings in options.items():
            for setting, value in settings.items():
                if hasattr(self.get_screen("settings").ids[widget_id], setting):
                    setattr(self.get_screen("settings").ids[widget_id], setting, value)
                else:
                    pass

    def go_to_input_number_manually_screen(self):
        self.current = "input_number_manually"

    def go_to_problem_screen(self, exception):
        self.current = "problem"
        self.fill_error_in_problem_screen(exception)

    def go_to_job_screen(self):
        self.current = "job"

    def go_back_from_settings_screen(self):
        self._save_settings()
        self.current = "main"

    def go_to_main_screen(self):
        self.current = "main"

    def go_to_settings_screen(self):
        self._clear_settings_screen()
        self._fill_up_settings()
        self.current = "settings"

    def go_to_results_screen(self, book_data: dict):
        self.current = "results"
        self.fill_book_data_in_results_screen(book_data)

    def _clear_settings_screen(self):
        for price in [0, 10, 20, 40]:
            widget_name = "set_" + str(price) + "_percent_price_strategy"
            self.get_screen("settings").ids[widget_name].state = "normal"

        self.get_screen("settings").ids["used_false"].state = "normal"
        self.get_screen("settings").ids["used_true"].state = "normal"
        self.get_screen("settings").ids["buynow_false"].state = "normal"
        self.get_screen("settings").ids["buynow_true"].state = "normal"

    def fill_book_data_in_results_screen(self, book_data: dict) -> None:
        self.get_screen("results").ids["title_content"].text = str(book_data["title"])
        self.get_screen("results").ids["author_content"].text = str(book_data["author"])
        self.get_screen("results").ids["avg_prices_content"].text = str(book_data["avg_prices"])
        self.get_screen("results").ids["sales_number_content"].text = str(book_data["sales_number"])

    def clear_book_data(self) -> None:
        self.get_screen("results").ids["title_content"].text = ""
        self.get_screen("results").ids["author_content"].text = ""
        self.get_screen("results").ids["avg_prices_content"].text = ""
        self.get_screen("results").ids["sales_number_content"].text = ""
        self.get_screen("input_number_manually").ids["isbn_number_label"].text = ""

    def fill_error_in_problem_screen(self, message: str):
        if hasattr(message, "args"):
            self.get_screen("problem").ids["problem_layout_message"].text = message.args[0]
        else:
            self.get_screen("problem").ids["problem_layout_message"].text = message

    def get_isbn_number_from_search_screen(self) -> str:
        return self.get_screen("input_number_manually").ids["isbn_number_label"].text
