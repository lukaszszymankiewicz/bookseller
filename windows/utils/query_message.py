class QueryMessage:
    def __init__(self, completed: bool = True, message: str = None):
        self.completed = completed
        self.message = message
