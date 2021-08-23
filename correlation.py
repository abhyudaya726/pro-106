import csv
import plotly.express as px
import numpy as np

def drawChart(dataPath):
    with open(dataPath) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df,x="Marks",y="Present")
        fig.show()

def fetchData(dataPath):
    marks = []
    present = []
    with open(dataPath) as f:
        df = csv.DictReader(f)
        for i in df:
            marks.append(float(i["Marks"]))
            present.append(float(i["Present"]))
    return{"x":marks,"y":present}

def calc_correlation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print(correlation)

def setup():
    datapath = "data.csv"
    datasource = fetchData(datapath)
    calc_correlation(datasource)
    drawChart(datapath)

setup()