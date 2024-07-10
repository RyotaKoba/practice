theta = 0.0

def setup():
    size(300,300,P3D)
    
def draw():
    global theta
    background(208)
    
    translate(150,150,0)
    
    pushMatrix()
    rotateY(theta)
    box(50)
    popMatrix()
    
    pushMatrix()
    translate(-80,0,0)
    rotateY(theta)
    box(50)
    popMatrix()
    
    pushMatrix()
    translate(80,0,0)
    rotateY(theta)
    box(50)
    popMatrix()
    
    theta += 0.01
    if theta > TWO_PI:
        theta = 0.0
