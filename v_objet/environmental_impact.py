class EnvironmentalImpact:
    def __init__(self) -> None:
        self.list5D = []

    def __repr__(self) -> str:
        return str(self.list5D)

    def compute5D(self, meal, envDict, envName):
        for name in envName:
            self.list5D.append(
                sum(
                    [
                        meal.productQuantity[i] * envDict[name][product]
                        for i, product in enumerate(meal.productList)
                    ]
                )
            )
        # print(self)
