from tkinter import W
import tools
# ______________________________________________________________________________
# Fonction :


def basalMetabolicRate(gender: str, weight: float,
                       height: float, age: int) -> float:
    """ # Voir son docstring  sur moodle ou jcp pas ou avec tout ce qu'elle demande
    Return the metabolic rate of a person according to Mifflin St Jeor's\
        equation

        Parameters :
                gender (str) : Your gender with "M" or "F"\
                    (male or female work)
                weight (float) : Your weight in Kg
                height (float) : Your height in Cm
                age (int) : Your age in year (you have to have more than 18 yo)
        Return :
                met_rate (int) : The metabolic rate calculted with\
                    the informations given
    """
    if age < 18:
        raise ValueError(
            'This program is currently designed for adult food requirements, sorry.')
    if weight < 0:
        raise ValueError('Body weight should be a positive number.')
    if height < 0:
        raise ValueError('Height should be a positive integer.')
    if gender.lower() in ["M", "male"]:
        met_rate = 10*weight+6.25*height-5*age+5
    else:
        met_rate = 10*weight+6.25*height-5*age-161
    return met_rate


def dailyEnergyRequirement(gender: str, weight: float,
                           height: float, age: int,
                           physical_activity_lvl: str):
    """
    Return the daily energy requirement of a person according to Mifflin St \
        Jeor's equation and his physical activity level

        Parameters :
                gender (str) : Your gender with "M" or "F"\
                    (male or female work)
                weight (float) : Your weight in Kg
                height (float) : Your height in Metter
                age (int) : Your age in year
                physical_activity_lvl (str) : One string among sedementary,\
                light, moderate, intense and very intense to describe \
                your physical activity
        Return :
                Value (int) : The daily energy requirement calculted with the\
                    informations given
    """
    activity_lvl = {"sedementary": 1.4, "light": 1.6,
                    "moderate": 1.75, "intense": 1.9, "very intense": 2.1}
    return activity_lvl[physical_activity_lvl] * basalMetabolicRate(
        gender, weight, height, age)


def askStatUser() -> list:
    userStats = []
    activityLvl = ["sedementary", "light",
                   "moderate", "intense", "very intense"]
    textToPrint = [
        "Select your gender (M/F) : \n",
        "Precise your age in years : \n",
        "Precise your body weigh in Kg : \n",
        "Precise your heigh in cm : \n",
        "Precise your activity level:\n"
        f"Press 1 for {activityLvl[0]}\n"
        f"Press 2 for {activityLvl[1]}\n"
        f"Press 3 for {activityLvl[2]}\n"
        f"Press 4 for {activityLvl[3]}\n"
        f"Press 5 for {activityLvl[4]}\nPress : "
    ]
    it = 0
    while it < len(textToPrint):

        if it == 0:
            genderAnswerError = "Please precise your gender by pressing 'M'"
            "for Male or 'F' for female."
            gender = tools.strInput(textToPrint[it], genderAnswerError)
            if gender not in ["m", "M", "f", "F"]:
                print(genderAnswerError)
            else:
                userStats.append(gender)
                it += 1

        elif it < 4:
            valAnswerError = "Please press the good unit."
            val = tools.intInput(textToPrint[it], valAnswerError)
            if val <= 0:
                print(valAnswerError)
            else:
                userStats.append(val)
                it += 1
        else:
            activityAnswerError = "Please press a int between 1 and 5"
            index_activityLvl = tools.intInput(
                textToPrint[it], activityAnswerError)
            if index_activityLvl < 0 or index_activityLvl > 5:
                print(activityAnswerError)
            else:
                userStats.append(activityLvl[index_activityLvl])
                it += 1

    return userStats

# ______________________________________________________________________________
# Variable :

# ______________________________________________________________________________
# Main Program :


if __name__ == "__main__":
    print(tools.floatUnitTest(dailyEnergyRequirement("male", 59, 175,
                                                     20, "light"), 2552))
