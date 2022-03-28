from meal import Meal
import itertools
from nutrition_database import NutritionDataBase
from enivornmental_database import EnvironmentalDatabase
from environmental_impact import EnvironmentalImpact
from user import User
import matplotlib.pyplot as plt


class MealSet:
    def __init__(
        self,
        dataNutriment: NutritionDataBase,
        dataEnviron: EnvironmentalDatabase,
    ) -> None:
        self.dataNutrimentByProduct = dataNutriment.foodByTypeOfProduct
        self.dataNutrimentByRU = dataNutriment.foodByTypeOfRetailUnit
        self.dataEnvironmental = dataEnviron.envDict
        self.mealList = []

    def __repr__(self) -> str:
        return str(self.mealList)

    def computeMealList(self) -> list:
        for meal in list(
            itertools.product(
                self.dataNutrimentByProduct["ProteinSource"],
                self.dataNutrimentByProduct["CarbSource"],
                self.dataNutrimentByProduct["FatSource"],
                self.dataNutrimentByProduct["Vegetable"],
                self.dataNutrimentByProduct["Fruit"],
                self.dataNutrimentByProduct["Extra"],
            )
        ):
            initMeal = Meal(*meal)
            initMeal.computeQuantity(yo, self.dataNutrimentByRU)
            if initMeal.productQuantity != []:
                self.mealList.append(initMeal)
                initMeal.environmental5D = EnvironmentalImpact()
                initMeal.environmental5D.compute5D(
                    initMeal,
                    self.dataEnvironmental,
                    EnvironmentalDatabase.envName,
                )

    def printHistEnv(self, envData: EnvironmentalDatabase) -> None:
        dictEnv = {}
        for meal in self.mealList:
            for ind, unit in enumerate(envData.envName):
                if unit in dictEnv:
                    dictEnv[envData.envName[ind]].append(
                        meal.environmental5D.list5D[ind]
                    )
                else:
                    dictEnv[unit] = []
        for i in range(5):
            plt.subplot(3, 2, i + 1)
            plt.hist(dictEnv[envData.envName[i]])
            plt.title(envData.envName[i])
            plt.ylabel("Number of Meal")
            plt.xlabel(envData.envName[i])
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    yo = User()
    b = NutritionDataBase("data/TableS1_augmented_with_FAO_data.xlsx")
    c = EnvironmentalDatabase("data/DataS2.xlsx")
    print(c.envDict)
    b.loadNutriData()
    b.computeDictbyTypeOfProduct()
    b.computeDictByTypeOfRetailUnit()

    a = MealSet(b, c)
    yo.computeAllUserThing(a.dataNutrimentByProduct)
    a.computeMealList()
    yo.thresholdsEnvimpact(a, c)
