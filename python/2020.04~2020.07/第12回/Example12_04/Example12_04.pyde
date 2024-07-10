theta = 0.0

def setup():
    size(300,300,P3D)
    
def draw():
    global theta
    background(208)
    translate(150,150,0)
    rotateY(theta)
    box(100)
    theta += 0.01
    if theta > TWO_PI:
        theta = 0.0
