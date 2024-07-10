class HumanoidRobot():
    def __init__(self,x,y,xs,ys,h):
        self.xpos = x
        self.ypos = y
        self.xspeed = xs
        self.yspeed = ys
        self.heart = h
    
    def display(self):
        robot(self.xpos,self.ypos,0.4)
        if self.heart:
            heart(self.xpos+4.8,self.ypos-40,0.12)
    
    def move(self):
        self.xpos += self.xspeed
        self.ypos += self.yspeed
        if self.xpos > width or self.xpos<0:
            self.xpos = - self.xspeed
        if self.ypos > height or self.ypos < 0:
            self.yspeed = - self.yspeed
            
atom = []
gundam = []

def setup():
    size(300,300)
    for i in range(5):
        atom.append(HumanoidRobot(150,150,random(5),random(5),True))
    for i in range(10):
        gundam.append(HumanoidRobot(150,150,random(5),random(5),False))
        
def draw():
    background(208)
    stroke(0)
    for i in range(len(atom)):
        atom[i].display()
        atom[i].move()
    for i in range(len(gundam)):
        gundam[i].display()
        gundam[i].move()
        
def robot(x,y,s):
    pushMatrix()
    translate(x,y)
    stroke(0)
    fill(255)
    #foot
    rect(-40*s,-20*s,40*s,20*s)
    rect(0*s,-20*s,40*s,20*s)
    #leg
    rect(-30*s,-80*s,30*s,60*s)
    rect(0*s,-80*s,30*s,60*s)
    #arm
    rect(-50*s,-140*s,20*s,80*s)
    rect(30*s,-140*s,20*s,80*s)
    #body
    rect(-30*s,-140*s,60*s,60*s)
    #head
    rect(-20*s,-180*s,40*s,40*s)
    popMatrix()
    
def heart(x,y,s):
    pushMatrix()
    translate(x,y)
    fill(255,0,0)
    noStroke()
    beginShape()
    vertex(0,0)
    bezierVertex(-80*s,-40*s,-40*s,-120*s,0,-80*s)
    bezierVertex(40*s,-120*s,80*s,-40*s,0,0)
    endShape()
    popMatrix()
