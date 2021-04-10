from kivy.app import App
from kivy.core.window import Window

from app.windows.camera_window import CameraWindow
from app.windows.input_number_manually_window import InputNumberManuallyScreen
from app.windows.job_window import JobWindow
from app.windows.main_window import MainWindow
from app.windows.manager import Manager
from app.windows.problem_window import ProblemWindow
from app.windows.results_window import ResultsWindow
from app.windows.settings_window import SettingsWindow
from app.windows.utils.options_reader import OptionsReader

from .config import DEFAULT_WINDOW_SIZE


class BuildApp(App):
    # TODO: is this really needed?
    Window.size = DEFAULT_WINDOW_SIZE  # this will set proper window size

    OptionsReader.get_options()  # this will validate options

    def build(self):
        return Manager()
