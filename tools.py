def comaIntoDot(iteration: int, max_iteration: int) -> str:
    if iteration != max_iteration - 1:
        return ", "
    else:
        return "."


def intInput(textToAsk: str, textToError: str) -> int:
    while True:
        try:
            value = int(input(textToAsk))
            return value
        except ValueError:
            print(textToError)


def floatInput(textToAsk: str, textToError: str) -> float:
    while True:
        try:
            value = float(input(textToAsk))
            return value
        except ValueError:
            print(textToError)


def strInput(textToAsk: str, textToError: str) -> str:
    while True:
        try:
            value = input(textToAsk)
            return value
        except ValueError:
            print(textToError)


def floatUnitTest(a: float, b: float, delta=10**-6) -> bool:
    """
    Try if a and b are equal with a gap smaller than delta
    """
    return abs(a-b) < abs(delta)
