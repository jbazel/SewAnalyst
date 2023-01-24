import pandas as pd
import numpy as np

def processData(rawData):
    """
    perform all analysis on raw data
    create dataFrames
    analyse
    """

    headers: list = ["Site Code","Site Name","IDWF l/s","Maximum Infiltration Rate (Imax, l/s)","Note","Site Name 2","Previous max infiltration rate where known","Maximum Infiltration Rate (Imax, l/s) 2","Annual Return Population Equivalent (2020) (Unrounded)","Previous Trade Effluent where known,Trade Effluent (l/day) (2020)","Water Resource Zone","TW Est. of per capita domestic flow in this area (l/hd/day)"]

    rawData: pd.DataFrame = pd.read_csv('python-backend/sampleData.csv', names=headers) #names=headers
    rawData = rawData.drop(rawData['Site Name 2'])
    rawData = rawData.drop(rawData['Maximum Infiltration Rate (Imax, l/s) 2'])
    rawData.replace(' ', np.NaN)
    rawData.replace('  no data ', np.NaN)
    rawData.replace('', np.NaN)
    rawData.replace(' -   ', np.NaN)
    #rawDataClean = rawData.drop(rawData.loc[rawData['stalk-root'] == '?'].index)

    data = pd.read_csv("python-backend/sampleData.csv", index_col=0, parse_dates=True)
    data = pd.DataFrame(data)
    data = data.dropna(axis=1)  # drop all columns with NaN
    print(data.to_string())

processData("python-backend/sampleData.csv")