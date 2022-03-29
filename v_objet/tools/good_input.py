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

    @staticmethod
    def isInputYes(textToAsk: str):
        textToError = "Thanks to press y for yes and n for no"
        while True:
            try:
                value = input(f"{textToAsk} (y/n) : ")
                if value.lower() == "y":
                    return True
                elif value.lower() == "n":
                    return False
                else:
                    print(textToError)
            except ValueError:
                print(textToError)
