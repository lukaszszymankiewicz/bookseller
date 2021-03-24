from kivy.uix.screenmanager import ScreenManager


class Manager(ScreenManager):
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
        self.current = "search"

    def get_isbn_number_from_search_screen(self) -> str:
        return self.get_screen("input_number_manually").ids["isbn_number_label"].text
