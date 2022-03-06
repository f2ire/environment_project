import matplotlib.pyplot as plt
import numpy as np


def computeFootprint(meal,landDict,ghgEmDict,acidEmDict,eutEmDict,waterDict):
	"""
    Parameters in data mode: [all]
    Parameters in data/result mode : [none]
    Parameters in result mode : [none]
    Preconditions : 
	meal (object list) list of object containing name and quantity for each ingredient of the meal
	landDict (float dictionnary) dictionnary which bind ingredient name with his per unit land use
	ghgEmDict (float dictionnary) dictionnary which bind ingredient name with his per unit greenhouse gas emissions
	acidEmDict (float dictionnary) dictionnary which bind ingredient name with his per unit acidifying emissions
	eutEmDict (float dictionnary) dictionnary which bind ingredient name with his per unit eutrophying emissions
	waterDict (float dictionnary) dictionnary which bind ingredient name with his per unit fresh water consumption
    Postconditions : [none]
    Result : (float list) sum of the meal footprint in the following order Land Uses, Greehouse gas emissions, Acidifying emissions, Eutrophying emissions, Freshwater
	"""
	sumLand,sumGhg,sumAcid,sumEut,sumWater = 0,0,0,0,0
	for ingredient in meal:
		sumLand += landDict[ingredient["name"]]*ingredient["quantity"]
		sumGhg += ghgEmDict[ingredient["name"]]*ingredient["quantity"]
		sumAcid += acidEmDict[ingredient["name"]]*ingredient["quantity"]
		sumEut += eutEmDict[ingredient["name"]]*ingredient["quantity"]
		sumWater += waterDict[ingredient["name"]]*ingredient["quantity"]
	return [sumLand,sumGhg,sumAcid,sumEut,sumWater]

def computeAllFootprint(meals,landDict,ghgEmDict,acidEmDict,eutEmDict,waterDict):
	footprints = []
	for meal in meals:
		footprints.append(computeFootprint(meal,landDict,ghgEmDict,acidEmDict,eutEmDict,waterDict))
	return footprints

def displayFootprint(footprints):
	npFootprints = np.array(footprints)
	figure, axis = plt.subplots(2, 3)
	axis[0,0].hist(npFootprints[:,0])
	axis[0,0].set_title("Land Use")
	axis[0,1].hist(npFootprints[:,1])
	axis[0,1].set_title("GHG Emissions")
	axis[0,2].hist(npFootprints[:,2])
	axis[0,2].set_title("Acidifying Emissions")
	axis[1,0].hist(npFootprints[:,3])
	axis[1,0].set_title("Eutrophying Emissions")
	axis[1,1].hist(npFootprints[:,4])
	axis[1,1].set_title("Freshwater consumption")
	plt.show()

def checkFootprintTreshold(values,treshold):
	if len(values) != len(treshold):
		raise "Parameters don't have the same length"
	for i in range(0,len(values)):
		if values[i] > treshold[i]:
			return False
	return True

def filterMenusWithTreshold(menus,footprints,maxLandUse,maxGhgEm,maxAcidEm,maxEutEm,maxWaterUser):
	if len(menus) != len(footprints):
		raise "Menus and footprints don't have the same length"
	treshold = [maxLandUse,maxGhgEm,maxAcidEm,maxEutEm,maxWaterUser]
	checkedMenus = []
	for iMenu in range(0,len(menus)):
		if checkFootprintTreshold(footprints[iMenu],treshold):
			checkedMenus.append(menus[iMenu])
	return checkedMenus
def printFootprint(values):
	"""
    Parameters in data mode: [all]
    Parameters in data/result mode : [none]
    Parameters in result mode : [none]
    Preconditions : 
	values (float list) in the following order Land Uses, Greehouse gas emissions, Acidifying emissions, Eutrophying emissions, Freshwater
    Postconditions : [none]
    Result : pretty print footprint based on value
    """
	print("########################")
	print("# Environmental impact #")
	print("########################")
	print("This meal uses  {0:>6.1f} square meters of land.".format(values[0]));
	print("This meal emits {0:>6.1f} kg CO2 eq. (greenhouse gas emissions).".format(values[1]));
	print("This meal emits {0:>6.1f} g SO2 eq. (acidifying emissions).".format(values[2]));
	print("This meal emits {0:>6.1f} PO43- eq. (eutrophying emissions)".format(values[3]));
	print("This meal uses  {0:>6.1f} L of freshwater.".format(values[4]));

def compareFloat(x,y,e=0.000001):
    """
    Parameters in data mode: [all]
    Parameters in data/result mode : [none]
    Parameters in result mode : [none]
    Preconditions : 
    x (float)
    y (float)
    [e optionnal (float)] 
    Postconditions : [none]
    Result : Basal Metabolic rate as float
    """
    if (x==y):
        return True;
    elif(y==0):
        return abs(x-y) < e;
    else:
        return abs(x-y)/abs(y) < e;
if __name__ == "__main__":
	landDict = {
		"Wheat & Rye(Bread)":2.7,
		"Maize (meal)":1.8,
		"Potatoes":0.8,
		"Beet Sugar":1.5,
		"Tofu":3.4,
		"Rapeseed Oil":9.4,
		"Olive Oil":17.3,
		"Tomatoes":0.2,
		"Root Vegetables":0.3,
		"Other Vegetables":0.2,
		"Bananas":1.4,
		"Apples":0.5,
		"Berries & Grapes":2.6,
		"Coffee":11.9,
		"Dark Chocolate":53.8,
		"Bovine Meat (beef herd)":170.4,
		"Poultry Meat":11.0,
		"Eggs":5.7
	}
	ghgEmDict = {
		"Wheat & Rye(Bread)":1.3,
		"Maize (meal)":1.2,
		"Potatoes":0.5,
		"Beet Sugar":1.8,
		"Tofu":2.6,
		"Rapeseed Oil":3.5,
		"Olive Oil":5.1,
		"Tomatoes":0.7,
		"Root Vegetables":0.4,
		"Other Vegetables":0.4,
		"Bananas":0.8,
		"Apples":0.4,
		"Berries & Grapes":1.4,
		"Coffee":8.2,
		"Dark Chocolate":5.0,
		"Bovine Meat (beef herd)":60.4,
		"Poultry Meat":7.5,
		"Eggs":4.2
	}
	acidEmDict = {
		"Wheat & Rye(Bread)":13.3,
		"Maize (meal)":10.2,
		"Potatoes":3.6,
		"Beet Sugar":12.4,
		"Tofu":6.0,
		"Rapeseed Oil":23.2,
		"Olive Oil":33.9,
		"Tomatoes":5.2,
		"Root Vegetables":2.9,
		"Other Vegetables":3.7,
		"Bananas":6.1,
		"Apples":4.0,
		"Berries & Grapes":6.9,
		"Coffee":87.2,
		"Dark Chocolate":29.0,
		"Bovine Meat (beef herd)":270.9,
		"Poultry Meat":64.7,
		"Eggs":54.2
	}
	eutEmDict = {
		"Wheat & Rye(Bread)":5.4,
		"Maize (meal)":2.4,
		"Potatoes":4.4,
		"Beet Sugar":4.3,
		"Tofu":6.6,
		"Rapeseed Oil":16.4,
		"Olive Oil":39.1,
		"Tomatoes":1.9,
		"Root Vegetables":1,
		"Other Vegetables":1.8,
		"Bananas":2.1,
		"Apples":2.0,
		"Berries & Grapes":1,
		"Coffee":49.9,
		"Dark Chocolate":67.3,
		"Bovine Meat (beef herd)":320.7,
		"Poultry Meat":34.5,
		"Eggs":21.3
	}
	waterDict = {
		"Wheat & Rye(Bread)":12822,
		"Maize (meal)":350,
		"Potatoes":78,
		"Beet Sugar":115,
		"Tofu":32,
		"Rapeseed Oil":14,
		"Olive Oil":24396,
		"Tomatoes":4481,
		"Root Vegetables":38,
		"Other Vegetables":2940,
		"Bananas":31,
		"Apples":1025,
		"Berries & Grapes":16245,
		"Coffee":341,
		"Dark Chocolate":220,
		"Bovine Meat (beef herd)":441,
		"Poultry Meat":334,
		"Eggs":18621
	}
	printFootprint(computeFootprint([{
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
			],landDict,ghgEmDict,acidEmDict,eutEmDict,waterDict))
	'''
		UNIT TEST CASE
	'''
	#allPossibleMeal()
	test1Value = computeFootprint([{
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
			],landDict,ghgEmDict,acidEmDict,eutEmDict,waterDict)
	print("Test 1 : funtion `computeFootprint()` : "+ ("passed" if (compareFloat(test1Value[0],0.82) and compareFloat(test1Value[1],0.576) and compareFloat(test1Value[2],6.396) and compareFloat(test1Value[3],3.14) and compareFloat(test1Value[4],1450.6)) else "error"))
