from kivy.uix.screenmanager import ScreenManager


class Manager(ScreenManager):
    def fill_book_data_in_results_screen(self, book_data: dict) -> None:
        self.ids["results_window"].ids["title_content"].text = str(book_data["title"])
        self.ids["results_window"].ids["author_content"].text = str(book_data["author"])
        self.ids["results_window"].ids["avg_prices_content"].text = str(book_data["avg_prices"])
        self.ids["results_window"].ids["sales_number_content"].text = str(book_data["sales_number"])

    def clear_book_data(self) -> None:
        self.ids["results_window"].ids["title_content"].text = ""
        self.ids["results_window"].ids["author_content"].text = ""
        self.ids["results_window"].ids["avg_prices_content"].text = ""
        self.ids["results_window"].ids["sales_number_content"].text = ""
        self.ids["search_window"].ids["isbn_number_label"].text = ""

    def fill_error_in_problem_screen(self, message: str):
        self.current = "search"
        print(message)
        # self.ids["problem_window"].ids["problem_layout_message"].text = str(message)

    def get_isbn_number_from_search_screen(self) -> str:
        return self.ids["search_window"].ids["isbn_number_label"].text
