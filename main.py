import threading

from kivy.app import App
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager

Window.size = (360, 640)

from models import Book

kv = Builder.load_file("main.kv")


class SearchWindow(Screen):
    pass


class ResultsWindow(Screen):
    pass


class WaitWindow(Screen):
    number = StringProperty("")

    def on_enter(self, *args):
        # this is SO wrong!
        self.number = self.manager.screens[0].ids["isbn_number"].text

        def callback(data):
            self.manager.current = "results"
            self.manager.screens[2].ids["title"].text = str(data["title"])
            self.manager.screens[2].ids["author"].text = str(data["author"])
            self.manager.screens[2].ids["avg_prices"].text = str(data["avg_prices"])
            self.manager.screens[2].ids["sales_number"].text = str(data["sales_number"])

        threading.Thread(target=check_book_by_isbn(self.number, callback)).start()


def check_book_by_isbn(number, callback):
    book = Book(raw_string=number, auto_request=True)
    callback(book.data)


class MyScreenManager(ScreenManager):
    pass


class BooksellerApp(App):
    def build(self):
        return MyScreenManager()


if __name__ == "__main__":
    BooksellerApp().run()
