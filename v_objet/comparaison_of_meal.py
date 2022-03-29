from environmental_impact import EnvironmentalImpact
from nutrition_database import NutritionDataBase
from enivornmental_database import EnvironmentalDatabase
from meal import Meal

if __name__ == "__main__":

    b = NutritionDataBase("data/TableS1_augmented_with_FAO_data.xlsx")
    c = EnvironmentalDatabase("data/DataS2.xlsx")
    b.loadNutriData()
    b.computeDictByTypeOfRetailUnit()

    mealA = Meal(
        "Bovine Meat (beef herd)",
        "Rice",
        "Rapeseed Oil",
        "Brassicas",
        "Apples",
        "Beet Sugar",
    )

    mealB = Meal(
        "Tofu", "Rice", "Rapeseed Oil", "Brassicas", "Apples", "Beet Sugar"
    )
    mL = [mealA, mealB]
    mealA.computeQuantity(803, {"Beet Sugar": 0}, b.foodByTypeOfRetailUnit)
    mealB.computeQuantity(803, {"Beet Sugar": 0}, b.foodByTypeOfRetailUnit)

    for number, m in enumerate(mL):
        if m.isPossible:
            print(EnvironmentalImpact(m, c.envDict, c.envName))
        else:
            print(f"Meal number {number+1} is not possible")
