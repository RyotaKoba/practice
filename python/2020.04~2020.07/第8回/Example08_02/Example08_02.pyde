radius = 40.0
x = 110.0
speed = 0.5

def setup():
    size(300,300)
    ellipseMode(RADIUS)
    
def draw():
    global x,direction
    background(208)
    noStroke()
    fill(255)
    x += speed
    if x > width+radius:
        x = -radius
    else:
        arc(x,110,radius,radius,0.52,5.76)
