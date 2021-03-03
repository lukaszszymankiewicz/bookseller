class ValidationMessage:
    @property
    def validation_passed(self):
        return self.validated

    def __init__(self, validated: bool, message: str = None):
        self.validated = validated
        self.message = message
