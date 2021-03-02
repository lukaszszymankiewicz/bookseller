import threading
from time import sleep

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

from utils import number_is_proper_isbn_number

Window.size = (360, 640)

from models import Book

kv = Builder.load_file("main.kv")


class SearchWindow(Screen):
    @property
    def _isbn_number(self):
        return self.manager.screens[0].ids["search_layout_number_label"].text

    def _len_is_satisfied(self):
        return len(self._isbn_number) == 10 or len(self._isbn_number) == 13

    def _validate(self):
        if self._len_is_satisfied():
            validation_message = number_is_proper_isbn_number(self._isbn_number)

            if validation_message.validation_passed:
                self._enable_start_button()
            else:
                self._set_error_message(value=validation_message.message)
                self._disable_start_button()

    def _set_error_message(self, value):
        self.manager.screens[0].ids["seach_layout_messages_label"].text = str(value)

    def _set_isbn_number(self, value):
        self.manager.screens[0].ids["search_layout_number_label"].text = value

    def _trim_isbn_number(self):
        self.manager.screens[0].ids["search_layout_number_label"].text = self._isbn_number[:-1]

    def _add_to_isbn_number(self, value):
        self.manager.screens[0].ids["search_layout_number_label"].text += str(value)

    def _disable_start_button(self):
        self.manager.screens[0].ids["run"].disabled = True

    def _enable_start_button(self):
        self.manager.screens[0].ids["run"].disabled = False

    def input_number(self, number: int):
        self._set_error_message(value="")

        if len(self._isbn_number) < 13:
            self._add_to_isbn_number(number)
            self._validate()

        else:
            self._set_error_message("ISBN can`t be longer!")

    def delete_last_number(self):
        if len(self._isbn_number) > 0:
            self._trim_isbn_number()

            if len(self._isbn_number) == 0:
                self._set_error_message("type ISBN number")
            else:
                self._validate()


class ResultsWindow(Screen):
    pass


class ProblemWindow(Screen):
    pass


class WaitWindow(Screen):
    def on_enter(self):

        global job_wip
        global job_done

        job_done = False
        job_wip = False

        Clock.schedule_interval(self.check, 1)

    @property
    def _isbn_number(self):
        return self.manager.screens[0].ids["search_layout_number_label"].text

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
        book = Book(raw_string=self._isbn_number, auto_request=True)

        self.manager.screens[2].ids["title"].text = str(book.data["title"])
        self.manager.screens[2].ids["author"].text = str(book.data["author"])
        self.manager.screens[2].ids["avg_prices"].text = str(book.data["avg_prices"])
        self.manager.screens[2].ids["sales_number"].text = str(book.data["sales_number"])

        global job_done
        job_done = True


def check_book_by_isbn(number, callback):
    book = Book(raw_string=number, auto_request=True)
    callback(book.data)


def wait(callback):
    sleep(10)
    callback()


class MyScreenManager(ScreenManager):
    pass


class BooksellerApp(App):
    def build(self):
        return MyScreenManager()


if __name__ == "__main__":
    BooksellerApp().run()
