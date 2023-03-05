import pandas as pd
import matplotlib.pyplot as plt
# ensures matplotlib does not generate a GUI, necessary for integration with flask
plt.matplotlib.use('Agg')

# function called in integratedSoftware, used to generate both figures
def generateFigures(dates, PEActual, PEForecast, DWFActual, DWFForecast):
    genFigPE(dates, PEActual, PEForecast)
    genFigDWF(dates, DWFActual, DWFForecast)

# function used to generate line graph comparing SOLAR PE forecast with reported
# PE figures
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
    plt.savefig('DWF_plot.png')

    ##close
    plt.close()