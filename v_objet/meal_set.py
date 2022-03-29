from turtle import update
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
        self.mealList: list[Meal] = []

    def __repr__(self) -> str:
        return str(self.mealList)

    def updateMealList(self, user: User):
        for meal in self.mealList:
            if meal.isPossible:
                if meal.isImpactTooBig(user.threshold):
                    # print("-1")
                    self.mealList.remove(meal)
            else:
                # print("-&")
                self.mealList.remove(meal)
            print("zezqd")

    def computeMealList(self, targetCal, extraDict) -> list:
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
            initMeal.computeQuantity(
                targetCal, extraDict, self.dataNutrimentByRU
            )
            if initMeal.isPossible:
                self.mealList.append(initMeal)
                initMeal.environmental5D = EnvironmentalImpact(
                    initMeal,
                    self.dataEnvironmental,
                    EnvironmentalDatabase.envName,
                )
        if self.mealList == []:
            exit("No meal avalaible")

    def printHistEnv(self, envData: EnvironmentalDatabase) -> None:
        dictEnv = {}
        for meal in self.mealList:
            for ind, unit in enumerate(envData.envName):
                if unit in dictEnv:
                    dictEnv[unit].append(
                        list(meal.environmental5D.dict5D.values())[ind]
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

    b = NutritionDataBase("data/TableS1_augmented_with_FAO_data.xlsx")
    c = EnvironmentalDatabase("data/DataS2.xlsx")
    print(c.envDict)
    b.loadNutriData()
    b.computeDictbyTypeOfProduct()
    b.computeDictByTypeOfRetailUnit()

    a = MealSet(b, c)
    yo = User.chooseUser("user_file", a.dataNutrimentByProduct, True)

    yo.computeAllUserThing()
    a.computeMealList()
    yo.thresholdsEnvimpact(a, c)
