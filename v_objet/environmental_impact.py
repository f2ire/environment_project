class EnvironmentalImpact:
    def __init__(self, meal, envDict, envName) -> None:
        self.list5D = [1]

    def __repr__(self) -> str:
        return str(self.list5D)

    def compute5D(self, meal, envDict, envName):
        for name in envName:
            self.list5D.append(
                [
                    meal.productQuantity[i] * envDict[name][product]
                    for i, product in enumerate(meal.productList)
                ]
            )
