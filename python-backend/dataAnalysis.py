'''
PLAN:
1. import data and convert to panda df
2. research statistics to answer following questions
3. compute statistics

questions and how to answer:
1. Do water companies accurately and consistently assess PE for individual Sewage Treatment Works? 

An answer will be obtained by comparing Solar PE forecast with companies assessments. 
Deviations between forecasted and reported data will be calculated and determined to be significant or not. 

2. Do water companies accurately calculate DWF? 

An answer will be obtained by recalculating DWF and comparing the result with the reported figures. 
Deviations between these two figures will be determined to be significant or not. 

3. Does the Environment Agency routinely and robustly Qualitatively Assure these calculations and measures 
by the water companies thus ensuring the provision of adequate sewage treatment capacity at water company Sewage Treatment Works? 

An answer will be obtained based on the first two questions. It will be assessed whether these deviations 
from provisioned guidance are significant enough to warrant a conclusion that adequate and qualitatively 
assured checks are not being carried out.

How to calculate and determine significant deviations:
paired t-test

DWF = PG + Idwf + E
DWF = total dry weather flow (l/d)
P = Catchment population (number)
G = per capita domestic flow (l/hd/d)
Idwf = dry weather infiltration (l/d)
E = trade effluent flow (l/d)
'''
import pandas as pd
from scipy import stats
from sklearn.metrics import mean_squared_error
'''
FORMATTING DATA
'''
#importing and formatting dummy data
headers = ["DATE", "MAX_IR (l/s)", "I_DWF (l/s)", "I_DWF_MAX (l/s)", "G (2020)", "TDV (l)", "PE (forecasted 2021)", "PE (unrounded 2020)"]
data = pd.DataFrame = pd.read_csv('python-backend/dummyData.csv', names=headers)
data = data.drop("DATE", axis=1)
data = data.drop(index = 0)
data = data.reset_index()

data["PE (forecasted 2021)"] = data["PE (forecasted 2021)"].str.replace(",", "").str.strip().astype(float)
data["PE (unrounded 2020)"] = data["PE (unrounded 2020)"].str.replace(",", "").str.strip().astype(float)
print(data)
#print(data["PE (forecasted 2021)"].describe())
#print(data["PE (unrounded 2020)"].describe())

'''
QUESTION 1 - PE
'''
#function for determining id fifferences between data are significant and how severe they are
def calculateDifference(forecastData, reportedData):
    #is there a significant difference between datasets and how severe is that difference
    significantDifference = False
    differenceSeverity = "none"
    #determine if data is normally distributed
    forecastNormal = stats.shapiro(forecastData).pvalue
    reportedNormal = stats.shapiro(reportedData).pvalue

    if (forecastNormal >= 0.05) and (reportedNormal >= 0.05):
        #if data is normally distributed, perform paired sample t-test
        sigDifTest = stats.ttest_rel(forecastData, reportedData).pvalue
    else:
        #if data is not normally distributed, perform wilcoxon sign-ranked test
        sigDifTest = stats.wilcoxon(forecastData, reportedData).pvalue

    if sigDifTest < 0.05:
        #if there is a significant difference, calculate root mean squared error and determine severity of difference
        RMSE = mean_squared_error(reportedData, forecastData, squared=False)
        threshold = RMSE/1 #replace with following with actual data: data["PE (unrounded 2020)"].std()
        if threshold < 1:
            differenceSeverity = "mild"
        else:
            differenceSeverity = "severe"
    return significantDifference, differenceSeverity







'''
QUESTION 2 - DWF
DWF = PG + Idwf + E
DWF = total dry weather flow (l/d)
P = Catchment population (number)
G = per capita domestic flow (l/hd/d)
Idwf = dry weather infiltration (l/d)
E = trade effluent flow (l/d)
'''

'''
DWFRecalc = []
for row in data.iterrows:
    DWF = data['P']*data['G'] + data['I'] + data['E']
    DWFRecalc.append(DWF)
'''

'''
QUESTION 3 - Summary
'''

#PEsignificantDifference, PEdifferenceSeverity = calculateDifference(data["PE (forecasted 2021)"], data["PE (unrounded 2020)"])
#calculateDifference(DWFRecalc, data["I_DWF (l/s)"])
'''
if significantDifferencePE and significantDifferenceDWF:
    significantDifferenceSum = True
    if differenceSeverityDWF == "severe" and differenceSeverityPE == "severe":
        differenceSeveritySum = "severe"
    else:
        differenceSeveritySum = "mild"
else:
    significantDifferenceSum = False
'''