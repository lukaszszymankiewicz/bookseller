from kivy.uix.screenmanager import Screen


class ResultsWindow(Screen):
    id = "results_window"

    def goback(self):
        self.manager.clear_book_data()
        self.manager.current = "main"

    def sell(self):
        pass
