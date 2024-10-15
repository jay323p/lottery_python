import constants
from matplotlib import pyplot as plt

def getPlotChoice():
    plot = input("Please input which plot type you would like: ")
    if (plot.lower() in constants.PLOTS_VALIDATORS):
        return plot
    else:
        print("ERROR: Invalid plot choice. Please choose from list given above | STATUS: 500")
        return getPlotChoice()

def generate_plot_data(plot: str, game: str, data):
    fx = None
    if (plot.lower() == "line"):
        fx = plt.plot
    elif (plot.lower() == "scatter"):
        fx = plt.scatter
    fx([1,2,3,4,5], [9,8,7,6,5])
    plt.show()