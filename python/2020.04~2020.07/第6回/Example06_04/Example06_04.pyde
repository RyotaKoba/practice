angle = 0.0
angleDirection = 1
speed = 0.005

def setup():
    size(300,300)
    
def draw():
    global angle,angleDirection
    background(208)
    armrobot(60,280,1)
    armrobot(240,280,-1)
    angle += speed * angleDirection
    if angle > 0.43 or angle < 0:
        angleDirection = -angleDirection
        
def armrobot(x,y,d):
    global angle
    stroke(100)
    pushMatrix()
    translate(x,y)
    rotate(d*angle-HALF_PI)
    strokeWeight(24)
    line(0,0,80,0)
    translate(80,0)
    rotate(d*angle * 2.0)
    strokeWeight(12)
    line(0,0,40,0)
    translate(40,0)
    rotate(d*angle * 1.6)
    strokeWeight(6)
    line(0,0,20,0)
    translate(20,0)
    if d*angleDirection == 1:
        rotate(-(d*angle-HALF_PI+d*angle * 2.0+d*angle * 1.6))
        strokeWeight(1)
        atom(0,94,0.5)
    popMatrix()
    
def atom(x,y,s):
    fill(255)
    robot(x,y,s)
    heart(x+12*s,y-100*s,0.3*s)
    
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
