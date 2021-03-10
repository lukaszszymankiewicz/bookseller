from kivy.app import App

from windows.job_window import JobWindow
from windows.manager import Manager
from windows.problem_window import ProblemWindow
from windows.results_window import ResultsWindow
from windows.search_window import SearchWindow


class BuildApp(App):
    def build(self):
        return Manager()
