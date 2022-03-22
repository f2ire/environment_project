from meal import Meal
import itertools


class MealSet:
    def __init__(self, dataNutriment) -> None:
        self.dataNutriment = dataNutriment
        self.mealList = []

    def computeMealList(self) -> list:
        for meal in list(
            itertools.product(
                self.dataNutriment["ProteinSource"],
                self.dataNutriment["CarbSource"],
                self.dataNutriment["FatSource"],
                self.dataNutriment["Vegetable"],
                self.dataNutriment["Fruit"],
                self.dataNutriment["Extra"],
            )
        ):
            Meal(meal[0], meal[1], meal[2], meal[3], meal[4], meal[0])
