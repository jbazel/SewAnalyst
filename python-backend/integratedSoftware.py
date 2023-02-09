from processData import *
from dataAnalysis import *
from reportGeneration import *

data = processData('python-backend/dummyData.csv')

sigDifPE, difSevPE = calculateDifference(data["PE (forecasted 2021)"], data["PE (unrounded 2020)"])

DWFCalc = calculateDWF(data)
sigDifDWF, difSevDWF = calculateDifference(DWFCalc, data["I_DWF (l/s)"])

q3Discrepancy, q3Severity = questionThree(sigDifPE, sigDifDWF, difSevPE, difSevDWF)

print(sigDifPE, sigDifDWF, difSevPE, difSevDWF, q3Discrepancy, q3Severity)

generateReport(difSevPE, difSevDWF, difSevDWF, q3Severity)