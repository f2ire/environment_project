import math,numpy

def allPossibleMeal(allIngredients):
	"""
	Parameters in data mode: [all]
	Parameters in data/result mode : [none]
	Parameters in result mode : [none]
	Preconditions : 
    allIngredients (list of list of string) : list of list of ingredient to put in all meal sorted by ingredient category order. 
    One list per each ingredient category. Each ingredient category must contain at least one ingredient
	Postconditions : [none]
	Result : All meal combination as array
	"""
	iterator = []
	length = []
	maxCombination = 1
	for i in range(0,len(allIngredients)):
		length.append(len(allIngredients[i]))
		maxCombination *= len(allIngredients[i])
		iterator.append(0)

	finished = False
	mealsRecipient = []
	while not finished:
		currentMeal = []
		for i in range(0,len(allIngredients)):
			currentMeal.append(allIngredients[i][iterator[i]])
		mealsRecipient.append(currentMeal)
		iterator[len(iterator)-1] +=1
		for i in reversed(range(0,len(iterator))):
			if(iterator[i]==length[i]):
				if i==0:
					finished = True
				else:
					iterator[i] = 0
					iterator[i-1] += 1
	return mealsRecipient

def prettyPrintMeal(meal,kcalDict,proteinDict,carbohydrateDict,fatDict):
	"""
	  Parameters passed in data mode: [all]
	  Parameters passed in data/result mode: [none]
	  Parameters passed in result mode: [none]
	  Preconditions: 
	    - Foods is a list of strings containing (in this order): a source of protein, a source of carbs, a source of fat, a vegetable, a fruit, an extra
	    - Quantities is a list of floats containing the quantity for each food, in kg or L depending on food type
	    - both lists must have the same size
	    - each food listed in Foods mut exist as a key in KcalDict, GProtDict, GCarbDict, GFatDict
	  Postconditions: A nutritional description of the meal is printed to screen.
	  Result: [none]
	"""
	print("The meal is composed of :")
	layout = "- {0:>4.3f} kg of {1:>20}, contributing {2:>4.0f} kcal, {3:>6.1f} g protein, {4:>6.1f} g carb, {5:>6.1f} g fat"
	prettyPrint = "";
	sumKcal,sumProt,sumCarb,sumFat = 0,0,0,0
	for ingredient in meal:
		prettyPrint += '\n' + layout.format(ingredient["quantity"],ingredient["name"],kcalDict[ingredient["name"]]*ingredient["quantity"],proteinDict[ingredient["name"]]*ingredient["quantity"],carbohydrateDict[ingredient["name"]]*ingredient["quantity"],fatDict[ingredient["name"]]*ingredient["quantity"])
		sumKcal += kcalDict[ingredient["name"]]*ingredient["quantity"]
		sumProt += proteinDict[ingredient["name"]]*ingredient["quantity"]
		sumCarb += carbohydrateDict[ingredient["name"]]*ingredient["quantity"]
		sumFat += fatDict[ingredient["name"]]*ingredient["quantity"]
	dash = "-"*math.floor(((len(prettyPrint)-(2*len(meal)))/len(meal))+1);
	prettyPrint = dash + prettyPrint + "\n" + dash
	layoutTotal = "{0:<49} {1:>4.0f} kcal, {2:>6.1f} g protein, {3:>6.1f} g carb, {4:>6.1f} g fat"
	prettyPrint += "\n"+layoutTotal.format("TOTAL",sumKcal,sumProt,sumCarb,sumFat)
	print(prettyPrint)

def inputDefaultQuantity(ingredients,default=0):
	"""
	Parameters passed in data mode: [all]
	Parameters passed in data/result mode: [none]
	Parameters passed in result mode: [none]
	Preconditions: 
	ingredients (list of string) : is a list of ingredient for which you want to ask quantity
	Postconditions (alterations of program state outside this function): [none]
	Returned result: a dictionary associating the typical serving size (asked to the user)
	"""
	dic = {}
	for ingredient in ingredients:
		if default==0:
			inp = input("Inserer la quantité de "+ingredient+" habituellement consommes (en g)\n")
		else:
			inp = default
		dic[ingredient] = float(inp)/1000;
	return dic

def processQuantity(ingredients,targetKcal,kcalDict,proteinDict,carbohydrateDict,fatDict,extraDict):
	"""
  Parameters passed in data mode: [all]
  Parameters passed in data/result mode: [none]
  Parameters passed in result mode: [none]
  Preconditions: 
    - Foods is a list of 6 strings containing the components of a meal: a source of proteins, a source of carbohydrates,
      a source of fat, a vegetable, a fruit and an extra (in this order)
    - Each meal component in Foods must exist as a key in proteinDict, carbohydrateDict, fatDict, and in kcalDict
    - The extra (last item in Foods) must exist as a key in extraDict
  Postconditions: an Exception is raised if we cannot reach targetKcal with positive quantities of each component.
  Result: A list of 6 floats corresponding to the quantity of each component that allows to:
    - reach exactly targetKcal kcal for the whole meal
    - have 125g of vegetable
    - have 50g of fruit
    - have the extra quantity defined in extraDict
    - have 12% of meal kcal should come from proteins
    - have 63% of meal kcal should come from carbs
    - have 25% of meal kcal should come from fat
	"""
	proteinSource = ingredients[0]
	carbSource = ingredients[1]
	fatSource = ingredients[2]
	vegetableSource = ingredients[3]
	fruitSource = ingredients[4]
	extraSource = ingredients[5]

	qVegetable = 0.125
	qFruit = 0.050
	qExtra = extraDict[extraSource]

	matB = numpy.array([
	targetKcal * 0.12 - 4 * qVegetable * proteinDict[vegetableSource] - 4 * qFruit * proteinDict[fruitSource] - 4 * qExtra * proteinDict[extraSource],
	targetKcal * 0.63 - 4 * qVegetable * carbohydrateDict[vegetableSource] - 4 * qFruit * carbohydrateDict[fruitSource] - 4 * qExtra * carbohydrateDict[extraSource],
	targetKcal * 0.25 - 8.8 * qVegetable * fatDict[vegetableSource] - 8.8 * qFruit * fatDict[fruitSource] - 8.8 * qExtra * fatDict[extraSource]
	])
	matA = numpy.array([
		[4 * proteinDict[proteinSource], 4 * proteinDict[carbSource], 4 *proteinDict[fatSource]],
		[4 * carbohydrateDict[proteinSource], 4 * carbohydrateDict[carbSource], 4 *carbohydrateDict[fatSource]],
		[8.8 * fatDict[proteinSource], 8.8 * fatDict[carbSource], 8.8 *fatDict[fatSource]]
		])
	x = numpy.linalg.solve(matA,matB)
	qProt = x[0]
	qCarb = x[1]
	qFat = x[2]
	if qProt < 0 or qCarb < 0 or qFat < 0:
		raise Exception("Impossible to satisfy the nutritional constraints with this meal ("+ingredients+"). Maybe you can think about changing your Extra consumption")

	kcalAmount = qProt * kcalDict[proteinSource] + qCarb * kcalDict[carbSource] + qFat * kcalDict[fatSource] + qVegetable * kcalDict[vegetableSource] + qFruit * kcalDict[fruitSource] + qExtra * kcalDict[extraSource]

	return [qProt,qCarb,qFat,qVegetable,qFruit,qExtra]

def computeAllMenus(allIngredients,targetKcal,kcalDict,proteinDict,carbohydrateDict,fatDict,extraDict):
	meals = allPossibleMeal(allIngredients)
	menus = []
	quantity = []
	for meal in meals:
		try:
			quantity.append(processQuantity(meal,targetKcal,kcalDict,proteinDict,carbohydrateDict,fatDict,extraDict))
			menus.append(meal)
		except Exception:
			continue
	computedMenus = []
	for iMenu in range(0,len(menus)):
		computedMenu = []
		for iIngredient in range(0,len(menus[0])):
			ingredient = {"name":menus[iMenu][iIngredient],"quantity":quantity[iMenu][iIngredient]}
			computedMenu.append(ingredient)
		computedMenus.append(computedMenu)
	return computedMenus

if __name__ == "__main__":
	proteinSource = ["Tofu","Bovine Meat (beef herd)","Poultry Meat","Eggs"]
	carbSource = ["Wheat & Rye(Bread)","Maize (meal)","Potatoes"]
	fatSource = ["Rapeseed Oil","Olive Oil"]
	vegetable = ["Tomatoes","Root Vegetables","Other Vegetables"]
	fruit = ["Bananas","Apples","Berries & Grapes"]
	extra = ["Beet Sugar","Coffee","Dark Chocolate"]
	allIngredients = []
	allIngredients.extend([proteinSource,carbSource,fatSource,vegetable,fruit,extra])

	kcalDict = {
		"Wheat & Rye(Bread)":2490,
		"Maize (meal)":3630,
		"Potatoes":670,
		"Beet Sugar":3870,
		"Coffee":560,
		"Dark Chocolate":3930,
		"Rapeseed Oil":8096,
		"Olive Oil":8096,
		"Bananas":600,
		"Apples":480,
		"Berries & Grapes":530,
		"Tofu":765,
		"Bovine Meat (beef herd)":1500,
		"Poultry Meat":1220,
		"Eggs":1630,
		"Tomatoes":170,
		"Root Vegetables":380,
		"Other Vegetables":220
	}
	proteinDict = {
		"Wheat & Rye(Bread)":82,
		"Maize (meal)":84,
		"Potatoes":16,
		"Beet Sugar":0,
		"Coffee":80,
		"Dark Chocolate":42,
		"Rapeseed Oil":0,
		"Olive Oil":0,
		"Bananas":7,
		"Apples":1,
		"Berries & Grapes":5,
		"Tofu":82,
		"Bovine Meat (beef herd)":185,
		"Poultry Meat":123,
		"Eggs":113,
		"Tomatoes":8,
		"Root Vegetables":9,
		"Other Vegetables":14
	}
	fatDict = {
		"Wheat & Rye(Bread)":12,
		"Maize (meal)":12,
		"Potatoes":1,
		"Beet Sugar":0,
		"Coffee":0,
		"Dark Chocolate":357,
		"Rapeseed Oil":920,
		"Olive Oil":920,
		"Bananas":3,
		"Apples":3,
		"Berries & Grapes":4,
		"Tofu":42,
		"Bovine Meat (beef herd)":79,
		"Poultry Meat":77,
		"Eggs":121,
		"Tomatoes":2,
		"Root Vegetables":2,
		"Other Vegetables":2
	}
	carbohydrateDict = {
		"Wheat & Rye(Bread)":514.1,
		"Maize (meal)":797.1,
		"Potatoes":149.3,
		"Beet Sugar":967.5,
		"Coffee":60,
		"Dark Chocolate":155.1,
		"Rapeseed Oil":0,
		"Olive Oil":0,
		"Bananas":136.4,
		"Apples":112.4,
		"Berries & Grapes":118.7,
		"Tofu":16.85,
		"Bovine Meat (beef herd)":16.2,
		"Poultry Meat":12.6,
		"Eggs":28.3,
		"Tomatoes":30.1,
		"Root Vegetables":81.6,
		"Other Vegetables":36.6
	}



	allMeals = allPossibleMeal(allIngredients)
	
	prettyPrintMeal([{
		"name":"Wheat & Rye(Bread)",
		"quantity":0.04
		},{
		"name":"Eggs",
		"quantity":0.04
		},{
		"name":"Tomatoes",
		"quantity":0.04
		},{
		"name":"Coffee",
		"quantity":0.04
		},
		],kcalDict,proteinDict,carbohydrateDict,fatDict)


	extraDict = {"Beet Sugar":0.01,"Coffee":0.01,"Dark Chocolate":0.01}
	sMeal = allMeals[239]
	quantity = processQuantity(sMeal,800,kcalDict,proteinDict,carbohydrateDict,fatDict,extraDict)
	#print(quantity)
	computedMeal = []
	for i in range(0,len(sMeal)):
		ingredient = {"name":sMeal[i],"quantity":quantity[i]}
		computedMeal.append(ingredient)
	#prettyPrintMeal(computedMeal,kcalDict,proteinDict,carbohydrateDict,fatDict)


	'''
		UNIT TEST CASE
	'''
	#allPossibleMeal()
	countCombination = 1
	for i in range(0,len(allIngredients)):
		countCombination *= len(allIngredients[i])
	firstMeal = allMeals[0] * 1
	lastMeal = allMeals[len(allMeals)-1] * 1
	print("Test 1 : function `allPossibleMeal()` : "+ ("passed" if firstMeal!=lastMeal else "error"))
	print("Test 2 : function `allPossibleMeal()` : "+ ("passed" if countCombination==len(allMeals) else "error"))
