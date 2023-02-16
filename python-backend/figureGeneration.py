import pandas as pd
import matplotlib.pyplot as plt
from integratedSoftware import DWFCalc

def cleanString(data):
    ## replaces the commas and spaces in each item in the dataframe
    data = data.replace(',', '')
    data = data.replace(' ', '')
    ## converts each value into an integer
    data = int(data)
    return data

def generateFigures(data):

    """
    take in processed data
    generate figures and graphs in matplotlib
    save figures as files to use in HTML report

    NOTES ON USiNG PANDAS AND MATPLOTLIB TO DRAW PLOTS:

    NOTE: this works on whole data, series, and dataFrame

    plotting all data:
        >data.plot()
        >plt.show()

    plotting only one column:
        >data["<VARIABLE NAME>"].plot()
        >plt.show()

    plotting different graphs:
        >data.plot.<GRAPH/PLOT TYPE>(parameters)
        >plt.shot()

        example:
        >data.plot.scatter(x = <VARIABLE 1>, y = <VARIABLE 2>, ...)
        >plt.show()


    """

    def genFigPE(pe_data):
        ## read in data
        data = pd.read_csv("dummyData.csv")

        ## convert date to correct format
        data['DATE'] = data['DATE'].apply(pd.to_datetime)

        ##call the cleanString() function on the values
        data['PE (forecasted 2021)']= data['PE (forecasted 2021)'].map(lambda a: cleanString(a))
        data['PE (unrounded 2020)']= data['PE (unrounded 2020)'].map(lambda a: cleanString(a))

        ## plot onto one graph
        data.plot(x = 'DATE', y = ['PE (forecasted 2021)', 'PE (unrounded 2020)'], kind = "line", color = ['black', 'red'])

        ##graph aesthetics
        plt.title("Recorded Population Equivalence versus Predicted Over Time", loc = 'left')
        plt.xlabel("Date Recorded")
        plt.ylabel("Population Equivalent (PE)")
        plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

        ##save as an image in the working directory
        plt.savefig('PE_plot.png')

        ##close
        plt.show()

    def genFigDWF(dwf_data):
        ## read in data
        data = pd.read_csv("dummyData.csv")

        ## convert date to correct format
        data['DATE'] = data['DATE'].apply(pd.to_datetime)

        ##call the cleanString() function on the values
        data['I_DWF (l/s)']= data['I_DWF (l/s)'].map(lambda a: cleanString(a))
        

        ## plot onto one graph
        data.plot(x = 'DATE', y = [DWFCalc,'I_DWF (l/s)'], kind = "line", color = ["black", "red"])

        ##graph aesthetics
        plt.title("Recorded Dry Weather Flow versus Predicted Over Time", loc = 'left')
        plt.xlabel("Date Recorded")
        plt.ylabel("Dry Weather Flow (DWF)")
        plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

        ##save as an image in the working directory
        plt.savefig('DWF_plot.png')

        ##close
        plt.close()


    def genFigSummary(summary_data):
        pass
    
generateFigures()