import os
import time

from app.windows.utils.barcode_reader import read_barcodes
from kivy.clock import Clock
from kivy.uix.camera import Camera
from kivy.uix.screenmanager import Screen
from PIL import Image

from ..config import camera_check_time_interval


class CameraWindow(Screen):
    orientation = "vertical"

    def on_enter(self):
        self.i = 0
        # self.event = Clock.schedule_interval(self.find_barcode, camera_check_time_interval)

    #  def find_barcode(self, dt):
    #      if self.i < 1:
    #          self.i += 1

    #      if self.i >= 1:
    #          camera = self.ids["camera"]
    #          timestr = time.strftime("%Y%m%d_%H%M%S")
    #          file_name = f"IMG_{timestr}.png"
    #          camera.export_to_png(file_name)
    #          image = Image.open(file_name)

    #          try:
    #              result = read_barcodes(image=image)
    #              # os.remove(file_name)
    #              print(result)

    #          except Exception as e:
    #              print(e)

    #          # self.event.cancel()

    # if self.job.status == "DONE":
    #     if self.job.result.success:
    #         self.manager.current = "results"
    #         print(isbn)
    #         self.manager.fill_book_data_in_results_screen(self.job.result.content)

    #     else:
    #         self.manager.current = "problem"
    #         self.manager.fill_error_in_problem_screen(self.job.result.content)

    #     self.event.cancel()

    def __init__(self, **kwargs):
        super(CameraWindow, self).__init__(**kwargs)
        # self.add_widget(
        #     Camera(resolution=(self.width, self.height), play=False, allow_stretch=True)
        # )
