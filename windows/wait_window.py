import threading

from kivy.clock import Clock
from kivy.uix.screenmanager import Screen

from .utils import get_book_data


class WaitWindow(Screen):
    def on_enter(self):
        global job_done
        global job_wip
        global job_succeded

        job_done = False
        job_succeded = False

        self.start_thread()

        Clock.schedule_interval(self.check, 1)

    def check(self, dt):
        global job_done

        if job_done:
            if job_succeded:
                self.manager.current = "results"
            else:
                self.manager.current = "problem"

    def start_thread(self):
        t = threading.Thread(target=self.process)
        t.start()

    def process(self):
        isbn_number = self.manager.get_isbn_number_from_search_screen()
        message = get_book_data(raw_string=isbn_number)

        global job_done
        global job_succeded

        if message.completed:
            book_data = message.message
            self.manager.fill_book_data_in_results_screen(book_data)
            job_succeded = True
            job_done = True

        else:
            self.manager.fill_error_in_problem_screen(message.message)
            job_succeded = False
            job_done = True
