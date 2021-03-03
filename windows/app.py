from kivy.app import App

from windows.problem_window import ProblemWindow
from windows.results_window import ResultsWindow
from windows.screen_menager import MyScreenManager
from windows.search_window import SearchWindow
from windows.wait_window import WaitWindow


class BuildApp(App):
    def build(self):
        return MyScreenManager()
