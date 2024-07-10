#Apple+Bubble
class Bupple():
    def __init__(self,x,y,xs,ys,c,s,r,t):
        self.xpos = x
        self.ypos = y
        self.xspeed = xs
        self.yspeed = ys
        self.Color = c
        self.Size = s
        self.radian = r
        self.rota = t
        
    def ringo(self):
        apple(self.Color,self.xpos,self.ypos,self.Size,self.radian)
        
    def en(self):
        bubble(self.xpos,self.ypos,self.Size,self.Color)
            
    def move(self):
        self.xpos += self.xspeed
        self.ypos += self.yspeed
        self.radian += self.rota
        if self.xpos > width-40 or self.xpos < 40:
            self.xspeed = -self.xspeed
        if self.ypos > height-40 or self.ypos < 40:
            self.yspeed = -self.yspeed
        
    def change(self):
        self.Color = color(random(101,255),random(101,255),random(101,255))
        self.xpos = random(0,width)
        self.ypos = random(0,height)
        self.Size = random(20,100)
    
        
app = Bupple(150,150,0.2,0.2,0,0.4,0,0.1)
bite = Bupple(0,0,0,0,0,10,0,0)

def setup():
    size(300,300)
    background(0)
    
def draw():
    bite.change()
    bite.en()
    bite.change()
    bite.en()
    bite.change()
    bite.en()
    bite.change()
    bite.en()
    bite.change()
    bite.en()
    bite.change()
    bite.en()
    bite.change()
    bite.en()
    bite.change()
    bite.en()
    app.ringo()
    app.move()
    
    
def bubble(x,y,s,c):
    noStroke()
    fill(c)
    ellipse(x,y,s,s)
    
def apple(c,x,y,s,z):
    pushMatrix()
    translate(x,y)
    rotate(radians(z))
    fill(c)
    noStroke()
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
