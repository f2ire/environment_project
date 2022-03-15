import unittest
import envimpact
import energyrequirement
import nutritionfacts
import matplotlib as plt

if __name__ == "__main__":

    # ____ all import _____

    # 1. Import of nutrition

    nutriNames = ["gFatPerRetailUnit", "kcalPerRetailUnit",
                  "gProteinPerRetailUnit", "gCarbPerRetailUnit"]
    dictNutrition = nutritionfacts.loadNutriData(
        "TableS1_augmented_with_FAO_data.xlsx")
    nutriDict = nutritionfacts.dictByType(dictNutrition, nutriNames)

    # 2. Import of env data
    envName = ["landUse", "ghgEmissions",
               "acidifyingEmissions", "eutrophyingEmissions",
               "stressWeightedWaterUse "]
    dict_environment = envimpact.loadEnvData(
        "DataS2.xlsx", envName, "A,E,K,W,AC,AO", [0, 1, 2, 46, 47, 48, 49])

    # ____ use import _____

    mealDict = nutritionfacts.dictByProduct_toDictByType(
        dictNutrition["Type"])

    isNotUnitTest = input("Enter to use unit test") != ""
    if isNotUnitTest:
        statUser = energyrequirement.askStatUser()
        targetCal = energyrequirement.dailyEnergyRequirement(
            statUser[0], statUser[1], statUser[2], statUser[3], statUser[4])
        extraDict = nutritionfacts.extraQuantity(mealDict)

    else:
        statUser = ["M", 20, 70, 170, "light"]
        targetCal = 1800
        extraDict = {"Barley (Beer)": 0.25, "Cane Sugar": 0.012,
                     "Beet Sugar": 0.012, "Wine": 0.1,
                     "Coffee": 0.008, "Dark Chocolate": 0.02}

    mealAndQuantity = \
        nutritionfacts.generateMeal(mealDict,  extraDict, targetCal*0.4,
                                    nutriDict["gFatPerRetailUnit"],
                                    nutriDict["gProteinPerRetailUnit"],
                                    nutriDict["gCarbPerRetailUnit"],
                                    isNotUnitTest)

    listOf_MealQuantity_Env = envimpact.mealListEnvimpact(
        mealAndQuantity, dict_environment, envName)

    test = listOf_MealQuantity_Env[0]
    print(isNotUnitTest)
    a = envimpact.thresholdsEnvimpact(listOf_MealQuantity_Env, isNotUnitTest)
    print(a)
