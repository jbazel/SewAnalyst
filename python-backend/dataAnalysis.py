import pandas as pd
from scipy import stats
from sklearn.metrics import mean_squared_error


# function for determining if differences between data are significant and how severe they are
def calculateDifference(forecastData, reportedData):
    # if there a significant difference between datasets and how severe is that difference
    significantDifference = False
    differenceSeverity = "none"
    # determine if data is normally distributed
    forecastNormal = stats.shapiro(forecastData).pvalue
    reportedNormal = stats.shapiro(reportedData).pvalue

    if (forecastNormal >= 0.05) and (reportedNormal >= 0.05):
        # if data is normally distributed, perform paired sample t-test
        sigDifTest = stats.ttest_rel(forecastData, reportedData).pvalue
    else:
        # if data is not normally distributed, perform wilcoxon sign-ranked test
        sigDifTest = stats.wilcoxon(forecastData, reportedData).pvalue

    if sigDifTest < 0.05:
        significantDifference = True
        # if there is a significant difference, calculate root mean squared error
        RMSE = mean_squared_error(reportedData, forecastData, squared=False)
        # use RMSE divided by standard deviation of reported data to determine the severity
        # of the difference
        threshold = RMSE / (reportedData.std() if reportedData.std() != 0 else 1)
        if threshold < 1:
            differenceSeverity = "mild"
        else:
            differenceSeverity = "severe"
    return significantDifference, differenceSeverity

# function for calculated DWF
def calculateDWF(data):
    DWFRecalc = []
    # calculate DWF using provided values for each row of the data and store in a list
    for idx in data.index:
        DWF = (data['PE (unrounded 2020)'][idx])*(data['G (2020)'][idx]) + (data['I_DWF (l/s)'][idx]) + (data['E'][idx])
        DWFRecalc.append(DWF)
    # convert list into a panda Series
    return pd.Series(DWFRecalc)

# function for determining an answer to question 3
def questionThree(significantDifferencePE, significantDifferenceDWF, differenceSeverityPE, differenceSeverityDWF):
    # if differences between both PE and DWF data is significant, provide the answer True
    if significantDifferencePE and significantDifferenceDWF:
        significantDifferenceSum = True
        # if both differences are severe, the answer is also severe
        if differenceSeverityDWF == "severe" and differenceSeverityPE == "severe":
            differenceSeveritySum = "severe"
        # if at least one difference is mild, return the answer mild
        else:
            differenceSeveritySum = "mild"
    # if both comparisons do not determine a significant difference, provide the answer False
    else:
        significantDifferenceSum = False
        differenceSeveritySum = "none"
    return significantDifferenceSum, differenceSeveritySum