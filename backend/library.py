# from processData import *
# from dataAnalysis import *
# from reportGeneration import *
# from figureGeneration import *

import warnings
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from fpdf import FPDF
import os
import sys
from statistics import mean, stdev
from math import sqrt

# ensures matplotlib does not generate a GUI, necessary for integration with flask
plt.matplotlib.use('Agg')
warnings.filterwarnings('ignore')

def resource_path(path):
    try:
        base_path = sys.executable.removesuffix("SewAnalyst")
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, path)

"""-------------------------------------------------------------------------------------------------------------------
    data processing functions
    -------------------------------------------------------------------------------------------------------------------"""

def processData(pathToData):
    headers = ["DATE", "POPULATION", "G", "I_DWF", "E", "DWF_REPORTED", "FFT", "PE_REPORTED", "PE_FORECAST"]

    data = pd.DataFrame = pd.read_csv(resource_path(pathToData), names=headers)
    data = data.drop(data.index[0])
    data = data.reset_index()
    ## convert date to correct format
    data['DATE'] = data['DATE'].apply(pd.to_datetime)
    data["G"] = data["G"].str.replace(",", "").str.strip().astype(float)
    data["I_DWF"] = data["I_DWF"].str.replace(",", "").str.strip().astype(float)
    data["E"] = data["E"].str.replace(",", "").str.strip().astype(float)
    data["DWF_REPORTED"] = data["DWF_REPORTED"].str.replace(",", "").str.strip().astype(float)
    data["FFT"] = data["FFT"].str.replace(",", "").str.strip().astype(float)
    data["POPULATION"] = data["POPULATION"].astype(float)


    data["PE_REPORTED"] = data["PE_REPORTED"].str.replace(",", "").str.strip().astype(float)
    data["PE_FORECAST"] = data["PE_FORECAST"].str.replace(",", "").str.strip().astype(float)
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


"""-------------------------------------------------------------------------------------------------------------------
    data analysis functions
    -------------------------------------------------------------------------------------------------------------------"""


# function for determining if differences between data are significant and how severe they are
def calculateDifference(forecastData, reportedData):
    # if there's a significant difference between datasets and how severe is that difference
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
        # if there is a significant difference, calculate cohens d
        cohensD = (mean(forecastData) - mean(reportedData)) / (sqrt((stdev(forecastData) ** 2 + stdev(reportedData) ** 2) / 2))
        print(cohensD)
        # use value of cohens d determine the severity of the difference
        if cohensD < 0.8:
            differenceSeverity = "mild"
        else:
            differenceSeverity = "severe"
    return significantDifference, differenceSeverity

# function for calculated DWF
def calculateDWF(data):
    DWFRecalc = []
    # calculate DWF using provided values for each row of the data and store in a list
    for idx in data.index:
        DWF = (data['POPULATION'][idx])*(data['G'][idx]) + (data['I_DWF'][idx]) + (data['E'][idx])
        DWFRecalc.append(DWF)
    # convert list into a panda Series
    return pd.Series(DWFRecalc)

def fftThreshold(DWFForecast, FFTActual):
    ReportedFFT = mean(FFTActual)
    ForecastedFFT = mean(DWFForecast) * 3
    if ForecastedFFT <= ReportedFFT:
        inadequateFFT = False
    else:
        inadequateFFT = True
    return inadequateFFT

# function for determining an answer to question 3
def questionThree(stats):
    # if differences between both PE and DWF data is significant, provide the answer True
    if stats['sigDifPE'] and stats['sigDifDWF'] and stats['FFTDiscrepancy']:
        significantDifferenceSum = True
        # if both differences are severe, the answer is also severe
        if stats['difSevDWF'] == "severe" and stats['difSevPE'] == "severe":
            differenceSeveritySum = "severe"
        # if at least one difference is mild, return the answer mild
        else:
            differenceSeveritySum = "mild"
    # if both comparisons do not determine a significant difference, provide the answer False
    else:
        significantDifferenceSum = False
        differenceSeveritySum = "none"
    return significantDifferenceSum, differenceSeveritySum



"""-------------------------------------------------------------------------------------------------------------------
    figure generation functions
    -------------------------------------------------------------------------------------------------------------------"""


# function called in integratedSoftware, used to generate both figures
def generateFigures(dates, PEActual, PEForecast, DWFActual, DWFForecast):
    genFigPE(dates, PEActual, PEForecast)
    genFigDWF(dates, DWFActual, DWFForecast)

# function used to generate line graph comparing SOLAR PE forecast with reported
# PE figures
def genFigPE(dates, PEActual, PEForecast):
    ## plot onto one graph
    plt.plot(PEForecast, color='red', label='Predicted')
    plt.plot(PEActual, color='black', label='Recorded')

    ##graph aesthetics
    plt.title("Recorded Population Equivalence versus Predicted Over Time", loc = 'left')
    plt.xlabel("Date Recorded")
    plt.ylabel("Population Equivalent (PE)")
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

    ##save as an image in the working directory
    plt.savefig(resource_path('resources/PE_plot.png'))

    ##close
    plt.close()

# determines the significance and severity of difference between the recalculated DWF
# and reported DWF figures
def genFigDWF(dates, DWFActual, DWFForecast):
    ## plot onto one graph
    plt.plot(DWFForecast, color='red', label='Predicted')
    plt.plot(DWFActual, color='black', label='Recorded')
    ##graph aesthetics
    plt.title("Recorded Dry Weather Flow versus Predicted Over Time", loc = 'left')
    plt.xlabel("Date Recorded")
    plt.ylabel("Dry Weather Flow (DWF)")
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

    ##save as an image in the working directory
    plt.savefig(resource_path('resources/DWF_plot.png'))

    ##close
    plt.close()



"""-------------------------------------------------------------------------------------------------------------------
    report generating functions
    -------------------------------------------------------------------------------------------------------------------"""


def generateReport(stats, PeGraph, DwfGraph, FILENAME):
    PeSeverity = stats['difSevPE']
    DwfSeverity = stats['difSevDWF']
    FftSeverity = stats['FFTDiscrepancy']
    OverallSeverity = stats['q3Severity']

    #Idea to do this:
    ## Data generation (will probs come from adam)
    ## Create the struct for the pdf (Snippets of graphs and text?? etc)
    ## Create the pdf report using fpdf


    #Deciding values and paragraph
    def PEParagraph(PeSeverity):
        if PeSeverity == "none":
            paragraph = 'The severity of the difference between the reported population equivalence and the forecasted one was determined as "none". This means that it was correctly reported and is not a point for concern. '
        elif PeSeverity == "mild":
            paragraph = 'The severity of the difference between the reported population equivalence and the forecasted one was determined as "mild". This means there was a slight difference between the reported PE and the actual forecasted one. This may be due company trying to avoid the extra funding they would need to inject in STWs maintenance and upgrade in order to be sufficient and safe for the environment. The other possibility is that they have not properly considered things like tourist population which impacts PE. '
        elif PeSeverity == "severe":
            paragraph = 'The severity of the difference between the reported population equivalence and the forecasted one was determined as "severe". This means there was a high difference between the reported PE and the actual forecasted one. This could insinuate the company is trying to minimise the maintenance cost for the STWs and as well may be hiding insufficient appropriate infrastructures for their respective true populations. This is a red flag, and it would be suggested to look further into the company as to whether they are being honest and they are just struggling to update their figures quick enough and accordingly or if they are lacking honesty and are trying to cut cost in an unethical manner. '
        else: 
            paragraph = 'There was an error with the PE data analysis please retry it and make sure your pe data is proper'
        return paragraph

    def DWFParagraph(DwfSeverity):
        if DwfSeverity == "none":
            paragraph = 'DWF value reported and the one calculated were deemed to be the same and thus of severity "none". Meaning the company is calculating DWF accurately and with the proper figures.'
        elif DwfSeverity == "mild":
            paragraph = 'DWF value reported and the one calculated were not the same and the severity of this difference was determined as "mild". Due to a change in 2012, there is a lot more leeway about the calculations of this therefore could explain the mild difference reported. As well numbers may have been rounded up and therefore vary the final value slightly or it was that a company was slightly over a threshold and wish to stay under, so they do not have to increase expenses on their STWs.'
        elif DwfSeverity == "severe":
            paragraph = 'DWF value reported and the one calculated were not the same and the severity of this difference was determined as "severe". This raises an important warning as often this means the company is changing values in order to avoid certain requirements that comes with higher DWF which would mean an increase in cost for STW maintenance. There is a possibility the wrong data or something was forgotten during the calculations, but this is highly unlikely.'
        else: 
            paragraph = 'There was an error with the DWF data analysis please retry it and make sure your pe data is proper'
        return paragraph

    def FFTParagraph(FftSeverity):
        if FftSeverity == False:
            paragraph = 'FFT value reported and the one calculated were deemed to be the same and thus of severity "none". Meaning the company is calculating FFT accurately and with the proper figures.'
        elif FftSeverity == True:
            paragraph = 'FFT value reported and the one calculated were not the same and the severity of this difference was determined as "severe". Numbers and values used in its calculations may have been rounded up and therefore vary the final value slightly. As well there are two different ways to calculate this and therefore the other equation may have been used in which values vary and it is dependent on PE which if flagged earlier may be the issue. Alternatively, this raises an important warning about the company changing values in order to avoid certain requirements that comes with higher FFT which would mean an increase in cost for STW maintenance. There is a possibility the wrong data or something was forgotten during the calculations, but this is highly unlikely. As well, the common agreement is that FFT is around 3 times DWF however many companies disagree and say it is around 2 times only and this is where a lot of the differences come from.'
        else: 
            paragraph = 'There was an error with the FFT data analysis please retry it and make sure your pe data is proper'
        return paragraph

    def CompAnParagraph(OverallSeverity):
        if OverallSeverity == "none":
            paragraph = 'The overall difference severity was "none". This means the company has not been flagged for any of the data it has reported and therefore it may be trusted.'
        elif OverallSeverity == "mild":
            paragraph = 'The overall difference severity was "mild". Some data values were flagged, or they were all averagely flagged for being mild differences meaning that some areas of data the company sent in did not match up with what was calculated or forecasted. This may just be miscalculations and a mistake by the company or it is an issue and they are trying to stay below the threshold to cut cost however this can be mildly detrimental to the environment and river ecosystems.'
        elif OverallSeverity == "severe":
            paragraph = 'The overall difference severity was "severe". This means that the company has consistently misreported the data and values. This is highly unlikely to be a mistake and is more likely to raise a red flag on the company suggesting they are severely trying to cut cost and investment into their STWs however this results in highly negative impacts on the environment around it.'
        else: 
            paragraph = 'There was an error with the overall company data analysis please retry it and make sure your pe data is proper'
        return paragraph

    PEPara = PEParagraph(PeSeverity)
    DWFPara = DWFParagraph(DwfSeverity)
    FFTPara = FFTParagraph(FftSeverity)
    CompAna = CompAnParagraph(OverallSeverity)
    title = 'STW Analysis Report'
    intro = 'The analysis of the data input has been conducted. The analysis will provide answers on: 1. Asses the accuracy and correctness of the company given PE for individual STWs 2. Verify that the company accurately calculated and reported their proper DWF for the according STWs 3. Verify that the company accurately calculated and reported the proper FFT for the according STWs 4. Qualitatively assure companies are ensuring provision of adequate sewage treatment capacity at water companies STWs  '
    conc = f'Overall to summarise the analysis of the data found: \n\
                PE: {PeSeverity} \n\
                DWF: {DwfSeverity} \n\
                FFT:{FftSeverity} \n\
                Company Analysis: {OverallSeverity}' 

    #Creating the pdf
    class PDF(FPDF):
        def __init__(self):
            super().__init__()
            self.WIDTH = 210
            self.HEIGHT = 297
            
        def header(self):
            #Title
            self.set_font('Arial', 'B', 15)
            w = self.get_string_width(title) + 6
            self.set_x((210 - w) / 2)
            self.cell(w, 9, title, 0, 1, 'C', 0)
            self.ln(10)
            
        def footer(self):
            # Page numbers in the footer
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            self.set_text_color(128)
            self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')


        def titleAndText(self, num, title, txt):
            #Text Format
            self.set_font('Arial', '', 12)
            self.set_fill_color(200, 220, 255)
            self.cell(0, 6, 'Section %d : %s' %(num, title), 0, 1, 'L', 1)
            self.ln(4)

            #Body Format
            self.set_font('Times', '', 12)
            self.multi_cell(0, 5, txt)
            self.ln()
        
        def ImageSet(self, img):
            #Set up the image so it fits on the page
            iMage = Image.open(img)
            width, height = iMage.size

            width, height = float(width * 0.264583), float(height * 0.264583)
            pdfSize = {'P': {'w': 210, 'h': 297}, 'L': {'w': 297, 'h': 210}}
            if width < height:
                orientation = 'P' 
            else:
                orientation = 'L'

            
            if width < pdfSize[orientation]['w']:
                width = width 
            else:
                width = pdfSize[orientation]['w']
            if height < pdfSize[orientation]['h']:
                height = height
            else:
                height = pdfSize[orientation]['h']
            
            self.image(img, w=width,h=height)
            self.ln()

        def print_section(self, num, title, txt, img):
            self.titleAndText(num, title, txt)
            if img != '0':
                self.ImageSet(img)

        
    pdf = PDF()

    pdf.add_page()
    pdf.print_section(0, 'Introduction', intro, '0')
    pdf.print_section(1, 'Population Equivalence', PEPara, PeGraph)
    pdf.print_section(2, 'Dry Weather Flow ', DWFPara, DwfGraph)
    pdf.print_section(3, 'Flow to Full Treatment', FFTPara, '0')
    pdf.print_section(4, 'Company Analysis', CompAna, '0')
    pdf.print_section(5, 'Conclusion', conc, '0')

    name = "reports/"+FILENAME+'.pdf'

    pdf.output(resource_path(name), 'F')



"""-------------------------------------------------------------------------------------------------------------------
    main function
    -------------------------------------------------------------------------------------------------------------------"""

# function which is called by flask backend to analyse the data and produce a report
# file_name is path to csv file provided by user during runtime
def main(file_name):

    FILENAME = file_name[0:-4]
    print(FILENAME)
    # reads the csv file in a panda dataframe, checks all required attributes are present
    # and cleans/formats the data
    data = processData(resource_path("resources/"+file_name))

    # assign required data fields to variables to be used for analysis
    dates = data['DATE']
    PEActual = data["PE_REPORTED"]
    PEForecast = data["PE_FORECAST"]
    DWFActual = data["DWF_REPORTED"]

    # calculate DWF using provided data and assign to the dataframe
    data['DWF_RECALCULATED'] = calculateDWF(data)
    DWFForecast = data['DWF_RECALCULATED']
    FFTActual = data['FFT']

    stats = {}

    # determines the significance and severity of difference between the SOLAR PE forecast
    # and reported PE figures
    stats['sigDifPE'], stats['difSevPE'] = calculateDifference(PEForecast, PEActual)

    # determines the significance and severity of difference between the recalculated DWF
    # figures and the reported DWF figures
    stats['sigDifDWF'], stats['difSevDWF'] = calculateDifference(DWFForecast, DWFActual)

    stats['FFTDiscrepancy'] = fftThreshold(DWFForecast, FFTActual)
    # Uses the statistics generated from the calculateDifference functions to determine an 
    # answer for question 3
    stats['q3Discrepancy'], stats['q3Severity'] = questionThree(stats)

    # used by the developer to check if all functions have produced an appropriate output
    for statistic in stats.keys():
        print(stats[statistic])
    try:
        # use the provided data to plot PE and DWF graphs
        generateFigures(dates, PEActual, PEForecast, DWFActual, DWFForecast)
        print("FIGURES GENERATED")
        # use the generated statistics and graphs to create a pdf report
        generateReport(stats, resource_path("resources/PE_plot.png"), resource_path(
            "resources/DWF_plot.png"), FILENAME)
    except Exception as e:
        # output any error if one occurs in the figure generation or report creation phase
        print (e)

if __name__ == "__main__":
    main("bad_example.csv")