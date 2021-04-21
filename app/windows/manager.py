from backend.job import JobManager
from backend.options_reader import OptionsReader
from backend.widget_helpers import WidgetInspector
from kivy.uix.screenmanager import ScreenManager


class Manager(ScreenManager):
    job_manager = JobManager()
    options_reader = OptionsReader()
    widget_inspector = WidgetInspector()

    def widgets_on_screen(self, screen):
        return self.get_screen(screen).ids

    def _save_settings(self):
        widgets_state = self.widget_inspector.filter_widgets_by_attribute(
            widgets=self.widgets_on_screen("settings"), attribute="save_in_settings"
        )
        self.options_reader.save_options(widgets_state)

    def go_to_input_number_manually_screen(self, number=""):
        self.get_screen("input_number_manually").ids["isbn_number_label"].text = str(number)
        self.current = "input_number_manually"

    def go_to_camera_screen(self):
        self.current = "camera"

    def go_to_main_screen(self):
        self.current = "main"

    def go_to_problem_screen(self, exception):
        self.fill_error_in_problem_screen(exception)
        self.current = "problem"

    def go_back_from_settings_screen(self):
        self._save_settings()
        self.current = "main"

    def go_to_settings_screen(self):
        self.set_defaults_values_on_window("settings")
        self._fill_up_settings()
        self.current = "settings"

    def _fill_up_settings(self):
        options = self.options_reader.get_options()
        self.widget_inspector.set_widgets_values(self.widgets_on_screen("settings"), options)

    def go_to_results_screen(self, book_data: dict):
        self.fill_book_data_in_results_screen(book_data)
        self.current = "results"

    def go_back_from_results_screen(self):
        self.job_manager.kill_all_jobs()
        self.set_defaults_values_on_window("input_number_manually")
        self.set_defaults_values_on_window("results")
        self.current = "main"

    def order_find_query(self, raw_isbn_code: str):
        self.get_screen("results").run_find_query(raw_isbn_code)
        self.current = "results"

    def set_defaults_values_on_window(self, screen: str):
        self.widget_inspector.set_widgets_default_values(self.widgets_on_screen(screen))

    def fill_error_in_problem_screen(self, message: str):
        self.get_screen("problem").ids["problem_layout_message"].text = message

    def get_isbn_number_from_search_screen(self) -> str:
        return self.get_screen("input_number_manually").ids["isbn_number_label"].text
