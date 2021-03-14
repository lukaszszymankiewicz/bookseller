from kivy.clock import Clock
from kivy.uix.screenmanager import Screen

from ..config import job_check_time_interval
from .utils import Job, query_book_data


class JobWindow(Screen):
    id = "job_window"

    def on_enter(self):
        isbn_number = self.manager.get_isbn_number_from_search_screen()
        self.job = Job(fun=query_book_data, args=isbn_number)
        self.event = Clock.schedule_interval(self.check_query_is_done, job_check_time_interval)

    def check_query_is_done(self, dt):
        if self.job.status == "DONE":
            if self.job.result.success:
                self.manager.current = "results"
                self.manager.fill_book_data_in_results_screen(self.job.result.content)

            else:
                self.manager.current = "problem"
                self.manager.fill_error_in_problem_screen(self.job.result.content)

            self.event.cancel()
