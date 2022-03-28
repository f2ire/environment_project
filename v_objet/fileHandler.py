import json


class FileHandler:
    @staticmethod
    def saveMealList(filename: str, mealList: list):
        with open(filename, "w") as file:
            for meal in mealList:
                for i in range(len(meal[0][0])):
                    file.write(
                        f"{meal[0][1][i]:.2F} g or cL of {meal[0][0][i]}, "
                    )
                file.write("\n")

    @staticmethod
    def saveData(filename: str, statUserData: list | dict):
        with open(filename, "w") as file:
            json.dump(statUserData, file)

    @staticmethod
    def loadData(filename: str) -> list:
        with open(filename, "r") as file:
            return json.load(file)


if __name__ == "__main__":
    a = [1, 2, 3, 5, "fdzsfs"]
    FileHandler.saveList("Yoo.json", a)
    sqdq = FileHandler.loadList("Yoo.json")
    print(sqdq)
