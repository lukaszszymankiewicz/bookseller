from kivy.uix.screenmanager import Screen


class ResultsWindow(Screen):
    def goback(self):
        self.manager.clear_book_data()

    def sell(self):
        pass
