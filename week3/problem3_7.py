import csv

def problem3_7(pricefile,flowername):
    with open(pricefile, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for r in reader:
               #print(r)
               if flowername in r:
                   print(r[1])