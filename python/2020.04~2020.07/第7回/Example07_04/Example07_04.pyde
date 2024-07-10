network = None

def setup():
    global network
    size(300,300)
    shapeMode(CENTER)
    network = loadShape("network.svg")
    
def draw():
    background(0)
    translate(width/2,height/2)
    angle = map(mouseY,0,height,0,TWO_PI)
    rotate(angle)
    diameter = map(mouseX,0,width,10,1000)
    shape(network,0,0,diameter,diameter)
