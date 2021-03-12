from kivy.app import App

from windows.input_number_manually_window import InputNumberManuallyScreen
from windows.job_window import JobWindow
from windows.main_window import MainWindow
from windows.manager import Manager
from windows.problem_window import ProblemWindow
from windows.results_window import ResultsWindow
from windows.settings_window import SettingsWindow


class BuildApp(App):
    def build(self):
        return Manager()
