from app.windows.ux.colors import BLACK, GREY
from kivy.uix.button import Button


class GrayButton(Button):
    background_normal = ""
    font_size = 20
    background_color = GREY

    def __init__(self, **kwargs):
        super(GrayButton, self).__init__(**kwargs)


class InputNumberButton(GrayButton):
    def __init__(self, **kwargs):
        super(InputNumberButton, self).__init__(**kwargs)


class ChangePriceButton(Button):
    background_normal = ""
    font_size = 20
    background_color = GREY
    size_hint = (0.2, 0.1)

    def __init__(self, **kwargs):
        super(ChangePriceButton, self).__init__(**kwargs)


class SetLessPriceButton(ChangePriceButton):
    text = "-"

    def __init__(self, **kwargs):
        super(SetLessPriceButton, self).__init__(**kwargs)


class SetMorePriceButton(ChangePriceButton):
    text = "+"

    def __init__(self, **kwargs):
        super(SetMorePriceButton, self).__init__(**kwargs)


class BlackButton(Button):
    background_normal = ""
    font_size = 20
    background_color = BLACK

    def __init__(self, **kwargs):
        super(BlackButton, self).__init__(**kwargs)


class SmallGrayButton(Button):
    size_hint = (0.2, 0.1)
    background_normal = ""
    font_size = 20
    background_color = GREY

    def __init__(self, **kwargs):
        super(SmallGrayButton, self).__init__(**kwargs)


class SmallBlackButton(Button):
    size_hint = (0.5, 0.1)
    background_normal = ""
    font_size = 20
    background_color = BLACK

    def __init__(self, **kwargs):
        super(SmallBlackButton, self).__init__(**kwargs)
