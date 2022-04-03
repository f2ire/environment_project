import calendar
import random
import datetime
from fileHandler import FileHandler
from reportlab.platypus import (
    PageTemplate,
    BaseDocTemplate,
    Frame,
    NextPageTemplate,
    PageBreak,
    Paragraph,
    Spacer,
)
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet


class PdfMaker:
    def __init__(self, mealListFile) -> None:
        self.mealList = FileHandler.loadData(mealListFile)
        self.mealByDate = self.getRandomMealByDay(self.mealList)
        self.pdfcontent = []

    def getRandomMealByDay(self, mealList):
        mealByDateFutureList = []
        cal = calendar.Calendar()
        todayDate = datetime.date.today().timetuple()[:3]
        for day in cal.itermonthdays4(2022, 4):
            if day[:3] > todayDate and todayDate[1] == day[1]:
                mealByDateFutureList.append(
                    [
                        day,
                        list(random.choice(mealList) for _ in [0, 1]),
                    ]
                )
        return mealByDateFutureList

    def beautyDate(self, index: int) -> tuple:
        weekDay = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]

        month = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]

        newYear = self.mealByDate[index][0][0]
        newMonth = month[self.mealByDate[index][0][1]]
        newDay = self.mealByDate[index][0][2]
        newTupleDate = weekDay[self.mealByDate[index][0][3]]
        dateText = f"{newTupleDate}, {newMonth} {newDay}, {newYear}"
        return dateText

    def makePdfContent(self):
        self.pdfcontent = []  # init if it is not
        styles = getSampleStyleSheet()
        styleN = styles["Normal"]
        styleH = styles["Heading1"]
        styleH2 = styles["Heading2"]

        self.pdfcontent = []
        self.pdfcontent.append(NextPageTemplate("firstPageTemplate"))
        self.pdfcontent.append(NextPageTemplate("otherPageTemplate"))
        self.pdfcontent.append(PageBreak())
        for iMeal in range(len(self.mealByDate)):
            self.pdfcontent.append(
                Paragraph(str(self.beautyDate(iMeal)), styleH)
            )
            for k in range(2):
                if k % 2 == 0:
                    self.pdfcontent.append(Paragraph("Lunch", styleH2))
                else:
                    self.pdfcontent.append(Paragraph("Dinner", styleH2))
                for j, elem in enumerate(self.mealByDate[iMeal][1][0][0]):
                    self.pdfcontent.append(
                        Paragraph(
                            f"{elem} : {int(self.mealByDate[iMeal][1][0][1][j]*1000)}g.",
                            styleN,
                        )
                    )
                self.pdfcontent.append(Spacer(17 * cm, 1 * cm))
            self.pdfcontent.append(Spacer(22 * cm, 1 * cm))
            if iMeal % 2 == 1:
                self.pdfcontent.append(PageBreak())

    def buildPdf(self):
        doc = BaseDocTemplate("sample.pdf", pagesize=A4)

        mySmallFrame = Frame(2 * cm, (2) * cm, 17 * cm, 15 * cm, id="myFrame")
        firstPageTemplate = PageTemplate(
            id="firstPageTemplate",
            frames=[mySmallFrame],
            onPage=self.firstPageLayout,
        )

        myBigFrame = Frame(
            2 * cm, 2 * cm, 17 * cm, 25.7 * cm, id="myFrame"
        )  # 2cm of margins on the four sides
        otherPageTemplate = PageTemplate(
            id="otherPageTemplate",
            frames=[myBigFrame],
            onPage=self.otherPageLayout,
        )

        doc.addPageTemplates([firstPageTemplate, otherPageTemplate])

        self.makePdfContent()

        doc.build(self.pdfcontent)

    @staticmethod
    def firstPageLayout(canvas, doc):
        canvas.saveState()
        canvas.setPageSize(A4)
        canvas.setFont("Helvetica-Bold", 16)
        canvas.drawCentredString(
            A4[0] / 2.0, A4[1] - 8 * cm, "Your menus for this month"
        )
        canvas.restoreState()

    @staticmethod
    def otherPageLayout(canvas, doc):
        canvas.saveState()
        canvas.setPageSize(A4)
        canvas.setFont("Times-Roman", 11)
        canvas.drawCentredString(A4[0] / 2.0, 1 * cm, "Page %d" % (doc.page))
        canvas.restoreState()


if __name__ == "__main__":
    new_pdf = PdfMaker("meal_list")
    # print(new_pdf.mealList)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(new_pdf.mealByDate)

    new_pdf.buildPdf()
