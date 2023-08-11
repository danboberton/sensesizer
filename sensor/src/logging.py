class Log:

    def __init__(self, logID: str):
        self.logID = logID

    def print_log(self, message: str):
        print(f"{self.logID}: {message}")
