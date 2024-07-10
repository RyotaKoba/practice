radius = 40.0
x = 110.0
speed = 0.5
direction = 1

def setup():
    size(300,300)
    ellipseMode(RADIUS)
    
def draw():
    global x,direction
    background(208)
    noStroke()
    fill(255)
    x += speed*direction
    if x > width-radius or x < radius:
        direction = -direction
    if direction == 1:
        arc(x,110,radius,radius,0.52,5.76)
    else:
        arc(x,110,radius,radius,3.69,8.9)
