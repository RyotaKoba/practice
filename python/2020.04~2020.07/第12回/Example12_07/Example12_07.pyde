theta = 0.0

def setup():
    size(300,300,P3D)
    
def draw():
    global theta
    background(208)
    
    lights()
    translate(width/2,height/2)
    
    pushMatrix()
    rotateX(theta)
    rotateY(5.0*theta)
    threeDRobot(0,0,0,5.0)
    popMatrix()
    
    pushMatrix()
    translate(-80,0,0)
    rotateX(theta)
    rotateY(5.0*theta)
    threeDRobot(0,0,0,5.0)
    popMatrix()
    
    pushMatrix()
    translate(80,0,0)
    rotateX(theta)
    rotateY(5.0*theta)
    threeDRobot(0,0,0,5.0)
    popMatrix()
    
    theta += 0.01

def threeDRobot(x,y,z,s):
    fill(200)
    noStroke()
    #foot
    pushMatrix()
    translate(x-2*s,y-s,z+0.5*s)
    box(3*s,2*s,4*s)
    translate(4*s,0,0)
    box(3*s,2*s,4*s)
    popMatrix()
    #leg
    pushMatrix()
    translate(x-1.5*s,y-5*s,z)
    box(2*s,6*s,2*s)
    translate(3*s,0,0)
    box(2*s,6*s,2*s)
    popMatrix()
    #body
    pushMatrix()
    translate(x,y-11*s,z)
    box(6*s,6*s,4*s)
    popMatrix()
    #arm
    pushMatrix()
    translate(x-4*s,y-10*s,z)
    box(2*s,8*s,2*s)
    translate(8*s,0,0)
    box(2*s,8*s,2*s)
    popMatrix()
    #head
    pushMatrix()
    translate(x,y-16*s,z)
    box(3*s,3*s,2*s)
    popMatrix()
    #heart
    pushMatrix()
    translate(x+10,y-11*s,2.2*s)
    heart(0,0,s/50.0)
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
