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
