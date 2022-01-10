import numpy
import csv
import plotly.express as pe

def setup():
    opener = open("Student Marks vs Days Present.csv")
    reader = csv.reader(opener)
    whole = list(reader)
    marks_list = []
    days_list = []
    def getDataSource():
        for i in range(len(whole)):
            marks = whole[i][1]
            marks_list.append(float(marks))
        for i in range(len(whole)):
            days = whole[i][2]
            days_list.append(float(days))
    def findCorrelation():
        coefficient = numpy.corrcoef(marks_list,days_list)
        print(coefficient)
    def plotFigure():
        fig = pe.scatter(x="Marks In Percentage",y="Days Present",title="Student Marks vs Days Present")
        fig.show()
    getDataSource()
    findCorrelation()
    plotFigure()

setup()