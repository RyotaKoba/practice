import json
dis = 1500.000
disx = 390
lightyear = None
byouga = None
flag = False
Orionflag = False
Ursaflag = False
Scorpflag = False

signs = []
orion = []
UrsaMajor = []
Scorp = []

def setup():
    global lightyear,byouga
    size(500,360)
    background(60,20,160)
    stroke(255)
    strokeCap(ROUND)
    strokeWeight(10)
    line(100,20,400,20)
    lightyear = loadImage("kounen.jpg")
    byouga = loadImage("byouga.jpg")
    image(byouga,75,32,110,27.5)
    image(lightyear,250,40,40,20)
    fill(255)
    textSize(20)
    text(int(dis),200,55)
    fill(0)
    ellipse(390,20,20,20)
    stroke(0)
    strokeWeight(2)
    fill(255)
    rect(410,70,80,30)
    rect(410,120,80,30)
    rect(410,170,80,30)
    rect(410,220,80,30)
    rect(410,270,80,30)
    rect(410,320,80,30)
    textSize(20)
    fill(0)
    text("Orion",422,95)
    text("None",425,245)
    text("None",425,295)
    text("None",425,345)
    textSize(14)
    text("Ursa Major",413,141)
    textSize(16)
    text("Scorpius",417,194)
    signHandle = open("kadai-10.json")
    signs = json.load(signHandle)
    for i in range(len(signs)):
        sign = signs[i]
        if sign["sign"] == "Orion":
            orion.append(sign)
        if sign["sign"] == "Ursa Major":
            UrsaMajor.append(sign)
        if sign["sign"] == "Scorpius":
            Scorp.append(sign)
    s = 'When you hover over a star, \n you can see its info.\nexample)\nDistance:\nName:'
    fill(255)
    textSize(12)
    text(s,5,80)
    
def draw():
    fill(0)
    noStroke()
    ellipse(250,210,300,300)
    distance()
    if Orionflag:
        for i in range(len(orion)):
            orions = orion[i]
            if dis > orions["distance"]:
                fill(255)
                ellipse(orions["x"],orions["y"],4,4)
                info(orions["x"],orions["y"],orions["name"],orions["distance"])
    if Ursaflag:
        for i in range(len(UrsaMajor)):
            UrsaMajors = UrsaMajor[i]
            if dis > UrsaMajors["distance"]:
                fill(255)
                ellipse(UrsaMajors["x"],UrsaMajors["y"],4,4)
                info(UrsaMajors["x"],UrsaMajors["y"],UrsaMajors["name"],UrsaMajors["distance"])
    if Scorpflag:
        for i in range(len(Scorp)):
            Scorpius = Scorp[i]
            if dis > Scorpius["distance"]:
                if Scorpius["name"] == "Antares":
                    fill(255,0,0)
                    ellipse(Scorpius["x"],Scorpius["y"],5,5)
                    info(Scorpius["x"],Scorpius["y"],Scorpius["name"],Scorpius["distance"])
                else:
                    fill(255)
                    ellipse(Scorpius["x"],Scorpius["y"],4,4)
                    info(Scorpius["x"],Scorpius["y"],Scorpius["name"],Scorpius["distance"])
    
    
def distance():
    global dis,disx
    if flag:
        noStroke()
        fill(60,20,160)
        rect(80,0,340,60)
        stroke(255)
        strokeCap(ROUND)
        strokeWeight(10)
        line(100,20,400,20)
        noStroke()
        if mouseX >= 110 and mouseX <=390:
            fill(255)
            ellipse(mouseX,20,30,30)
            fill(0)
            ellipse(mouseX,20,10,10)
            disx = mouseX
            dis = map(mouseX,110,390,50,1500)
        elif mouseX < 110:
            fill(255)
            ellipse(110,20,30,30)
            fill(0)
            ellipse(110,20,10,10)
            disx = 110
            dis = map(110,110,390,50,1500)
        elif mouseX > 390:
            fill(255)
            ellipse(390,20,30,30)
            fill(0)
            ellipse(390,20,10,10)
            disx = 390
            dis = map(390,110,390,50,1500)
        fill(255)
        textSize(20)
        text(int(dis),200,55)
    image(lightyear,250,40,40,20)
    image(byouga,75,36,110,27.5)

def info(x,y,n,d):
    dn = dist(x,y,mouseX,mouseY)
    fill(255)
    if dn < 5:
        if n == "Alkaid" or n == "Acrab" or  n == "Bellatrix":
            textSize(15)
            text(n,x-21,y-5)
            text(d,x-21,y-17)
        elif n == "Dschubba":
            textSize(15)
            text(n,x-35,y)
            text(d,x-35,y-12)
        elif n == "Betelgeuse":
            textSize(15)
            text(n,x+4,y+8)
            text(d,x+4,y-4)
        else:
            textSize(15)
            text(n,x,y-5)
            text(d,x,y-17)
                    
def mousePressed():
    global flag,Orionflag,Ursaflag,Scorpflag
    d = dist(disx,20,mouseX,mouseY)
    if d < 10:
        flag = True
    if mouseX >= 410 and mouseX <=490 and mouseY >= 70 and mouseY <= 100:
        Orionflag = True
        Ursaflag = False
        Scorpflag = False
    if mouseX >= 410 and mouseX <=490 and mouseY >= 120 and mouseY <= 150:
        Orionflag = False
        Ursaflag = True
        Scorpflag = False
    if mouseX >= 410 and mouseX <=490 and mouseY >= 170 and mouseY <= 200:
        Orionflag = False
        Ursaflag = False
        Scorpflag = True
        
def mouseReleased():
    global flag
    flag = False
