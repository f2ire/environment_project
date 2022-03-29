from nutrition_database import NutritionDataBase
from enivornmental_database import EnvironmentalDatabase
from user import User
from meal_set import MealSet
from meal import Meal

if __name__ == "__main__":

    b = NutritionDataBase("data/TableS1_augmented_with_FAO_data.xlsx")
    c = EnvironmentalDatabase("data/DataS2.xlsx")
    b.loadNutriData()
    b.computeDictbyTypeOfProduct()
    b.computeDictByTypeOfRetailUnit()

    a = MealSet(b, c)
    yo = User.chooseUser("user_file", a.dataNutrimentByProduct, True)

    yo.computeAllUserThing()
    a.computeMealList(yo.dailyEnergyRequirement * 0.4, yo.dictExtraQuantity)
    yo.thresholdsEnvimpact(a, c)
    print(len(a.mealList))
    a.updateMealList(yo)
    print(len(a.mealList))