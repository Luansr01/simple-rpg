class NoStateFound(Exception):
    def __init__(self, message="No State Found"):
        self.message = message
        super().__init__(self.message)