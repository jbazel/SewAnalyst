import pandas as pd
import numpy as np

def processData(pathToData):
    headers = ["DATE", "MAX_IR (l/s)", "I_DWF (l/s)", "I_DWF_MAX (l/s)", "G (2020)", "E", "TDV (l)", "PE (forecasted 2021)", "PE (unrounded 2020)"]
    data = pd.DataFrame = pd.read_csv(pathToData, names=headers)
    data = data.drop(data.index[0])
    data = data.reset_index()
    data["I_DWF (l/s)"] = data["I_DWF (l/s)"].str.replace(",", "").str.strip().astype(float)
    data["G (2020)"] = data["G (2020)"].str.replace(",", "").str.strip().astype(float)
    data["PE (forecasted 2021)"] = data["PE (forecasted 2021)"].str.replace(",", "").str.strip().astype(float)
    data["PE (unrounded 2020)"] = data["PE (unrounded 2020)"].str.replace(",", "").str.strip().astype(float)
    print(data)
    for i in headers:
        if i not in data.columns:
            print("ERROR missing column: " + i)

    dropped_indexes = []
    for i in data.index:
        for j in data.iloc[i]:
            if j == "" or j == " ":
                dropped_indexes.append(i)
                break
            elif j is str:
                try:
                    j = float(j)
                except:
                    print("ERROR: missing data for row: " + str(i))
                    print("dropping..."+ str(j))
                    dropped_indexes.append(i)
                    break 
                
    for i in dropped_indexes:
        data.drop(i, inplace=True)
        data = data.reset_index()
        print(data)

    return data
                        

if __name__ == "__main__":
    data = processData('python-backend/dummyData.csv')