import numpy as np


class Meal:
    def __init__(
        self, prot: str, carb: str, fat: str, vege: str, fruit: str, extra: str
    ):
        self.productList = [prot, carb, fat, vege, fruit, extra]
        self.productQuantity = []
        self.Environmental5D = []

    def __repr__(self) -> str:
        return (
            f"{self.productList} : liste des produits"
            + f"{self.productQuantity} : liste des quantité"
            + f"{self.Environmental5D} : list Env5D"
        )

    def computeQuantity(self, user, dictByRU):
        targetCal = user.dailyEnergyRequirement * 0.4
        meal = self.productList
        extraDict = user.dictExtraQuantity
        proteinDict = dictByRU["gFatPerRetailUnit"]
        fatDict = dictByRU["gProteinPerRetailUnit"]
        carbohydrateDict = dictByRU["gCarbPerRetailUnit"]
        """
        Compute the quantity of g needed for the meal for each component
        and return a list [qProtSource, qCarbSource, qFatSource, qVegetable,"\
                    qFruit, qExtr²a]
        """
        qVeg = 0.125
        qFruit = 0.05
        # 0 : prot, 1 carb, 2 : fat, 3 : vegetable, 4 : fruit, 5 : extras
        # b = [prot, carb, fat]
        const = np.array(
            [
                (0.12 * targetCal / 4)
                - qVeg * proteinDict[meal[3]]
                - qFruit * proteinDict[meal[4]]
                - proteinDict[meal[5]] * extraDict[meal[5]],
                (0.66 * targetCal / 4)
                - qVeg * carbohydrateDict[meal[3]]
                - qFruit * carbohydrateDict[meal[4]]
                - carbohydrateDict[meal[5]] * extraDict[meal[5]],
                (0.22 * targetCal / 8.8)
                - qVeg * fatDict[meal[3]]
                - qFruit * fatDict[meal[4]]
                - fatDict[meal[5]] * extraDict[meal[5]],
            ]
        )
        coef = np.array(
            [
                [
                    proteinDict[meal[0]],
                    proteinDict[meal[1]],
                    proteinDict[meal[2]],
                ],
                [
                    carbohydrateDict[meal[0]],
                    carbohydrateDict[meal[1]],
                    carbohydrateDict[meal[2]],
                ],
                [fatDict[meal[0]], fatDict[meal[1]], fatDict[meal[2]]],
            ]
        )

        qValues = np.linalg.solve(coef, const)
        for elem in qValues:  # Test of no null values
            if elem < 0:
                return None
        self.productQuantity = [
            qValues[0],
            qValues[1],
            qValues[2],
            qVeg,
            qFruit,
            extraDict[meal[5]],
        ]
