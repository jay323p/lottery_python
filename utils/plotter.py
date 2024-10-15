from static import constants
from matplotlib import pyplot as plt

def getPlotChoice():
    plot = input("Please input which plot type you would like: ")
    if (plot.lower() in constants.PLOTS_VALIDATORS):
        return plot
    else:
        print("ERROR: Invalid plot choice. Please choose from list given above | STATUS: 500")
        return getPlotChoice()

def generate_plot_data(plot: str, game: str, data: list[dict]):
    fx = None
    x = []
    y = []
    if (plot.lower() == "line"):
        fx = plt.plot
    elif (plot.lower() == "scatter"):
        fx = plt.scatter
    for i in range(len(data)):
        x.append(i)
        y.append(data[i].get("payout"))
    fx(x, y)
    plt.show()