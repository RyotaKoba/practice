time1 = 2000
angle = 0.0
offset = 150.0
scalar = 50.0
speed = 0.05

def setup():
    size(300,300)
    
def draw():
    global angle
    background(204)
    
    y1 = offset + sin(angle)*scalar
    y2 = offset + sin(angle+0.4)*scalar
    y3 = offset + sin(angle+0.8)*scalar
    atom(75,y1,0.4)
    atom(150,y2,0.4)
    atom(225,y3,0.4)
    angle += speed
        
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
