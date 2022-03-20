import envimpact
import energyrequirement
import nutritionfacts
from fileHandler import FileHandler
import os


if __name__ == "__main__":

    # ____ all import _____

    # 1. Import of nutrition

    nutriNames = [
        "gFatPerRetailUnit",
        "kcalPerRetailUnit",
        "gProteinPerRetailUnit",
        "gCarbPerRetailUnit",
    ]
    dictNutrition = nutritionfacts.loadNutriData(
        "TableS1_augmented_with_FAO_data.xlsx"
    )
    nutriDict = nutritionfacts.dictByType(dictNutrition, nutriNames)

    # 2. Import of env data
    envName = [
        "landUse",
        "ghgEmissions",
        "acidifyingEmissions",
        "eutrophyingEmissions",
        "stressWeightedWaterUse ",
    ]
    dict_environment = envimpact.loadEnvData(
        "DataS2.xlsx", envName, "A,E,K,W,AC,AO", [0, 1, 2, 46, 47, 48, 49]
    )

    # ____ use import _____

    mealDict = nutritionfacts.dictByProduct_toDictByType(dictNutrition["Type"])

    if (
        os.path.exists("userStat.json")
        and input("Do you want to select previous user data ? (y/n) : ")
        == "y".lower()
    ):
        statUser = FileHandler.loadData("userStat.json")
    else:
        # Basic statUser = ["M", 20, 70, 170, "light"] ou targetCal 2668
        statUser = energyrequirement.askStatUser()
        FileHandler.saveData("userStat.json", statUser)

    targetCal = energyrequirement.dailyEnergyRequirement(
        statUser[0], statUser[1], statUser[2], statUser[3], statUser[4]
    )
    print(f"Your needs are {targetCal} kCal")

    # Extradict example {"Barley (Beer)": 0.25, "Cane Sugar": 0.012,*
    # "Beet Sugar": 0.012, "Wine": 0.1,
    # "Coffee": 0.008, "Dark Chocolate": 0.02}

    if (
        os.path.exists("extraDict.json")
        and input("Do you want to select previous extra data ? (y/n) : ")
        == "y".lower()
    ):
        extraDict = FileHandler.loadData("extraDict.json")
    else:
        extraDict = nutritionfacts.extraQuantity(mealDict)
        FileHandler.saveData("extraDict.json", extraDict)

    mealAndQuantity = nutritionfacts.generateMeal(
        mealDict,
        extraDict,
        targetCal * 0.4,
        nutriDict["gFatPerRetailUnit"],
        nutriDict["gProteinPerRetailUnit"],
        nutriDict["gCarbPerRetailUnit"],
    )

    listOf_MealQuantity_Env = envimpact.mealListEnvimpact(
        mealAndQuantity, dict_environment, envName
    )

    thresholdValues = envimpact.thresholdsEnvimpact(listOf_MealQuantity_Env)
    goodMealList = envimpact.computeValidEnvMeal(
        listOf_MealQuantity_Env, thresholdValues
    )
    print(goodMealList[0])
    FileHandler.saveMealList("meal.txt", goodMealList)
