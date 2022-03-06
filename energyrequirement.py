def basalMetabolicRate(gender: str, weight: float, height: float, age: int) -> float:
    """ # Voir son docstring  sur moodle ou jcp pas ou avec tout ce qu'elle demande
    Return the metabolic rate of a person according to Mifflin St Jeor's equation

        Parameters : 
                gender (str) : Your gender with "M" or "F" (male or female work)
                weight (float) : Your weight in Kg
                height (float) : Your height in Metter
                age (int) : Your age in year
        Return :
                met_rate (int) : The metabolic rate calculted with the informations given
    """
    if gender.lower() in ["M", "male"]:
        met_rate = 10*weight+6.25*height-5*age+5
    else:
        met_rate = 10*weight+6.25*height-5*age-161
    return met_rate


def dailyEnergyRequirement(gender: str, weight: float, height: float, age: int, physical_activity_lvl: str):
    """
    Return the daily energy requirement of a person according to Mifflin St Jeor's equation and his physical activity level

        Parameters : 
                gender (str) : Your gender with "M" or "F" (male or female work)
                weight (float) : Your weight in Kg
                height (float) : Your height in Metter
                age (int) : Your age in year
                physical_activity_lvl (str) : One string among sedementary, light, moderate, intense and very intense to describe your physical activity
        Return :
                Value (int) : The daily energy requirement calculted with the informations given
    """
    activity_lvl = {"sedementary": 1.4, "light": 1.6,
                    "moderate": 1.75, "intense": 1.9, "very intense": 2.1}
    return activity_lvl[physical_activity_lvl]*basalMetabolicRate(gender, weight, height, age)


def unit_test(a: float, b: float, delta=10**-6) -> bool:
    """
    Try if a and b are equal with a gap smaller than delta
    """
    return abs(a-b) < abs(delta)

print(unit_test(dailyEnergyRequirement("male", 59, 175, 20, "light"), 2552))
