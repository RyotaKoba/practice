def setup():
    size(300,300)
    
def draw():
    background(208)
    translate(mouseX,mouseY)
    atom(0,0,0.6)
    translate(40,0)
    atom(0,0,0.3)
    
def atom(x,y,s):
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
