import numpy
import csv
import plotly.express as pe

def setup():
    opener = open("cups of coffee vs hours of sleep.csv")
    reader = csv.reader(opener)
    whole = list(reader)
    coffee_List = []
    sleep_List = []
    def getDataSource():
        for i in range(len(whole)):
            coffee = whole[i][1]
            coffee_List.append(float(coffee))
        for i in range(len(whole)):
            sleep = whole[i][2]
            sleep_List.append(float(sleep))
    def findCorrelation():
        coefficient = numpy.corrcoef(coffee_List,sleep_List)
        print(coefficient)
    def plotFigure():
        fig = pe.scatter(x="Coffee in ml",y="sleep in hours",title="Cups of coffee vs Hours of sleep")
        fig.show()
    getDataSource()
    findCorrelation()
    plotFigure()

setup()