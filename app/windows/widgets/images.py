from kivy.uix.image import Image


class TwoStateClickableImage(Image):
    state = 1

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if self.state == 1:
                self.source = "static/no.png"
                self.state = 0
            else:
                self.source = "static/yes.png"
                self.state = 1


class WaitForResultsImage(Image):
    source = "static/wait.gif"
    anim_delay = 0.1
    anim_loop = 5
    allow_stretch = False
    size_hint_y = 0.1
    size_hint_x = 0.1
    pos_hint = {"center_x": 0.5, "center_y": 0.5}

    def __init__(self, **kwargs):
        super(WaitForResultsImage, self).__init__(**kwargs)
