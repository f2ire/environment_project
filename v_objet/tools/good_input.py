class GoodInput:
    """Class to use good input"""

    @staticmethod
    def intInput(textToAsk: str, textToError: str) -> int:
        while True:
            try:
                value = int(input(textToAsk))
                return value
            except ValueError:
                print(textToError)

    @staticmethod
    def floatInput(textToAsk: str, textToError: str) -> float:
        while True:
            try:
                value = float(input(textToAsk))
                return value
            except ValueError:
                print(textToError)

    @staticmethod
    def strInput(textToAsk: str, textToError: str) -> str:
        while True:
            try:
                value = input(textToAsk)
                return value
            except ValueError:
                print(textToError)
