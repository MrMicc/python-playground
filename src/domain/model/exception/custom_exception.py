class NomeInvalidoError(Exception):
    def __init__(self, messages):
        self.messages = messages


class EmailInvalidoError(Exception):
    def __init__(self, messages):
        self.messages = messages
