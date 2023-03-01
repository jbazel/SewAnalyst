from processData import *
from dataAnalysis import *
from reportGeneration import *
from figureGeneration import *


def main(file_name):
    data = processData(file_name)
    dates = data['DATE']
    PEActual = data["PE (unrounded 2020)"]
    PEForecast = data["PE (forecasted 2021)"]
    DWFActual = data["I_DWF (l/s)"]
    data['DWF_RECALCULATED'] = calculateDWF(data)
    DWFForecast = data['DWF_RECALCULATED']
    
    sigDifPE, difSevPE = calculateDifference(PEForecast, PEActual)
    sigDifDWF, difSevDWF = calculateDifference(DWFForecast, DWFActual)
    q3Discrepancy, q3Severity = questionThree(sigDifPE, sigDifDWF, difSevPE, difSevDWF)

    print(sigDifPE, sigDifDWF, difSevPE, difSevDWF, q3Discrepancy, q3Severity)

    generateFigures(dates, PEActual, PEForecast, DWFActual, DWFForecast)

    generateReport(difSevPE, difSevDWF, difSevDWF, q3Severity, "PE_plot.png", "DWF_plot.png")


if __name__ == "__main__":
    main("python-backend/dummyData.csv")