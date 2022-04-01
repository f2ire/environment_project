import calendar
import random
import datetime
from fileHandler import FileHandler


class PdfMaker:
    def __init__(self, mealListFile) -> None:
        self.mealList = FileHandler.loadData(mealListFile)
        self.mealByDate = self.getRandomMealByDay(self.mealList)

    def getRandomMealByDay(self, mealList):
        mealByDateFutureList = []
        cal = calendar.Calendar()
        for day in cal.itermonthdays4(2022, 4):
            if day[1] == datetime.date.today().month:
                print(day)
                mealByDateFutureList.append(random.choice(mealList))
        return mealByDateFutureList


if __name__ == "__main__":
    new_pdf = PdfMaker("meal_list")
    # print(new_pdf.mealList)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(new_pdf.mealByDate)
