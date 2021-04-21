from backend.validation import ValidationMessage, code_is_proper_isbn
from kivy.uix.screenmanager import Screen


class InputNumberManuallyScreen(Screen):
    id = "input_number_manually_window"

    @property
    def _isbn_number(self):
        return self.ids["isbn_number_label"].text

    def _read_validation_message(self, message: ValidationMessage) -> None:
        if message.success:
            self._enable_going_further(message_to_user=message.content)
        else:
            self._disable_going_further(message_to_user=message.content)

    def _enable_going_further(self, message_to_user: str) -> None:
        self._set_message(message_to_user)
        self._set_run_button(True)

    def _disable_going_further(self, message_to_user: str) -> None:
        self._set_message(message_to_user)
        self._set_run_button(False)

    def _set_run_button(self, button_state: bool) -> None:
        self.ids["run"].disabled = not button_state

    def _clear_message(self) -> None:
        self._set_message(value="")

    def _set_message(self, value: str) -> None:
        self.ids["message_label"].text = str(value)

    def input_number(self, number: int) -> None:
        if len(self._isbn_number) < 13:
            self.ids["isbn_number_label"].text += str(number)
            self._validate(self._isbn_number)

    def delete_last_number(self) -> None:
        if len(self._isbn_number) > 0:
            self.ids["isbn_number_label"].text = self._isbn_number[:-1]
            self._validate(self._isbn_number)

    def _validate(self, code: int) -> None:
        self.manager.job_manager.add_concurent_jobs(
            funs=[code_is_proper_isbn],
            args={"code": code},
            callback=self._read_validation_message,
            fallback=self.manager.go_to_problem_screen,
            check_interval=0.01,
        )
