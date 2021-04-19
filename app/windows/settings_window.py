from kivy.uix.screenmanager import Screen

CURRENCY = "PLN"


class SettingsWindow(Screen):
    id = "settings_window"
    price_strategy = 0

    def change_price(self, delivey_option: str, direction: int):
        widget = self.ids[delivey_option + "_delivery_price"]
        price = self._get_price(widget)

        if price == 0 and direction == -1:
            pass
        else:
            self._set_price(widget, price + direction)

    def _get_price(self, widget) -> bool:
        return float(widget.text.replace(" PLN", ""))

    def _set_price(self, widget, price) -> None:
        widget.text = str(price) + " " + CURRENCY
