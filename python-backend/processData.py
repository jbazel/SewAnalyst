import pandas as pd
import numpy as np

def processData():
    headers = ["DATE", "MAX_IR (l/s)", "I_DWF (l/s)", "I_DWF_MAX (l/s)", "G (2020)", "TDV (l)", "PE (forecasted 2021)", "PE (unrounded 2020)"]
    data = pd.DataFrame = pd.read_csv('python-backend/dummyData.csv', names=headers)
    data = data.drop("DATE", axis=1)
    data = data.drop(index = 0)
    data = data.reset_index()

    data["PE (forecasted 2021)"] = data["PE (forecasted 2021)"].str.replace(",", "").str.strip().astype(float)
    data["PE (unrounded 2020)"] = data["PE (unrounded 2020)"].str.replace(",", "").str.strip().astype(float)
    print(data)
    for i in headers:
        if i not in data.columns:
            print("ERROR: missing column: " + i)

    dropped_indexes = []
    for i in data.index:
        for j in data.iloc[i]:
            if j is str:
                try:
                      j = float(j)
                except:
                    print("ERROR: missing data for row: " + str(i))
                    print("dropping..."+ str(j))
                    dropped_indexes.append(i)
                    break 
                        

processData()