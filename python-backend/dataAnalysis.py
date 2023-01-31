import pandas as pd
from scipy import stats
from sklearn.metrics import mean_squared_error

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
        threshold = RMSE / (data["PE (unrounded 2020)"].std() if data["PE (unrounded 2020)"].std() != 0 else 1)
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

def calculateDWF(data):
    DWFRecalc = []
    for row in data.iterrows:
        DWF = data['P']*data['G'] + data['I_DWF (l/s)'] + data['E']
        DWFRecalc.append(DWF)
    return DWFRecalc


'''
QUESTION 3 - Summary
'''

#PEsignificantDifference, PEdifferenceSeverity = calculateDifference(data["PE (forecasted 2021)"], data["PE (unrounded 2020)"])
#calculateDifference(DWFRecalc, data["I_DWF (l/s)"])

def questionThree(significantDifferencePE, significantDifferenceDWF, differenceSeverityPE, differenceSeverityDWF):
    if significantDifferencePE and significantDifferenceDWF:
        significantDifferenceSum = True
        if differenceSeverityDWF == "severe" and differenceSeverityPE == "severe":
            differenceSeveritySum = "severe"
        else:
            differenceSeveritySum = "mild"
    else:
        significantDifferenceSum = False
    return significantDifferenceSum, differenceSeveritySum