import pickle
from tools.good_input import GoodInput
import os
from fileHandler import FileHandler


class User:

    activity_lvl = {
        "sedementary": 1.4,
        "light": 1.6,
        "moderate": 1.75,
        "intense": 1.9,
        "very intense": 2.1,
    }

    # Basic methods

    def __init__(
        self,
        gender: str = "m",
        weight: int = 75,
        height: int = 185,
        age: int = 21,
        activity_lvl: str = "moderate",
    ):
        self.userDict = {
            "gender": gender,
            "weight": weight,
            "height": height,
            "age": age,
            "activity_lvl": activity_lvl,
        }
        self.metabobicRate = None
        self.dailyEnergyRequirement = None
        self.dictExtraQuantity = {}
        self.threshold = []

    def __repr__(self) -> str:
        return f"User dict : {str(self.userDict)},\n\
            and metabolic rate is {str(self.metabobicRate)} \n\
            so daily energy requirement is {str(self.dailyEnergyRequirement)}"

    # Other methods
    def computeAllUserThing(self):
        self.computeMetabolicRate()
        self.computeDailyEnergyRequirement()

    def askStatUser(self):
        activityLvl = [
            "sedementary",
            "light",
            "moderate",
            "intense",
            "very intense",
        ]
        textToPrint = [
            "Select your gender (M/F) : \n",
            "Precise your body weigh in Kg : \n",
            "Precise your heigh in cm : \n",
            "Precise your age in years : \n",
            "Precise your activity level:\n"
            f"Press 1 for {activityLvl[0]}\n"
            f"Press 2 for {activityLvl[1]}\n"
            f"Press 3 for {activityLvl[2]}\n"
            f"Press 4 for {activityLvl[3]}\n"
            f"Press 5 for {activityLvl[4]}\nPress : ",
        ]
        for it, key in enumerate(self.userDict.keys()):
            if it == 0:
                test = True
                while test:
                    genderAnswerError = "Please precise your gender (M/F)"
                    gender = GoodInput.strInput(
                        textToPrint[it], genderAnswerError
                    )
                    if gender not in ["m", "M", "f", "F"]:
                        print(genderAnswerError)
                    else:
                        self.userDict[key] = gender
                        test = False
            elif it < 4:
                test = True
                while test:
                    valAnswerError = "Please press the good unit."
                    val = GoodInput.intInput(textToPrint[it], valAnswerError)
                    if val <= 0:
                        print(valAnswerError)
                    else:
                        self.userDict[key] = val
                        test = False
            else:
                test = True
                while test:
                    activityAnswerError = "Please press a int between 1 and 5"
                    index_activityLvl = GoodInput.intInput(
                        textToPrint[it], activityAnswerError
                    )
                    if index_activityLvl < 0 or index_activityLvl > 5:
                        print(activityAnswerError)
                    else:
                        self.userDict[key] = activityLvl[index_activityLvl]
                        test = False

    def computeMetabolicRate(self) -> float:
        if self.userDict["age"] < 18:
            raise ValueError(
                "This program is designed for adult food requirements."
            )
        if self.userDict["weight"] < 0:
            raise ValueError("Body weight should be a positive number.")
        if self.userDict["height"] < 0:
            raise ValueError("Height should be a positive integer.")
        if self.userDict["gender"] in ["m", "M"]:
            met_rate = (
                10 * self.userDict["weight"]
                + 6.25 * self.userDict["height"]
                - (5 * self.userDict["age"])
                + 5
            )
        else:
            met_rate = (
                10 * self.userDict["weight"]
                + 6.25 * self.userDict["height"]
                - (5 * self.userDict["age"])
                - 161
            )
        self.metabobicRate = met_rate

    def computeDailyEnergyRequirement(self) -> float:
        if self.metabobicRate is None:
            print("You have to use computeMetabolicRate() before this call")
        else:
            DER = (
                self.activity_lvl[self.userDict["activity_lvl"]]
                * self.metabobicRate
            )
            self.dailyEnergyRequirement = DER

    def extraQuantity(self, nutriDict: dict):
        extraSource = nutriDict["Extra"]
        it = 0
        while it < len(extraSource):
            extraQuestion = (
                f"How much extra kg of {extraSource[it]} do you need ? \n"
            )
            extraAnswerError = (
                "\nERROR :\n\nYou have to write a number superior of 0.\n"
            )
            i_Extra = GoodInput.floatInput(extraQuestion, extraAnswerError)
            if i_Extra >= 0:
                self.dictExtraQuantity[extraSource[it]] = i_Extra
                it += 1
            else:
                print(extraAnswerError)

    def thresholdsEnvimpact(self, mealset, envData) -> list:

        mealset.printHistEnv(envData)

        if os.path.exists("thresholdsList.json") and GoodInput.isInputYes(
            "Do you want to keep last thresholds"
        ):
            thresholdsList = FileHandler.loadData("thresholdsList.json")
        else:
            thresholdsList = [
                GoodInput.floatInput(
                    f"What is the limite of {name} : ", "Please write a float"
                )
                for name in envData.envName
            ]
            FileHandler.saveData("thresholdsList.json", thresholdsList)
        self.threshold = thresholdsList

    @staticmethod
    def chooseUser(filename, nutriDict, default=False):
        if os.path.exists(filename) and GoodInput.isInputYes(
            "Do you want to select previous user data ?"
        ):
            with open(filename, "rb") as file:
                loadUser = pickle.load(file)
            if not GoodInput.isInputYes("Do you want to keep extra setting ?"):
                loadUser.extraQuantity(nutriDict)
            return loadUser
        else:
            newUser = User()
            if not default:
                newUser.askStatUser()
            newUser.extraQuantity(nutriDict)
            with open(filename, "wb") as file:
                pickle.dump(newUser, file)
            return newUser


# Main program
if __name__ == "__main__":
    mayo = User()
    mayo.computeMetabolicRate()
    mayo.computeDailyEnergyRequirement()
    print(mayo)
