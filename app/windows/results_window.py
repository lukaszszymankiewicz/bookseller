from typing import Dict

from kivy.uix.screenmanager import Screen

from .utils import query_avg_price_and_sold_copies, query_title_and_author


class ResultsWindow(Screen):
    id = "results_window"

    def run_find_query(self, raw_isbn_string: str):
        self.manager.job_manager.add_job(
            fun=query_title_and_author,
            args={"isbn_string": raw_isbn_string},
            callback=self.run_avg_price_and_sold_copies_query,
            fallback=self.manager.go_to_problem_screen,
            check_interval=0.5,
        )

    def run_avg_price_and_sold_copies_query(self, title_and_author_data: Dict[str, str]):
        self._update_title_and_author(title_and_author_data)

        self.manager.job_manager.add_job(
            fun=query_avg_price_and_sold_copies,
            args=title_and_author_data,
            callback=self._update_avg_prices_and_sold_copies,
            fallback=self.manager.go_to_problem_screen,
            check_interval=0.5,
        )

    def _update_avg_prices_and_sold_copies(self, avg_prices_and_sold_copies: Dict[str, float]):
        self._fill_label(item="avg_prices", content=avg_prices_and_sold_copies["avg_prices"])
        self._fill_label(item="sold_copies", content=avg_prices_and_sold_copies["sold_copies"])
        self._disable_hourglass(item="avg_prices")
        self._disable_hourglass(item="sold_copies")

    def _update_title_and_author(self, title_and_author_data):
        self._fill_label(item="title", content=title_and_author_data["title"])
        self._fill_label(item="author", content=title_and_author_data["author"])
        self._disable_hourglass(item="title")
        self._disable_hourglass(item="author")

    def _disable_hourglass(self, item: str):
        self.ids[item + "_hourglass"].source = "static/empty.png"

    def _fill_label(self, item: str, content: str):
        self.ids[item + "_content"].text = str(content)
