import basics

# ______________________________________________________________________________
# Fonction :



def generateMeal(mealList: list) -> list:
    """
    Generate a list of possible meal can be done with all meat given 
    """
    listOfPossibleMeal = []
    for prot in mealList[0]:
        for carb in mealList[1]:
            for fat in mealList[2]:
                for vege in mealList[3]:
                    for fruit in mealList[4]:
                        for extra in mealList[5]:
                            listOfPossibleMeal.append(
                                [prot, carb, fat, vege, fruit, extra])
    return listOfPossibleMeal


def unitMealTest(mealList: list, listToTest: list) -> bool:
    """
    Return true is unit test is confirmet
    """
    count = 1
    for i in [len(j) for j in mealList]:
        count *= i
    return count == len(listToTest)


def mealComposition(meal: list, listQuantity: list, listOfDict: list) -> None:
    unity = ["kcal", "g protein", "g carb", "g fat"]
    total = [0]*len(unity)
    template = f'The meal is composed of : \n {"-":-^105}\n'
    for i in range(len(meal)):
        template += f'-   {listQuantity[i]}g of {meal[i]: >25}, contributing {"": ^5}'
        for j in range(len(listOfDict)):
            values = (listOfDict[j][meal[i]] * listQuantity[i])/1000
            template += f'{values: >5.1f} {unity[j]}'
            total[j] += values
            template += basics.comaIntoDot(j,len(listOfDict))
        template += "\n"
    template += f'{"-":-^105}\n TOTAL: {"": >43}'
    for i in range(len(unity)):
        template += f"{total[i]:.1f} {unity[i]}"
        template += basics.comaIntoDot(i,len(listOfDict))
    print(template+"\n")
# ______________________________________________________________________________
# Variable :


proteinSource = ["Tofu", "Bovine Meat (beef herd)", "Poultry Meat", "Eggs"]
carbSource = ["Wheat & Rye(Bread)", "Maize (meal)", "Potatoes"]
fatSource = ["Rapeseed Oil", "Olive Oil"]
vegetable = ["Tomatoes", "Root Vegetables", "Other Vegetables"]
fruit = ["Bananas", "Apples", "Berries & Grapes"]
extra = ["Beet Sugar", "Coffee", "Dark Chocolate"]

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

listElem = [proteinSource, carbSource, fatSource, vegetable, fruit, extra]

listOfPossibleMeal = generateMeal(listElem)

# print(unitMealTest(listElem, listOfPossibleMeal))

a = 3
quantity = [39, 180, 16, 125, 50, 8]
listDict = [kcalDict, proteinDict, carbohydrateDict, fatDict]

mealComposition(listOfPossibleMeal[345], quantity, listDict)

# print(listOfPossibleMeal)
