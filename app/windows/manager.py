from backend.job import JobManager
from backend.options_reader import OptionsReader
from kivy.uix.screenmanager import ScreenManager


class Manager(ScreenManager):
    job_manager = JobManager()

    def _save_settings(self):
        # TODO: move it to OptionsReader
        settings = {}

        for name, widget in self.get_screen("settings").ids.items():
            if hasattr(widget, "save_in_settings") and getattr(widget, "save_in_settings") != "":
                settings[name] = {widget.save_in_settings: getattr(widget, widget.save_in_settings)}

        OptionsReader.save_options(settings)

    def _fill_up_settings(self):
        # TODO: move it to OptionsReader
        options = OptionsReader.get_options()

        for widget_id, settings in options.items():
            for setting, value in settings.items():
                if hasattr(self.get_screen("settings").ids[widget_id], setting):
                    setattr(self.get_screen("settings").ids[widget_id], setting, value)
                else:
                    pass

    def go_to_input_number_manually_screen(self, number=""):
        self.current = "input_number_manually"
        self.get_screen("input_number_manually").ids["isbn_number_label"].text = str(number)

    def go_to_camera_screen(self):
        self.current = "camera"

    def go_to_main_screen(self):
        self.current = "main"

    def go_to_problem_screen(self, exception):
        self.current = "problem"
        self.fill_error_in_problem_screen(exception)

    def go_back_from_settings_screen(self):
        self._save_settings()
        self.current = "main"

    def go_to_settings_screen(self):
        self._clear_settings_screen()
        self._fill_up_settings()
        self.current = "settings"

    def go_to_results_screen(self, book_data: dict):
        self.current = "results"
        self.fill_book_data_in_results_screen(book_data)

    def go_back_from_results_screen(self):
        self.job_manager.kill_jobs()
        self.clear_book_data()
        self.current = "main"

    def order_find_query(self, raw_isbn_code: str):
        self.current = "results"
        self.get_screen("results").run_find_query(raw_isbn_code)

    def _clear_settings_screen(self):
        # TODO: add some custom propperty to know what should be cleared
        for price in [0, 10, 20, 40]:
            widget_name = "set_" + str(price) + "_percent_price_strategy"
            self.get_screen("settings").ids[widget_name].state = "normal"

        self.get_screen("settings").ids["used_false"].state = "normal"
        self.get_screen("settings").ids["used_true"].state = "normal"
        self.get_screen("settings").ids["buynow_false"].state = "normal"
        self.get_screen("settings").ids["buynow_true"].state = "normal"

    def clear_book_data(self) -> None:
        # TODO: add some custom propperty to know what should be cleared
        self.get_screen("results").ids["title_content"].text = ""
        self.get_screen("results").ids["author_content"].text = ""
        self.get_screen("results").ids["avg_prices_content"].text = ""
        self.get_screen("results").ids["sold_copies_content"].text = ""
        self.get_screen("input_number_manually").ids["isbn_number_label"].text = ""

    def fill_error_in_problem_screen(self, message: str):
        self.get_screen("problem").ids["problem_layout_message"].text = message

    def get_isbn_number_from_search_screen(self) -> str:
        return self.get_screen("input_number_manually").ids["isbn_number_label"].text
