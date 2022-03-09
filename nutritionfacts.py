import itertools

from pandas import melt
import tools
import numpy as np

# ______________________________________________________________________________
# Fonction :


def computeQuantity(targetCal: int, meal: list, extraDict: dict,
                    proteinDict: dict, fatDict: dict,
                    carbohydrateDict: dict) -> list:
    """
    Compute the quantity of g needed for the meal for each component
    and return a list [qProtSource, qCarbSource, qFatSource, qVegetable,"\
                qFruit, qExtra]
    """
    qVeg = 0.125
    qFruit = 0.05
    # 0 : prot, 1 carb, 2 : fat, 3 : vegetable, 4 : fruit, 5 : extras
    # b = [prot, carb, fat]
    const = np.array([
        (0.12*targetCal/4) -
        qVeg * proteinDict[meal[3]] -
        qFruit * proteinDict[meal[4]] -
        proteinDict[meal[5]] * extraDict[meal[5]],

        (0.66*targetCal/4) -
        qVeg * carbohydrateDict[meal[3]] -
        qFruit * carbohydrateDict[meal[4]] -
        carbohydrateDict[meal[5]] * extraDict[meal[5]],

        (0.22*targetCal/8.8) -
        qVeg * fatDict[meal[3]] -
        qFruit * fatDict[meal[4]] -
        fatDict[meal[5]]*extraDict[meal[5]]]
    )
    coef = np.array([[proteinDict[meal[0]],
                      proteinDict[meal[1]],
                      proteinDict[meal[2]]],
                     [carbohydrateDict[meal[0]],
                      carbohydrateDict[meal[1]],
                      carbohydrateDict[meal[2]]],
                     [fatDict[meal[0]],
                      fatDict[meal[1]],
                      fatDict[meal[2]]]])

    qValues = np.linalg.solve(coef, const)
    for elem in qValues:  # Test of no null values
        if elem < 0:
            return ValueError("This values can't satisfy a good meal, try to"
                              "change your extra consumption")
    return [qValues[0], qValues[1], qValues[2],
            qVeg, qFruit, extraDict[meal[5]]]


def generateMeal(mealDict: dict, extraDict: dict, targetCal: int,
                 protDict: dict, fatDict: dict, carbonDict: dict) -> list:
    """
    Generate a list of possible meal can be done with all meat given
    """
    listOfPossibleMeal = []
    for meal in list(itertools.product(mealDict["proteinSource"],
                                       mealDict["carbSource"],
                                       mealDict["fatSource"],
                                       mealDict["vegetable"],
                                       mealDict["fruit"],
                                       mealDict["extraSource"])):
        qMeal = computeQuantity(
            targetCal, meal, extraDict,
            protDict, fatDict, carbonDict)
        listOfPossibleMeal.append((meal, qMeal))

    return listOfPossibleMeal


def unitMealTest(mealDict: dict, listToTest: list) -> bool:
    """
    Return true is unit test is confirmet
    """
    count = 1
    for i in [len(j) for j in mealDict.value()]:
        count *= i
    return count == len(listToTest)


def mealComposition(meal: list, listQuantity: list, listOfDict: list) -> None:
    """
    Print the composition of the meal given
    """
    unity = ["kcal", "g protein", "g carb", "g fat"]
    total = [0]*len(unity)
    template = f'The meal is composed of : \n {"-":-^105}\n'
    for i in range(len(meal)):
        template += f'-   {listQuantity[i]}g of {meal[i]: >25},\
            contributing {"": ^5}'

        for j in range(len(listOfDict)):
            values = (listOfDict[j][meal[i]] * listQuantity[i])/1000
            template += f'{values: >5.1f} {unity[j]}'
            total[j] += values
            template += tools.comaIntoDot(j, len(listOfDict))
        template += "\n"

    template += f'{"-":-^105}\n TOTAL: {"": >43}'

    for i in range(len(unity)):
        template += f"{total[i]:.1f} {unity[i]}"
        template += tools.comaIntoDot(i, len(listOfDict))
    print(template+"\n")


def extraQuantity(mealDict: dict) -> dict:
    """
    Return a dict of quantity of extra in g given by the user.
    """
    dict_extraQuantity = {}
    extraSource = mealDict["extraSource"]
    it = 0
    while it < len(extraSource):
        extraQuestion = f"How much extra gramme of {extraSource[it]}"
        "do you need ? \n"
        extraAnswerError = "\nERROR :\n\nYou have to write a number"
        "superior of 0.\n"
        i_Extra = tools.floatInput(extraQuestion, extraAnswerError)
        if i_Extra >= 0:
            dict_extraQuantity[extraSource[it]] = i_Extra
            it += 1
        else:
            print(extraAnswerError)
    return dict_extraQuantity

# ______________________________________________________________________________
# Variable :


mealDict = {
    "proteinSource": ["Tofu", "Bovine Meat (beef herd)",
                      "Poultry Meat", "Eggs"],
    "carbSource": ["Wheat & Rye(Bread)", "Maize (meal)", "Potatoes"],
    "fatSource": ["Rapeseed Oil", "Olive Oil"],
    "vegetable": ["Tomatoes", "Root Vegetables", "Other Vegetables"],
    "fruit": ["Bananas", "Apples", "Berries & Grapes"],
    "extraSource": ["Beet Sugar", "Coffee", "Dark Chocolate"]
}

kcalDict = {
    "Wheat & Rye(Bread)": 2490,
    "Maize (meal)": 3630,
    "Potatoes": 670,
    "Beet Sugar": 3870,
    "Coffee": 560,
    "Dark Chocolate": 3930,
    "Rapeseed Oil": 8096,
    "Olive Oil": 8096,
    "Bananas": 600,
    "Apples": 480,
    "Berries & Grapes": 530,
    "Tofu": 765,
    "Bovine Meat (beef herd)": 1500,
    "Poultry Meat": 1220,
    "Eggs": 1630,
    "Tomatoes": 170,
    "Root Vegetables": 380,
    "Other Vegetables": 220
}
proteinDict = {
    "Wheat & Rye(Bread)": 82,
    "Maize (meal)": 84,
    "Potatoes": 16,
    "Beet Sugar": 0,
    "Coffee": 80,
    "Dark Chocolate": 42,
    "Rapeseed Oil": 0,
    "Olive Oil": 0,
    "Bananas": 7,
    "Apples": 1,
    "Berries & Grapes": 5,
    "Tofu": 82,
    "Bovine Meat (beef herd)": 185,
    "Poultry Meat": 123,
    "Eggs": 113,
    "Tomatoes": 8,
    "Root Vegetables": 9,
    "Other Vegetables": 14
}
fatDict = {
    "Wheat & Rye(Bread)": 12,
    "Maize (meal)": 12,
    "Potatoes": 1,
    "Beet Sugar": 0,
    "Coffee": 0,
    "Dark Chocolate": 357,
    "Rapeseed Oil": 920,
    "Olive Oil": 920,
    "Bananas": 3,
    "Apples": 3,
    "Berries & Grapes": 4,
    "Tofu": 42,
    "Bovine Meat (beef herd)": 79,
    "Poultry Meat": 77,
    "Eggs": 121,
    "Tomatoes": 2,
    "Root Vegetables": 2,
    "Other Vegetables": 2
}
carbohydrateDict = {
    "Wheat & Rye(Bread)": 514.1,
    "Maize (meal)": 797.1,
    "Potatoes": 149.3,
    "Beet Sugar": 967.5,
    "Coffee": 60,
    "Dark Chocolate": 155.1,
    "Rapeseed Oil": 0,
    "Olive Oil": 0,
    "Bananas": 136.4,
    "Apples": 112.4,
    "Berries & Grapes": 118.7,
    "Tofu": 16.85,
    "Bovine Meat (beef herd)": 16.2,
    "Poultry Meat": 12.6,
    "Eggs": 28.3,
    "Tomatoes": 30.1,
    "Root Vegetables": 81.6,
    "Other Vegetables": 36.6
}


# ______________________________________________________________________________
# Main Program :
if __name__ == "__main__":
    extra = extraQuantity(mealDict)
    listOfPossibleMeal = generateMeal(
        mealDict, extra, 1800, proteinDict, fatDict, carbohydrateDict)
    print(listOfPossibleMeal)

    # print(unitMealTest(mealDict, listOfPossibleMeal))

#         quantity = [39, 180, 16, 125, 50, 8]
#         listDict = [kcalDict, proteinDict, carbohydrateDict, fatDict]

#         meal = listOfPossibleMeal[345]

#         mealComposition(meal, quantity, listDict)

#         # print(listOfPossibleMeal)

#         dict_extraQuantity = extraQuantity(mealDict)

#         listQuantityComptued = computeQuantity(500, meal, dict_extraQuantity,
#                                                proteinDict, fatDict,
#                                                carbohydrateDict)

#         print(listQuantityComptued)
