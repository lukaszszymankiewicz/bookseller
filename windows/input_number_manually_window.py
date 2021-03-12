from kivy.uix.screenmanager import Screen

from .utils import number_is_proper_isbn_number


class InputNumberManuallyScreen(Screen):
    @property
    def _isbn_number(self):
        return self.ids["isbn_number_label"].text

    def _len_is_satisfied(self):
        return len(self._isbn_number) == 10 or len(self._isbn_number) == 13

    def _validate(self):
        if self._len_is_satisfied():
            validation_message = number_is_proper_isbn_number(self._isbn_number)

            if validation_message.success:
                self._set_run_button(False)
            else:
                self._set_message(validation_message.content)
                self._set_run_button(True)

    def _set_run_button(self, button_state: bool):
        self.ids["run"].disabled = button_state

    def _add_char_to_isbn_number(self, char: str):
        self.ids["isbn_number_label"].text += str(char)

    def _clear_message(self):
        self._set_message(value="")

    def _set_message(self, value: str):
        self.ids["message_label"].text = str(value)

    def _delete_last_char_from_isbn(self):
        self.ids["isbn_number_label"].text = self._isbn_number[:-1]

    def input_number(self, number: int):
        self._clear_message()

        if len(self._isbn_number) < 13:
            self._add_char_to_isbn_number(number)
            self._validate()
        else:
            self._set_message("ISBN can`t be longer!")

    def delete_last_number(self):
        if len(self._isbn_number) > 0:
            self._delete_last_char_from_isbn()

            if len(self._isbn_number) == 0:
                self._set_message("type ISBN number")
            else:
                self._validate()
