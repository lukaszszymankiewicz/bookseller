from app.windows.utils.constants import CURRENCY
from app.windows.ux.colors import BLACK, GREY
from app.windows.widgets.two_state_clickable_image import \
    TwoStateClickableImage

from .base_window import BaseBooksellerWindow


class SettingsWindow(BaseBooksellerWindow):
    id = "settings_window"

    price_strategy = 0

    def _disable_all_price_strategy_button(self):
        for widget_name in self.ids.keys():
            # TODO: add some "functionality" paramter to whis widget class
            if widget_name.endswith("price_strategy"):
                self.ids[widget_name].background_color = BLACK

    def sell_as(self, condition: str):
        if condition == "new":
            self.ids["set_sell_as_new"].background_color = BLACK
            self.ids["set_sell_as_used"].background_color = GREY
        else:
            self.ids["set_sell_as_new"].background_color = GREY
            self.ids["set_sell_as_used"].background_color = BLACK

    def buynow(self, set_buynow: bool):
        if set_buynow:
            self.ids["buynow_true"].background_color = GREY
            self.ids["buynow_false"].background_color = BLACK
        else:
            self.ids["buynow_true"].background_color = BLACK
            self.ids["buynow_false"].background_color = GREY

    def set_price_strategy(self, percent: int):
        self._disable_all_price_strategy_button()
        self.ids[f"set_{str(percent)}_percent_price_strategy"].background_color = GREY
        self.price_strategy = percent

    def change_price(self, option: str, direction: int):
        widget = self.ids[option + "_delivery_price"]
        price = self._get_price(widget)

        if price == 0 and direction == -1:
            pass
        else:
            self._set_price(widget, price + direction)

    def _get_price(self, widget) -> bool:
        return float(widget.text.replace(" PLN", ""))

    def _set_price(self, widget, price) -> None:
        widget.text = str(price) + " " + CURRENCY

    def save_and_proceed(self):
        pass
