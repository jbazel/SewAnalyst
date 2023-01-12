import pandas as pd

def processData(rawData):
    """
    perform all analysis on raw data
    create dataFrames
    analyse
    """

    data = pd.read_csv("python-backend/sampleData.csv", index_col=0, parse_dates=True)
    data = pd.DataFrame(data)
    data = data.dropna(axis=1)  # drop all columns with NaN
    print(data.to_string())

processData("python-backend/sampleData.csv")