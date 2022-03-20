from json import tool
import matplotlib.pyplot as plt
import nutritionfacts
import pandas
import tools

# ______________________________________________________________________________
# Fonction :


def loadEnvData(dataPath: str, envName: list, columnsToSelect: str, lineToDontSelect: list) -> dict:
    df_environment = pandas.read_excel(
        dataPath, 0,
        header=None, names=["products"] + envName,
        index_col=0, usecols=columnsToSelect,
        skiprows=lambda x: x in lineToDontSelect
    )
    return df_environment.to_dict("series")


def mealEnvimpact(meal: list, listOfDico: list, listQuantity) -> list:
    totalList = [0]*len(listOfDico)
    for j in range(len(meal)):
        for i in range(len(listOfDico)):
            totalList[i] += listQuantity[j] * listOfDico[i][meal[j]]
    return [i for i in totalList]


def mealListEnvimpact(listMeal: list, envDict: dict,
                      envTypeList: list) -> list:
    dictList = [envDict[i] for i in envTypeList]
    listMeal_Envimpact = []
    for meal in listMeal:
        listMeal_Envimpact.append(
            (meal, mealEnvimpact(meal[0], dictList, meal[1])))
    return listMeal_Envimpact


def printEnvimpact(listEnvimpact: list) -> None:
    unitList = ["square meters of land.",
                "kg CO2 eq. (greenhouse gas emissions).",
                "g SO2 eq. (acidifying emissions).",
                "g PO43- eq. (entrophying emissions). ",
                "L of freshwater"]
    template = f'{"#":#^50}\n# Environmental impact #\n {"#":#^50}\n'
    for i in range(len(unitList)):
        if i in (0, 4):
            template += 'This meal uses\t'
        else:
            template += 'This meal emits\t'
        template += f'{listEnvimpact[i]:.1f} {unitList[i]}\n'
    print(template)


def thresholdsEnvimpact(listMeal: list, isUnitTest: bool) -> list:
    # _______ Init var _________
    unitList = ["meters of land",
                "greenhouse gas emissions",
                "acidifying emissions",
                "entrophying emissions",
                "freshwater used"]
    units = ["m2/FU", "kg CO2eq/FU", "g SO2eq/FU", "g PO43-eq/FU", "L/FU"]
    # Check if unittest
    printHistEnv(listMeal, unitList, units)
    if not isUnitTest:
        thresholdsList = [1, 1, 5, 5, 1000]
    else:
        thresholdsList = [tools.floatInput(f"What is the limite of {name} : ,",
                                           "Please write a float")
                          for name in unitList]
    return thresholdsList


def computeValidEnvMeal(listMeal: list, thresholdsList: list) -> list:
    goodMeal = []
    nbImpossible = 0
    for meal in listMeal:
        i = 0
        noEnv = False
        while i < (len(meal[1])-1) and not noEnv:
            if meal[1][i] > thresholdsList[i]:
                noEnv = True
                nbImpossible += 1
                i += 1
            else:
                i += 1
        if not noEnv:
            goodMeal.append(meal)
    print(
        f"There are {nbImpossible} more impossible meal \n"
        f"But there now {len(listMeal)-nbImpossible} possible meal")
    return goodMeal

    # template = f'{"-":-^105}\n'
    # for i in range(len(listEnvimpact)):
    #     isEnvGood.append(listEnvimpact[i] >= thresholdsList[i])
    #     if isEnvGood[i]:
    #         template += f"The amount of {unitList[i]} is too big\n"
    #     else:
    #         template += f"The amount of {unitList[i]} is correct\n"
    # template += f'{"-":-^105}\n'
    # print(template)


def printHistEnv(listMeal: list, unit: list, unitOfUnit: list) -> None:
    dictEnv = {}
    for name in unit:
        dictEnv[name] = []
    # Dans l'ordre de l'unitlist
    for meal in listMeal:
        for i in range(len(meal[1])):
            dictEnv[unit[i]].append(meal[1][i])
    for i in range(5):
        plt.subplot(3, 2, i+1)
        plt.hist(dictEnv[unit[i]])
        plt.title(unit[i])
        plt.ylabel("Number of Meal")
        plt.xlabel(unitOfUnit[i])
    plt.tight_layout()
    plt.show()


# ______________________________________________________________________________
# Variable :
if __name__ == "__main__":

    landDict = {
        "Wheat & Rye(Bread)": 2.7,
        "Maize (meal)": 1.8,
        "Potatoes": 0.8,
        "Beet Sugar": 1.5,
        "Tofu": 3.4,
        "Rapeseed Oil": 9.4,
        "Olive Oil": 17.3,
        "Tomatoes": 0.2,
        "Root Vegetables": 0.3,
        "Other Vegetables": 0.2,
        "Bananas": 1.4,
        "Apples": 0.5,
        "Berries & Grapes": 2.6,
        "Coffee": 11.9,
        "Dark Chocolate": 53.8,
        "Bovine Meat (beef herd)": 170.4,
        "Poultry Meat": 11.0,
        "Eggs": 5.7
    }
    ghgEmDict = {
        "Wheat & Rye(Bread)": 1.3,
        "Maize (meal)": 1.2,
        "Potatoes": 0.5,
        "Beet Sugar": 1.8,
        "Tofu": 2.6,
        "Rapeseed Oil": 3.5,
        "Olive Oil": 5.1,
        "Tomatoes": 0.7,
        "Root Vegetables": 0.4,
        "Other Vegetables": 0.4,
        "Bananas": 0.8,
        "Apples": 0.4,
        "Berries & Grapes": 1.4,
        "Coffee": 8.2,
        "Dark Chocolate": 5.0,
        "Bovine Meat (beef herd)": 60.4,
        "Poultry Meat": 7.5,
        "Eggs": 4.2
    }
    acidEmDict = {
        "Wheat & Rye(Bread)": 13.3,
        "Maize (meal)": 10.2,
        "Potatoes": 3.6,
        "Beet Sugar": 12.4,
        "Tofu": 6.0,
        "Rapeseed Oil": 23.2,
        "Olive Oil": 33.9,
        "Tomatoes": 5.2,
        "Root Vegetables": 2.9,
        "Other Vegetables": 3.7,
        "Bananas": 6.1,
        "Apples": 4.0,
        "Berries & Grapes": 6.9,
        "Coffee": 87.2,
        "Dark Chocolate": 29.0,
        "Bovine Meat (beef herd)": 270.9,
        "Poultry Meat": 64.7,
        "Eggs": 54.2
    }
    eutEmDict = {
        "Wheat & Rye(Bread)": 5.4,
        "Maize (meal)": 2.4,
        "Potatoes": 4.4,
        "Beet Sugar": 4.3,
        "Tofu": 6.6,
        "Rapeseed Oil": 16.4,
        "Olive Oil": 39.1,
        "Tomatoes": 1.9,
        "Root Vegetables": 1,
        "Other Vegetables": 1.8,
        "Bananas": 2.1,
        "Apples": 2.0,
        "Berries & Grapes": 1,
        "Coffee": 49.9,
        "Dark Chocolate": 67.3,
        "Bovine Meat (beef herd)": 320.7,
        "Poultry Meat": 34.5,
        "Eggs": 21.3
    }
    waterDict = {
        "Wheat & Rye(Bread)": 12822,
        "Maize (meal)": 350,
        "Potatoes": 78,
        "Beet Sugar": 115,
        "Tofu": 32,
        "Rapeseed Oil": 14,
        "Olive Oil": 24396,
        "Tomatoes": 4481,
        "Root Vegetables": 38,
        "Other Vegetables": 2940,
        "Bananas": 31,
        "Apples": 1025,
        "Berries & Grapes": 16245,
        "Coffee": 341,
        "Dark Chocolate": 220,
        "Bovine Meat (beef herd)": 441,
        "Poultry Meat": 334,
        "Eggs": 18621
    }


# ______________________________________________________________________________
# Main program :

    # listOfDico = [landDict, ghgEmDict, acidEmDict, eutEmDict, waterDict]
    # listOfEnvimpact = mealEnvimpact(
    #     nutritionfacts.listOfPossibleMeal[345], listOfDico,
    #     nutritionfacts.quantity)

    # printEnvimpact(listOfEnvimpact)

    # thresholds = [1, 0.5, 4, 2, 1000]

    # isGoodEnv = thresholdsEnvimpact(thresholds, listOfEnvimpact)
    pass
