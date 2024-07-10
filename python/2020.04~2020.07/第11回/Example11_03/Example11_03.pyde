import csv

homeRuns = list()
battingAverages = list()

statsFileHandle = open("ortiz.csv")
statsData = csv.reader(statsFileHandle)

for row in statsData:
    homeRuns.append(int(row[1]))
    battingAverages.append(float(row[3]))
    
print homeRuns
print battingAverages
