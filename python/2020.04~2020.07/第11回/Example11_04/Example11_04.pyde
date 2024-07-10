import csv

gWidth = 260
gHeight = 260
offsetX = 20
offsetY = 280
maxRange = 100
easing = 0.04

homeRuns = list()
battingAverages = list()
bar = list()

def setup():
    size(300,300)
    statsFileHandle = open("ortiz.csv")
    statsData = csv.reader(statsFileHandle)
    for row in statsData:
        homeRuns.append(int(row[1]))
        battingAverages.append(float(row[3]))
        bar.append(offsetY)
        
def draw():
    background(204)
    stroke(153)
    strokeWeight(1)
    line(offsetX,offsetY,offsetX,offsetY-gHeight)
    line(offsetX,offsetY,offsetX+gWidth,offsetY)
    
    for i in range(len(homeRuns)):
        x = map(i,0,len(homeRuns)-1,offsetX,offsetY+gWidth)
        line(x,offsetY-gHeight,x,offsetY)
        
    for i in range(0,maxRange,5):
        y = map(i,0,maxRange,offsetY-gHeight,offsetY)
        line(offsetX,y,offsetX+gWidth,y)
        
    stroke(0)
    strokeWeight(10)
    for i in range(len(homeRuns)):
        x = map(i,0,len(homeRuns)-1,offsetX,offsetX+gWidth)
        y = map(homeRuns[i],0,maxRange,offsetY,offsetY-gHeight)
        bar[i] += (y-bar[i])*easing
        line(x,offsetY,x,bar[i])
        
    noFill()
    stroke(255,0,0)
    strokeWeight(2)
    beginShape()
    for i in range(len(battingAverages)):
        x = map(i,0,len(battingAverages)-1,offsetX,offsetX+gWidth)
        y = offsetY-battingAverages[i]*gHeight
        vertex(x,y)
    endShape()
