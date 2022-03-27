from meal import Meal
import itertools
from nutrition_database import NutritionDataBase
from enivornmental_database import EnvironmentalDatabase
from environmental_impact import EnvironmentalImpact
from user import User


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
                env = EnvironmentalImpact
                env.compute5D(
                    initMeal,
                    self.dataEnvironmental,
                    EnvironmentalDatabase.envName,
                )
                initMeal.environmental5D = env
            print(initMeal)


if __name__ == "__main__":
    yo = User()
    b = NutritionDataBase("v_objet/data/TableS1_augmented_with_FAO_data.xlsx")
    c = EnvironmentalDatabase("v_objet/data/DataS2.xlsx")
    print(c.envDict)
    b.loadNutriData()
    b.computeDictbyTypeOfProduct()
    b.computeDictByTypeOfRetailUnit()

    a = MealSet(b, c)
    yo.computeAllUserThing(a.dataNutrimentByProduct)
    a.computeMealList()
