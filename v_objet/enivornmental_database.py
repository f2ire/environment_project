import pandas


class EnvironmentalDatabase:

    envName = [
        "landUse",
        "ghgEmissions",
        "acidifyingEmissions",
        "eutrophyingEmissions",
        "stressWeightedWaterUse ",
    ]

    envUnit = ["m2/FU", "kg CO2eq/FU", "g SO2eq/FU", "g PO43-eq/FU", "L/FU"]
    colomnsSelected = "A,E,K,W,AC,AO"
    rowSelected = [0, 1, 2, 46, 47, 48, 49]

    def __init__(self, path: str):
        self.path: str = path
        self.envDict = self.loadEnvData()

    def loadEnvData(self) -> dict:
        df_environment = pandas.read_excel(
            self.path,
            0,
            header=None,
            names=["products"] + self.envName,
            index_col=0,
            usecols=self.colomnsSelected,
            skiprows=lambda x: x in self.rowSelected,
        )
        return df_environment.to_dict("series")
