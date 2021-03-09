from kivy.uix.screenmanager import Screen

from .utils import number_is_proper_isbn_number


class SearchWindow(Screen):
    @property
    def _isbn_number(self):
        return self.manager.get_isbn_number_from_search_screen()

    def _len_is_satisfied(self):
        return len(self._isbn_number) == 10 or len(self._isbn_number) == 13

    def _validate(self):
        if self._len_is_satisfied():
            validation_message = number_is_proper_isbn_number(self._isbn_number)

            if validation_message.validation_passed:
                self.manager.enable_start_button_on_search_screen()
            else:
                self.manager.set_error_message_on_search_screen(validation_message.message)
                self.manager.disable_start_button_on_search_screen()

    def input_number(self, number: int):
        self.manager.set_error_message_on_search_screen("")

        if len(self._isbn_number) < 13:
            self.manager.add_to_isbn_number_on_search_screen(number)
            self._validate()

        else:
            self._set_error_message()
            self.manager.set_error_message_on_search_screen("ISBN can`t be longer!")

    def delete_last_number(self):
        if len(self._isbn_number) > 0:
            self.manager.trim_isbn_number_on_search_screen()

            if len(self._isbn_number) == 0:
                self.manager.set_error_message_on_search_screen("type ISBN number")
            else:
                self._validate()
