#Psycho Apple Wave
class Apple():
    def __init__(self,x,y,xs,ys,c):
        self.xpos = x
        self.ypos = y
        self.xspeed = xs
        self.yspeed = ys
        self.Color = c
        self.angle = 0
        
    def ringo(self):
        apple(self.Color,self.xpos,self.ypos,0.8)
            
    def move(self):
        self.xpos = (width/2) + sin(self.angle + radians(self.xspeed))*15
        self.ypos = (height/2) + sin(self.angle + radians(self.yspeed))*15
        self.angle += random(0.01,0.05)
        
Color = [color(255,0,2),color(255,35,0),color(255,73,0),color(255,111,0),
         color(255,149,0),color(255,187,0),color(248,255,0),color(210,255,0),
         color(172,255,0),color(134,255,0),color(96,255,0),color(58,255,0),
         color(0,255,17),color(0,255,55),color(0,255,93),color(0,255,131),
         color(0,255,169),color(0,255,207),color(0,228,255),color(255,0,20),
         color(255,0,40),color(255,0,116),color(255,0,154),color(255,0,192),
         color(243,0,255),color(205,0,255),color(167,0,255),color(129,0,255),
         color(91,0,255),color(53,0,255),color(0,0,255),color(0,38,255),
         color(0,76,255),color(0,114,255),color(0,152,255),color(0,190,255)]

app = []

def setup():
    size(400,400)
    background(0)
    for i in range(len(Color)):
        app.append(Apple(150,150,random(-180,180),random(-180,180),Color[i]))
    
def draw():
    background(0)
    for i in range(len(app)):
        app[i].ringo()
        app[i].move()    
    
def apple(c,x,y,s):
    pushMatrix()
    translate(x,y)
    #rotate(radians(z))
    #fill(c)
    fill(0,0,0,0)
    strokeWeight(10)
    stroke(c,40)
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
    #fill(v2)
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
