class BooksellerError(Exception):
    pass


class BookNotFoundError(BooksellerError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)


class WrongResponseError(BooksellerError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)


class AllegroUnavailableError(BooksellerError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)


class NoInternetConnectionError(BooksellerError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)


class NoBarcodeFoundError(BooksellerError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
