from kivy.app import App
from kivy.core.window import Window

from app.windows.camera_window import CameraWindow
from app.windows.input_number_manually_window import InputNumberManuallyScreen
from app.windows.main_window import MainWindow
from app.windows.manager import Manager
from app.windows.problem_window import ProblemWindow
from app.windows.results_window import ResultsWindow
from app.windows.settings_window import SettingsWindow

from .config import DEFAULT_WINDOW_SIZE


class BuildApp(App):
    # TODO: is this really needed?
    # TODO: response (it is good for testing but in the end it should not be in the app code).
    Window.size = DEFAULT_WINDOW_SIZE  # this will set proper window size

    def build(self):
        return Manager()

    def on_stop(self):
        # TODO: here camera should be stopeed
        pass

    def on_pause(self):
        # TODO: here camera should be stopeed
        return True

    def on_resume(self):
        # TODO: here camera should be started
        pass
