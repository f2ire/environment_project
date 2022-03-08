def comaIntoDot(iteration: int, max_iteration: int) -> str:
    if iteration != max_iteration - 1:
        return ", "
    else:
        return "."


def intInput(textToAsk: str, textToError: str) -> int:
    try:
        value = int(input(textToAsk))
    except ValueError:
        print(textToError)
        value = intInput(textToAsk, textToError)
    return value


def floatInput(textToAsk: str, textToError: str) -> float:
    try:
        value = float(input(textToAsk))
    except ValueError:
        print(textToError)
        value = floatInput(textToAsk, textToError)
    return value


def strInput(textToAsk: str, textToError: str) -> str:
    try:
        value = input(textToAsk)
    except ValueError:
        print(textToError)
        value = strInput(textToAsk, textToError)
    return value


def floatUnitTest(a: float, b: float, delta=10**-6) -> bool:
    """
    Try if a and b are equal with a gap smaller than delta
    """
    return abs(a-b) < abs(delta)
