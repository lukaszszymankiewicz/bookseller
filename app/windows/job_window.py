from kivy.uix.screenmanager import Screen

from .utils import query_book_data


class JobWindow(Screen):
    def on_enter(self):
        isbn_number = self.manager.get_isbn_number_from_search_screen()

        # TODO: move this to manager mayabe? (think about it!)
        self.manager.job_manager.add_job(
            fun=query_book_data,
            args={"raw_string": isbn_number},
            callback=self.manager.go_to_results_screen,
            fallback=self.manager.go_to_problem_screen,
            check_interval=0.5,
        )
