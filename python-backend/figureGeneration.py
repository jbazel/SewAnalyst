import pandas as pd
import matplotlib.pyplot as plt

def cleanString(data):
    ## replaces the commas and spaces in each item in the dataframe
    data = data.replace(',', '')
    data = data.replace(' ', '')
    ## converts each value into an integer
    data = int(data)
    return data

def generateFigures(dates, PEActual, PEForecast, DWFActual, DWFForecast):
    genFigPE(dates, PEActual, PEForecast)
    genFigDWF(dates, DWFActual, DWFForecast)


def genFigPE(dates, PEActual, PEForecast):
    ## plot onto one graph
    plt.plot(dates, PEForecast, color='red', label='Predicted')
    plt.plot(dates, PEActual, color='black', label='Recorded')

    ##graph aesthetics
    plt.title("Recorded Population Equivalence versus Predicted Over Time", loc = 'left')
    plt.xlabel("Date Recorded")
    plt.ylabel("Population Equivalent (PE)")
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

    ##save as an image in the working directory
    plt.savefig('PE_plot.png')

    ##close
    plt.close()

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
    plt.savefig('DWF_plot.png')

    ##close
    plt.close()


def genFigSummary(data):
    pass

