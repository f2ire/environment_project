import pandas


class NutritionDataBase:

    nutriNames = [
        "gFatPerRetailUnit",
        "kcalPerRetailUnit",
        "gProteinPerRetailUnit",
        "gCarbPerRetailUnit",
    ]

    def __init__(self, path: str) -> None:
        self.path: str = path
        self.dfNutritions = None
        self.dictNutritions: dict = None
        self.foodByTypeOfRetailUnit: dict = {}
        self.foodByTypeOfProduct: dict = {}

    def __repr__(self) -> str:
        return str(self.foodByTypeOfProduct)

    def loadNutriData(self):
        self.dfNutritions = pandas.read_excel(self.path, 0, 0, index_col=0)
        self.dictNutritions = self.dfNutritions.to_dict("series")

    def computeDictByTypeOfRetailUnit(self):
        for name in self.nutriNames:
            self.foodByTypeOfRetailUnit[name] = self.dictNutritions[name]

    def computeDictbyTypeOfProduct(self):
        for productType in self.dictNutritions["Type"].items():
            if productType[1] in self.foodByTypeOfProduct:
                self.foodByTypeOfProduct[productType[1]].append(productType[0])
            else:
                self.foodByTypeOfProduct[productType[1]] = [productType[0]]


if __name__ == "__main__":

    a = NutritionDataBase("v_objet/data/TableS1_augmented_with_FAO_data.xlsx")
    a.loadNutriData()
    a.computeDictbyTypeOfProduct()
    print(a)
