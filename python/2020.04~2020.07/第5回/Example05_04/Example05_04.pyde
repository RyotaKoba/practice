x = 150
y = 150
radius = 12

def setup():
    size(300,300)
    
    ellipseMode(RADIUS)
    
def draw():
    global radius
    background(208)
    d = dist(mouseX,mouseY,x,y)
    if radius > width/2:
        radius = 12
    elif d < radius:
        radius += 1
        fill(0)
    else:
        fill(255)
    ellipse(x,y,radius,radius)
