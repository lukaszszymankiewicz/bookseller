import threading

from kivy.clock import Clock
from kivy.uix.screenmanager import Screen

from .utils import get_book_data


class WaitWindow(Screen):
    @property
    def _isbn_number(self):
        return self.manager.screens[0].ids["search_layout_number_label"].text

    def on_enter(self):

        global job_wip
        global job_done

        job_done = False
        job_wip = False

        Clock.schedule_interval(self.check, 1)

    def check(self, dt):
        global job_wip
        global job_done

        if not job_wip:
            job_wip = True
            self.start_thread()

        if job_done:
            self.manager.current = "results"

    def start_thread(self):
        t = threading.Thread(target=self.process)
        t.start()

    def process(self):
        book_data = get_book_data(raw_string=self._isbn_number)

        self.manager.screens[2].ids["title"].text = str(book_data["title"])
        self.manager.screens[2].ids["author"].text = str(book_data["author"])
        self.manager.screens[2].ids["avg_prices"].text = str(book_data["avg_prices"])
        self.manager.screens[2].ids["sales_number"].text = str(book_data["sales_number"])

        global job_done
        job_done = True
