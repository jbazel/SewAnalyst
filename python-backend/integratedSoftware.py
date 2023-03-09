from processData import *
from dataAnalysis import *
from reportGeneration import *
from figureGeneration import *

# function which is called by flask backend to analyse the data and produce a report
# file_name is path to csv file provided by user during runtime
def main(file_name):
    # reads the csv file in a panda dataframe, checks all required attributes are present
    # and cleans/formats the data
    data = processData(file_name)
    # assign required data fields to variables to be used for analysis
    dates = data['DATE']
    PEActual = data["PE (unrounded 2020)"]
    PEForecast = data["PE (forecasted 2021)"]
    DWFActual = data["I_DWF (l/s)"]
    # calculate DWF using provided data and assign to the dataframe
    data['DWF_RECALCULATED'] = calculateDWF(data)
    DWFForecast = data['DWF_RECALCULATED']
    # determines the significance and severity of difference between the SOLAR PE forecast
    # and reported PE figures
    sigDifPE, difSevPE = calculateDifference(PEForecast, PEActual)
    # determines the significance and severity of difference between the recalculated DWF
    # figures and the reported DWF figures
    sigDifDWF, difSevDWF = calculateDifference(DWFForecast, DWFActual)
    # Uses the statistics generated from the calculateDifference functions to determine an 
    # answer for question 3
    q3Discrepancy, q3Severity = questionThree(sigDifPE, sigDifDWF, difSevPE, difSevDWF)
    # used by the developer to check if all functions have produced an appropriate output
    print(sigDifPE, sigDifDWF, difSevPE, difSevDWF, q3Discrepancy, q3Severity)
    try:
        # use the provided data to plot PE and DWF graphs
        generateFigures(dates, PEActual, PEForecast, DWFActual, DWFForecast)
        print("FIGURES GENERATED")
        # use the generated statistics and graphs to create a pdf report
        generateReport(difSevPE, difSevDWF, difSevDWF, q3Severity, "PE_plot.png", "DWF_plot.png")
    except Exception as e:
        # output any error if one occurs in the figure generation or report creation phase
        print (e)

# if __name__ == "__main__":
#     main("python-backend/dummyData.csv")