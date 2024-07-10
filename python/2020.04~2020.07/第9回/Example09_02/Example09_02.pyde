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
            
atom = HumanoidRobot(150,150,random(5),random(5),True)
gundam = HumanoidRobot(150,150,random(10),random(10),False)

def setup():
    size(300,300)
    
def draw():
    background(200)
    stroke(0)
    atom.display()
    atom.move()
    gundam.display()
    gundam.move()
    
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
