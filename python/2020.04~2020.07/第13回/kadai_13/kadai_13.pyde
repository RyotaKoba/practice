add_library('sound')

x = 250
y = 408
z = 1750
s = 1.00
r = 255
g = 0
b = 0
xShaft = 0
yShaft = 0
flag = False
yflag = False
theta = 0
stheta = 0
count = 0
imgNames = []
BGM = None

class structure():
    def __init__(self,xp,yp,zp,xl,l):
        self.xpos = xp
        self.ypos = yp
        self.zpos = zp
        self.xpole = xl
        self.lengh = l
    
    def skytree(self):
        X = self.xpos-x
        Y = self.ypos-y
        Z = self.zpos-z
        SkyTree(X,Y,Z,yShaft)
        
    def Floor(self):
        pushMatrix()
        fill(208)
        stroke(0)
        rotateY(radians(yShaft))
        X = self.xpos-x
        Y = self.ypos-y
        Z = self.zpos-z
        translate(X,Y,Z)
        box(5000,50,5000)
        popMatrix()
    
    def smallbuilding(self):
        pushMatrix()
        fill(0)
        stroke(255)
        rotateY(radians(yShaft))
        X = self.xpos-x
        Y = self.ypos-y
        Z = self.zpos-z
        translate(X,Y,Z)
        box(150,400,300)
        popMatrix()
        pushMatrix()
        rotateY(radians(yShaft))
        if self.xpos < 250:
            i = 1
        else:
            i = -1
        X = self.xpos - x
        Y = self.ypos - y
        Z = self.zpos - z
        translate(X+(75.1*i),Y-235,Z+150)
        rotateY(radians(90))
        image(imgNames[self.lengh],0,0,300,440)
        popMatrix()
        
    def mediumbuilding(self):
        pushMatrix()
        fill(0)
        stroke(255)
        rotateY(radians(yShaft))
        X = self.xpos - x
        Y = self.ypos - y
        Z = self.zpos - z
        translate(X,Y,Z)
        box(150,550,300)
        popMatrix()
        pushMatrix()
        rotateY(radians(yShaft))
        if self.xpos < 250:
            i = 1
        else:
            i = -1
        X = self.xpos - x
        Y = self.ypos - y
        Z = self.zpos - z
        translate(X+(75.1*i),Y-275,Z+150)
        rotateY(radians(90))
        image(imgNames[self.lengh],0,0,300,480)
        popMatrix()
        
    def largebuilding(self):
        pushMatrix()
        fill(0)
        stroke(255)
        rotateY(radians(yShaft))
        X = self.xpos - x
        Y = self.ypos - y
        Z = self.zpos - z
        translate(X,Y,Z)
        box(150,700,300)
        popMatrix()
        pushMatrix()
        rotateY(radians(yShaft))
        if self.xpos < 250:
            i = 1
        else:
            i = -1
        X = self.xpos - x
        Y = self.ypos - y
        Z = self.zpos - z
        translate(X+(75.1*i),Y-350,Z+150)
        rotateY(radians(90))
        image(imgNames[self.lengh],0,0,300,550)
        popMatrix()
        
    def curbstone(self):
        pushMatrix()
        fill(208)
        stroke(0)
        rotateY(radians(yShaft))
        X = self.xpos - x
        Y = self.ypos - y
        Z = self.zpos - z
        translate(X,Y,Z)
        rotateY(radians(self.xpole))
        box(5,4,self.lengh)
        popMatrix()
        
    def moon(self):
        pushMatrix()
        noStroke()
        fill(255,222,0)
        rotateY(radians(yShaft))
        X = self.xpos - x
        Y = self.ypos - y
        Z = self.zpos - z
        translate(X,Y,Z)
        sphere(200)
        popMatrix()
        
    def apple(self):
        X = self.xpos - x
        Y = self.ypos - y
        Z = self.zpos - z
        apple(X,Y,Z,yShaft)
        
    def stage(self):
        pushMatrix()
        fill(138,191,138)
        stroke(255)
        rotateY(radians(yShaft))
        X = self.xpos - x
        Y = self.ypos - y
        Z = self.zpos - z
        translate(X,Y,Z)
        box(6642,8,1000)
        popMatrix()

class paint():
    def __init__(self,name,xs,ys,zs,xp,zp,IH,IW,t,xf,yf):
        self.ImgName = name 
        self.xpos = xs
        self.ypos = ys
        self.zpos = zs
        self.xpole = xp
        self.zpole = zp
        self.ImgHeight = IH
        self.ImgWeight = IW
        self.times = t
        self.xfrequency = xf
        self.yfrequency = yf
        
    def paper(self):
        pushMatrix()
        rotateY(radians(yShaft))
        X = self.xpos - x
        Y = self.ypos - y
        Z = self.zpos - z
        translate(X,Y,Z)
        rotateX(radians(self.xpole))
        rotateZ(radians(self.zpole))
        image(imgNames[self.ImgName],0,0,self.ImgWeight,self.ImgHeight)
        popMatrix()
        
    def longpaper(self):
        pushMatrix()
        rotateY(radians(yShaft))
        X = self.xpos - x
        Y = self.ypos - y
        Z = self.zpos - z
        translate(X,Y,Z)
        rotateX(radians(self.xpole))
        rotateZ(radians(self.zpole))
        for i in range(self.times):
            image(imgNames[self.ImgName],0 + i*self.xfrequency ,0 + i*self.yfrequency ,self.ImgWeight,self.ImgHeight)
        popMatrix()
        
def setup():
    global imgNames
    size(500,500,P3D)
    noCursor()
    BGM = SoundFile(this,"wind.wav")
    imgNames.append(loadImage("road.jpg"))         #[0]
    imgNames.append(loadImage("intersection.jpg")) #[1]
    imgNames.append(loadImage("renga.jpg"))        #[2]
    imgNames.append(loadImage("side1.jpg"))        #[3]
    imgNames.append(loadImage("parking.jpg"))      #[4]
    imgNames.append(loadImage("front1.jpg"))       #[5]
    imgNames.append(loadImage("front2.jpg"))       #[6]
    imgNames.append(loadImage("front3.jpg"))       #[7]
    imgNames.append(loadImage("front4.jpg"))       #[8]
    imgNames.append(loadImage("front5.jpg"))       #[9]
    imgNames.append(loadImage("front6.jpg"))       #[10]
    imgNames.append(loadImage("background.jpg"))   #[11]
    #BGM.play()
    #fullScreen()

def draw():
    global x,y,z,yShaft
    background(18,11,57)
    yShaft = map(mouseX,0,500,-90,90)
    translate(x,y,z)
    rotateY(radians(-yShaft))
    move()
    jump()
    Colorchange()
    xShaft = mouseY-380
    camera(0,0,0,0,xShaft,-170+80,0,1,0)
    buildingSide1 = paint(3,-5,-65,810.1,0,0,490,150,0,0,0)
    buildingSide2 = paint(7,-5,-125,1350.1,0,0,550,150,0,0,0)
    buildingSide3 = paint(7,355,-125,1450.1,0,0,550,150,0,0,0)
    parking = paint(4,-40,424,1050,90,-90,185.5,240,0,0,0)
    road1 = paint(0,200,424,0,-90,-90,100,400,4,400,0)
    road2 = paint(0,-380,424,-181,-90,0,100,400,0,0,0)
    road3 = paint(0,482,424,-181,-90,0,100,400,0,0,0)
    walkwayL = paint(2,148,423.9,-150,-90,0,30,50,60,0,-30)
    walkwayR = paint(2,302,423.9,-150,-90,0,30,50,60,0,-30)
    walkwayR2 = paint(2,352,423.9,-180,-90,-90,30,50,30,0,30)
    walkwayL2 = paint(2,118,423.9,-180,-90,-90,30,50,30,0,-30)
    intersection1 = paint(1,20,424,-462,-90,-90,462,462,0,0,0)
    Back = paint(11,-2000,-130,-1130,0,0,630,1107,5,1107,0)
    Stage = structure(1321,421,-800,0,0)
    AppleStore = structure(354.8,275,340,0,0)
    MOON = structure(-200,-3500,-700,0,0)
    curb1 = structure(198,423,350,0,800)
    curb2 = structure(302,423,775,0,1650)
    curb3 = structure(302,423,-170,0,25)
    curb4 = structure(198,423,-170,0,25)
    curb5 = structure(317,423,-180,-90,25)
    curb6 = structure(183,423,-180,90,25)
    curb7 = structure(610,423,-180,-90,400)
    curb7 = structure(-110,423,-180,90,400)
    curb8 = structure(198,423,1250,0,700)
    skyscraper1 = structure(70,225,20,0,8)
    skyscraper2 = structure(70,225,340,0,6)
    skyscraper3 = structure(70,225,660,0,5)
    skyscraper4 = structure(70,225,1200,0,7)
    skyscraper5 = structure(-120,225,800,0,3)
    skyscraper6 = structure(-120,225,1120,0,3)
    skyscraper7 = structure(430,225,20,0,9)
    skyscraper8 = structure(430,225,340,0,10)
    skyscraper9 = structure(430,225,660,0,6)
    skyscraper10 = structure(430,225,980,0,5)
    skyscraper11 = structure(430,225,1300,0,7)
    base = structure(-500,450,500,0,0)
    SKYTREE = structure(250,1100,-800,0,0)
    Back.longpaper()
    buildingSide1.paper()
    buildingSide2.paper()
    buildingSide3.paper()
    parking.paper()
    intersection1.paper()
    road1.longpaper()
    road2.paper()
    road3.paper()
    walkwayL.longpaper()
    walkwayL2.longpaper()
    walkwayR.longpaper()
    walkwayR2.longpaper()
    curb1.curbstone()
    curb2.curbstone()
    curb3.curbstone()
    curb4.curbstone()
    curb5.curbstone()
    curb6.curbstone()
    curb7.curbstone()
    curb8.curbstone()
    Stage.stage()
    skyscraper1.smallbuilding()
    skyscraper2.mediumbuilding()
    skyscraper3.mediumbuilding()
    skyscraper4.largebuilding()
    skyscraper5.mediumbuilding()
    skyscraper6.mediumbuilding()
    skyscraper7.largebuilding()
    skyscraper8.smallbuilding()
    skyscraper9.mediumbuilding()
    skyscraper10.mediumbuilding()
    skyscraper11.largebuilding()
    base.Floor()
    SKYTREE.skytree()
    MOON.moon()
    AppleStore.apple()

def jump():
    global count,yflag,stheta,y
    if yflag:
        if count == 60:
            yflag = False
            y = 408
            stheta = 0
            count = 0
        else:
            y = 408
            y -= sin(radians(stheta))*5
            stheta += 3
            count +=1
            
def SkyTree(A,B,C,yShaft):
    global theta
    pushMatrix()
    s = 10.0
    rotateY(radians(yShaft))
    translate(A,B,C)
    for i in range(360):
        rotateY(radians(theta))
        noFill()
        stroke(r,g,b)
        beginShape()
        vertex(0,-68*s,0)
        vertex(-22*s,-68*s,0*s)
        vertex(-10*s,-282*s,0*s)
        vertex(-13*s,-289*s,0*s)
        vertex(-14*s,-290*s,0*s)
        vertex(-20*s,-306*s,0*s)
        vertex(-18*s,-306*s,0*s)
        vertex(-19*s,-313*s,0*s)
        vertex(-19*s,-315*s,0*s)
        vertex(-19*s,-313*s,0*s)
        vertex(-10*s,-313*s,0*s)
        vertex(-10*s,-320*s,0*s)
        vertex(-9*s,-320*s,0*s)
        vertex(-8*s,-353*s,0*s)
        vertex(-12*s,-367*s,0*s)
        vertex(-9*s,-367*s,0*s)
        vertex(-8*s,-372*s,0*s)
        vertex(-6*s,-372*s,0*s)
        vertex(-6*s,-392*s,0*s)
        vertex(-2*s,-392*s,0*s)
        vertex(-2*s,-474*s,0*s)
        vertex(-4*s,-478*s,0*s)
        vertex(-4*s,-484*s,0*s)
        vertex(0*s,-484*s,0*s)
        vertex(0*s,-68*s,0*s)
        vertex(-22*s,-68*s,0*s)
        endShape()
        stroke(255)
        beginShape()
        vertex(0*s,-50*s,0)
        vertex(-32*s,-50*s,0)
        vertex(-32*s,-68*s,0)
        vertex(0,-68*s,0)
        vertex(0,-50*s,0)
        endShape()
        theta += 1
    popMatrix()   

def apple(x,y,z,yShaft):
    pushMatrix()
    s = 0.2
    rotateY(radians(yShaft))
    translate(x,y,z)
    rotateY(radians(-90))
    fill(255)
    stroke(255)
    beginShape()
    curveVertex(0*s,118*s)
    curveVertex(0*s,118*s)
    curveVertex(-10*s,120*s)
    curveVertex(-20*s,124*s)
    curveVertex(-30*s,128*s)
    curveVertex(-40*s,132*s)
    curveVertex(-50*s,134*s)
    curveVertex(-60*s,131*s)
    curveVertex(-70*s,124*s)
    curveVertex(-80*s,116*s)
    curveVertex(-90*s,106*s)
    curveVertex(-95*s,100*s)
    curveVertex(-100*s,94*s)
    curveVertex(-102*s,90*s)
    curveVertex(-104*s,86*s)
    curveVertex(-107*s,80*s)
    curveVertex(-110*s,74*s)
    curveVertex(-114*s,66*s)
    curveVertex(-116*s,60*s)
    curveVertex(-120*s,50*s)
    curveVertex(-124*s,40*s)
    curveVertex(-127*s,30*s)
    curveVertex(-130*s,18*s)
    curveVertex(-131*s,10*s)
    curveVertex(-132*s,0*s)
    curveVertex(-133*s,-10*s)
    curveVertex(-134*s,-20*s)
    curveVertex(-133*s,-30*s)
    curveVertex(-132*s,-40*s)
    curveVertex(-129*s,-50*s)
    curveVertex(-124*s,-60*s)
    curveVertex(-120*s,-68*s)
    curveVertex(-110*s,-80*s)
    curveVertex(-100*s,-90*s)
    curveVertex(-90*s,-98*s)
    curveVertex(-80*s,-104*s)
    curveVertex(-60*s,-106*s)
    curveVertex(-40*s,-105*s)
    curveVertex(-20*s,-98*s)
    curveVertex(-10*s,-95*s)
    curveVertex(-4*s,-95*s)
    curveVertex(0,-95*s)
    curveVertex(20*s,-103*s)
    curveVertex(40*s,-108*s)
    curveVertex(60*s,-109*s)
    curveVertex(80*s,-104*s)
    curveVertex(100*s,-94*s)
    curveVertex(116*s,-78*s)
    curveVertex(107*s,-70*s)
    curveVertex(100*s,-64*s)
    curveVertex(90*s,-50*s)
    curveVertex(86*s,-40*s)
    curveVertex(83*s,-30*s)
    curveVertex(82*s,-20*s)
    curveVertex(85*s,0*s)
    curveVertex(90*s,12*s)
    curveVertex(100*s,29*s)
    curveVertex(110*s,40*s)
    curveVertex(124*s,49*s)
    curveVertex(120*s,62*s)
    curveVertex(110*s,82*s)
    curveVertex(100*s,97*s)
    curveVertex(80*s,120*s)
    curveVertex(70*s,130*s)
    curveVertex(60*s,133*s)
    curveVertex(40*s,129*s)
    curveVertex(20*s,120*s)
    curveVertex(0,118*s)
    curveVertex(0,118*s)
    endShape()
    beginShape()
    curveVertex(-7*s,-111*s)
    curveVertex(-7*s,-111*s)
    curveVertex(-7*s,-120*s)
    curveVertex(-5*s,-130*s)
    curveVertex(0*s,-142*s)
    curveVertex(10*s,-156*s)
    curveVertex(20*s,-166*s)
    curveVertex(30*s,-175*s)
    curveVertex(40*s,-183*s)
    curveVertex(50*s,-188*s)
    curveVertex(58*s,-188*s)
    curveVertex(60*s,-180*s)
    curveVertex(59*s,-170*s)
    curveVertex(56*s,-160*s)
    curveVertex(52*s,-152*s)
    curveVertex(46*s,-140*s)
    curveVertex(38*s,-130*s)
    curveVertex(26*s,-120*s)
    curveVertex(12*s,-112*s)
    curveVertex(0,-110*s)
    curveVertex(-7*s,-111*s)
    curveVertex(-7*s,-111*s)
    endShape()
    popMatrix() 
            
def keyPressed():
    global flag
    flag = True
    
def keyReleased():
    global flag
    flag = False
        
def move():
    global x,z,flag,yflag
    if flag:
        if key == 'w':
            z -= 2
        elif key == 's':
            z += 2
        elif key == 'a':
            x -= 2
        elif key == 'd':
            x += 2
        elif key == ' ':
            yflag = True

def Colorchange():
    global r,g,b
    #n kisuu only
    n = 3
    if g < 130 and b == 0:
        g += n
    elif g < 255 and b == 0:
        g += n
        r -= n
    elif r > 30 and b == 0:
        r -= n
    elif r > 0 and g == 255:
        r -= n
        b += n
    elif b < 205 and r == 0:
        b += n
    elif b < 255 and r == 0:
        b += n
        g -= n
    elif g > 0 and b == 255 and r == 0:
        g -= n
    elif r < 240 and g == 0:
        r += n
    elif r < 255 and g == 0:
        r += n
        b -= n
    elif b > 0 and g == 0:
        b -= n
