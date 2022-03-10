import envimpact
import energyrequirement
import nutritionfacts
import pandas

if __name__ == "__main__":
    if input("Enter to skip : ") != "":
        statUser = energyrequirement.askStatUser()
    else:
        statUser = ["M", 20, 70, 170, "light"]
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
    envName = ["landUse", "ghgEmissions",
               "acidifyingEmissions", "eutrophyingEmissions",
               "stressWeightedWaterUse "]
    df_environment = pandas.read_excel(
        "DataS2.xlsx", 0,
        header=None, names=["products"] + envName,
        index_col=0, usecols="A,E,K,W,AC,AO",
        skiprows=lambda x: x in [0, 1, 2, 46, 47, 48, 49]
    )

    dict_environment = df_environment.to_dict("series")

    mealDict = nutritionfacts.dictByProduct_toDictByType(
        dict_nutritions["Type"])

    targetCal = energyrequirement.dailyEnergyRequirement(
        statUser[0], statUser[1], statUser[2], statUser[3], statUser[4])
    targetCal = 1800  # 'Beet Sugar': 0.012, 'Coffee': 0.008, 'Dark Chocolate': 0.020
    extraDict = nutritionfacts.extraQuantity(mealDict)

    mealAndQuantity = nutritionfacts.generateMeal(mealDict,  extraDict, targetCal*0.4,
                                                  dict_gProteinPerRetailUnit,
                                                  dict_gFatPerRetailUnit,
                                                  dict_gCarbPerRetailUnit)

    a = envimpact.mealListEnvimpact(mealAndQuantity, dict_environment, envName)
    print(a)
