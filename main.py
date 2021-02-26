from kivy.app import App
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

Window.size = (360, 640)

from models import Book

kv = Builder.load_file("main.kv")


class SearchWindow(Screen):
    def check_book_by_isbn(self, number):

        book = Book(raw_string=number, auto_request=True)
        import pdb

        pdb.set_trace()


class ResultsWindow(Screen):
    pass


class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)


class BooksellerApp(App):
    def build(self):
        return MyScreenManager()


if __name__ == "__main__":
    BooksellerApp().run()
