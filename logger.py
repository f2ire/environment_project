class Logger:

    def __init__(self, mealList=None):
        self.mealList = mealList

    def saveMealList(self, filename: str):
        with open(filename, "w") as file:
            for meal in self.mealList:
                for i in range(len(meal[0][0])):
                    file.write(
                        f"{meal[0][1][i]:.2F} g or cL of {meal[0][0][i]}, ")
                file.write("\n")
