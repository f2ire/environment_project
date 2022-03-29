class EnvironmentalImpact:
    def __init__(self, meal, envDict, envName) -> None:
        self.dict5D = {}
        for name in envName:
            val = sum(
                [
                    meal.productQuantity[i] * envDict[name][product]
                    for i, product in enumerate(meal.productList)
                ]
            )
            self.dict5D[name] = val

    def __repr__(self) -> str:
        return str(self.dict5D)
        # print(self)
