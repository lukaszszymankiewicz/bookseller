import warnings

from utils import (NONDIGITS_REGEX, WHITESPACE_REGEX, construct_author_request,
                   construct_isbn_url, make_request_and_serialize_response,
                   run_substract_regex)


class ISBNnumber:
    CLEANERS = [WHITESPACE_REGEX, NONDIGITS_REGEX]
    LEGAL_PREFIX = [978, 979]

    def __init__(self, raw_string: str, validate: bool = False):
        self.code = self._clean_raw_string(raw_string)

        if validate:
            self._validate()

    def __len__(self):
        return len(self.code)

    def _clean_raw_string(self, raw_string: str) -> str:
        string_cleaned = raw_string

        for cleaner_regex in self.CLEANERS:
            string_cleaned = run_substract_regex(regex_args=cleaner_regex, text=string_cleaned)

        return string_cleaned

    @property
    def control_number(self):
        return int(self.code[-1])

    @property
    def prefix(self):
        if len(self) == 13:
            return int(self.code[:3])
        else:
            raise warnings.warn("ISBN prefix is nonexistent for short codes.")
            return None

    def get_book_data(self):
        url = construct_isbn_url(self.code)
        data = make_request_and_serialize_response(url)

        author_code = self._extract_author_code(data)
        author_request_url = construct_author_request(author_code)
        author_data = make_request_and_serialize_response(author_request_url)

        author = self._extract_author(author_data)
        title = self._extract_title(data)

        return {"author": author, "title": title}

    def _extract_author(self, data: dict):
        return data.get("name")

    def _extract_title(self, data: dict):
        raw_title = data.get("title")
        return raw_title.split(":")[0]

    def _extract_author_code(self, data: dict):
        return data.get("authors")[0]["key"].replace("/authors/", "")

    def _validate(self):
        if len(self) not in [10, 13]:
            raise ValueError(f"{self.code} is not valid ISBN number! (nonvalid length)")

        if len(self) == 13 and self.prefix not in self.LEGAL_PREFIX:
            raise ValueError(f"{self.code} is not valid ISBN number! (nonvalid prefix)")

        if len(self) == 10:
            control_sum = 0
            for index, number in enumerate(self.code[:-1]):
                control_sum += int(number) * index

            control_number = control_sum % 11

            if control_number != self.control_number:
                raise ValueError(f"{self.code} is not valid ISBN number! (control sum error)")

        if len(self) == 13:
            control_sum = 0

            for index, number in enumerate(self.code[3:]):
                if index % 2 == 0:
                    multiplier = 3
                else:
                    multiplier = 1
                control_sum += int(number) * multiplier

            control_number = 10 - (control_sum % 10)

            if control_number != self.control_number:
                raise ValueError(f"{self.code} is not valid ISBN number! (control sum error)")
