import pandas as pd

def processData(rawData):
    """
    perform all analysis on raw data
    create dataFrames
    analyse
    """

    headers: list = ["Site Code","Site Name","IDWF l/s","Maximum Infiltration Rate (Imax, l/s)","Note","Site Name","Previous max infiltration rate where known","Maximum Infiltration Rate (Imax, l/s)","Annual Return Population Equivalent (2020) (Unrounded)","Previous Trade Effluent where known,Trade Effluent (l/day) (2020)","Water Resource Zone","TW Est. of per capita domestic flow in this area (l/hd/day)"]

    rawData: pd.DataFrame = pd.read_csv('python-backend/sampleData.csv', names=headers)
    rawDataClean = rawData.drop(rawData.loc[rawData['stalk-root'] == '?'].index)

    data = pd.read_csv("python-backend/sampleData.csv", index_col=0, parse_dates=True)
    data = pd.DataFrame(data)
    data = data.dropna(axis=1)  # drop all columns with NaN
    print(data.to_string())

processData("python-backend/sampleData.csv")