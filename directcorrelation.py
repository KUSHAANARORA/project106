import csv
import numpy as ny

def setup():
    datapath = "C://Users//i_kap//Desktop//Kushaan//csv files//Student Marks vs Days Present.csv"
    data = dataRetrival(datapath)
    getcorrelationnumber(data)

def getcorrelationnumber(data):
    correlationnumber = ny.corrcoef(data["x"],data["y"])
    print(correlationnumber)

def dataRetrival(datapath):
    Marks = []
    DaysPresent = []
    with open(datapath) as f:
        df = csv.DictReader(f)
        for i in df:
            Marks.append(float(i["Marks In Percentage"]))
            DaysPresent.append(float(i["Days Present"]))
    return {"x":Marks,"y":DaysPresent}



setup()
