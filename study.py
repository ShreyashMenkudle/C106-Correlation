import csv 
import numpy as np

def setup():
    dataPath = "mark.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)

def getDataSource(data_path):
    days = []
    marks = []
    with open (data_path) as csvfile:
        csv_reader = csv.DictReader(csvfile)

        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
            days.append(float(row["Days Present"]))
    return {"x":marks,"y":days}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"]) 
    print("Correlation between Marks in percentage and Days present :- \n--->",correlation[0,1])
setup()