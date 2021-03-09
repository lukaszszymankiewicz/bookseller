from kivy.uix.screenmanager import ScreenManager


class MyScreenManager(ScreenManager):
    def fill_book_data_in_results_screen(self, book_data: dict) -> None:
        self.ids["results_window"].ids["title"].text = str(book_data["title"])
        self.ids["results_window"].ids["author"].text = str(book_data["author"])
        self.ids["results_window"].ids["avg_prices"].text = str(book_data["avg_prices"])
        self.ids["results_window"].ids["sales_number"].text = str(book_data["sales_number"])

    def clear_book_data(self) -> None:
        self.ids["results_window"].ids["title"].text = ""
        self.ids["results_window"].ids["author"].text = ""
        self.ids["results_window"].ids["avg_prices"].text = ""
        self.ids["results_window"].ids["sales_number"].text = ""
        self.ids["search_window"].ids["search_layout_number_label"].text = ""
        self.set_error_message_on_search_screen("")
        self.disable_start_button_on_search_screen()

    def fill_error_in_problem_screen(self, message: str):
        self.ids["problem_window"].ids["problem_layout_message"].text = str(message)

    def get_isbn_number_from_search_screen(self) -> str:
        return self.ids["search_window"].ids["search_layout_number_label"].text

    def set_error_message_on_search_screen(self, message: str):
        self.ids["search_window"].ids["seach_layout_messages_label"].text = str(message)

    def set_isbn_number_on_seach_screen(self, value: str):
        self.ids["search_window"].ids["search_layout_number_label"].text = str(value)

    def trim_isbn_number_on_search_screen(self):
        trimmed_number = self.get_isbn_number_from_search_screen()[:-1]
        self.ids["search_window"].ids["search_layout_number_label"].text = trimmed_number

    def add_to_isbn_number_on_search_screen(self, char: str):
        self.ids["search_window"].ids["search_layout_number_label"].text += str(char)

    def disable_start_button_on_search_screen(self):
        self.ids["search_window"].ids["run"].disabled = True
        self.ids["search_window"].ids["run"].state = "normal"

    def enable_start_button_on_search_screen(self):
        self.ids["search_window"].ids["run"].disabled = False
