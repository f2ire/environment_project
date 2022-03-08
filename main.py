
from os import stat
import envimpact
import energyrequirement
import nutritionfacts
import pandas

if __name__ == "__main__":
    statUser = energyrequirement.askStatUser()
    print(statUser)
    # compute dict for meal
    df_nutritions = pandas.read_excel(
        "TableS1_augmented_with_FAO_data.xlsx", 0, 0, index_col=0)
    dict_nutritions = df_nutritions.to_dict("series")
    # Compute dict
    dict_gFatPerRetailUnit = dict_nutritions["gFatPerRetailUnit"]
    dict_gkcalPerRetailUnit = dict_nutritions["kcalPerRetailUnit"]
    dict_gProteinPerRetailUnit = dict_nutritions["gProteinPerRetailUnit"]
    dict_gCarbPerRetailUnit = dict_nutritions["gCarbPerRetailUnit"]
    # compute dict for env
    df_envi = pandas.read_excel(
        "DataS2.xlsx", 0,
        header=None, names=["products", "landUse", "ghgEmissions",
                            "acidifyingEmissions", "eutrophyingEmissions",
                            "stressWeightedWaterUse "],
        index_col=0, usecols="A,E,K,W,AC,AO",
        skiprows=lambda x: x in [0, 1, 2, 46, 47, 48, 49]
    )
    mealDict = {
        "proteinSource": ["Tofu", "Bovine Meat (beef herd)",
                          "Poultry Meat", "Eggs"],
        "carbSource": ["Wheat & Rye(Bread)", "Maize (meal)", "Potatoes"],
        "fatSource": ["Rapeseed Oil", "Olive Oil"],
        "vegetable": ["Tomatoes", "Root Vegetables", "Other Vegetables"],
        "fruit": ["Bananas", "Apples", "Berries & Grapes"],
        "extraSource": ["Beet Sugar", "Coffee", "Dark Chocolate"]
    }
    # Calcul

    targetCal = energyrequirement.dailyEnergyRequirement(
        statUser[0], statUser[1], statUser[2], statUser[3], statUser[4])
    extraDict = nutritionfacts.extraQuantity(mealDict)

    mealAndQuantity = nutritionfacts.generateMeal(mealDict,  extraDict, targetCal,
                                                  nutritionfacts.proteinDict,
                                                  nutritionfacts.fatDict,
                                                  nutritionfacts.carbohydrateDict)
