def processData(rawData):
    """
    perform all analysis on raw data
    create dataFrames
    analyse
    """

    data = pd.read_csv(rawData, index_col=0, parse_dates=True)
    data = pandas.DataFrame(data)
    data = data.dropna(axis=1)  # drop all columns with NaN
    print(data.to_string())