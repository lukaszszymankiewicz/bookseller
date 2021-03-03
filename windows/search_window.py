from kivy.uix.screenmanager import Screen

from .utils import number_is_proper_isbn_number


class SearchWindow(Screen):
    @property
    def _isbn_number(self):
        return self.manager.screens[0].ids["search_layout_number_label"].text

    def _len_is_satisfied(self):
        return len(self._isbn_number) == 10 or len(self._isbn_number) == 13

    def _validate(self):
        if self._len_is_satisfied():
            validation_message = number_is_proper_isbn_number(self._isbn_number)

            if validation_message.validation_passed:
                self._enable_start_button()
            else:
                self._set_error_message(value=validation_message.message)
                self._disable_start_button()

    def _set_error_message(self, value):
        self.manager.screens[0].ids["seach_layout_messages_label"].text = str(value)

    def _set_isbn_number(self, value):
        self.manager.screens[0].ids["search_layout_number_label"].text = value

    def _trim_isbn_number(self):
        self.manager.screens[0].ids["search_layout_number_label"].text = self._isbn_number[:-1]

    def _add_to_isbn_number(self, value):
        self.manager.screens[0].ids["search_layout_number_label"].text += str(value)

    def _disable_start_button(self):
        self.manager.screens[0].ids["run"].disabled = True

    def _enable_start_button(self):
        self.manager.screens[0].ids["run"].disabled = False

    def input_number(self, number: int):
        self._set_error_message(value="")

        if len(self._isbn_number) < 13:
            self._add_to_isbn_number(number)
            self._validate()

        else:
            self._set_error_message("ISBN can`t be longer!")

    def delete_last_number(self):
        if len(self._isbn_number) > 0:
            self._trim_isbn_number()

            if len(self._isbn_number) == 0:
                self._set_error_message("type ISBN number")
            else:
                self._validate()
