from app.windows.utils.barcode_reader import read_barcodes
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from PIL import Image

ON = True
OFF = False


class CameraWindow(Screen):
    orientation = "vertical"

    def __init__(self, **kwargs):
        super(CameraWindow, self).__init__(**kwargs)
        self.event = None

    @property
    def scan_camera(self):
        return self.ids.get("scan_camera")

    @property
    def scan_camera_is_indexed(self):
        return self.scan_camera is not None

    @property
    def texture(self):
        return self.scan_camera.texture

    @property
    def texture_working(self):
        return self.texture is not None

    def on_enter(self):
        self.event = Clock.schedule_interval(self.check_barcode, 0.2)

    def on_leave(self):
        self._set_camera(OFF)
        self.event.cancel()
        Clock.unschedule(self.event)

    def _set_camera(self, state: bool):
        if self.scan_camera_is_indexed:
            self.scan_camera.play = state

    def check_barcode(self, dt: str):
        self.canvas.ask_update()
        self._set_camera(ON)

        if self.scan_camera_is_indexed and self.texture_working:
            self.manager.job_manager.add_job(
                fun=read_barcodes,
                args={
                    "image": Image.frombytes(
                        mode="RGBA",
                        size=self.texture.size,
                        data=self.texture.pixels,
                    )
                },
                callback=self.manager.go_to_input_number_manually_screen,
                check_interval=0.05,
            )
