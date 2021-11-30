import csv 
import numpy as np

def setup():
    dataPath = "screenTime.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)

def getDataSource(data_path):
    tvSize = []
    timespent = []
    with open (data_path) as csvfile:
        csv_reader = csv.DictReader(csvfile)

        for row in csv_reader:
            tvSize.append(float(row["Size of TV"]))
            timespent.append(float(row["\tAverage time spent watching TV in a week"]))
    return {"x":tvSize,"y":timespent}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"]) 
    print("Correlation between TV Size and TV time :- \n--->",correlation[0,1])
setup()