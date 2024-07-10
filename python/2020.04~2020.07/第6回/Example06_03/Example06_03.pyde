angle = 0.0
angelDirection = 1
speed = 0.005

def setup():
    size(300,300)
    
def draw():
    global angelDirection,angle
    background(208)
    stroke(0)
    translate(50,50)
    rotate(angle)
    strokeWeight(24)
    line(0,0,80,0)
    translate(80,0)
    rotate(angle*2.9)
    strokeWeight(12)
    line(0,0,60,0)
    translate(60,0)
    rotate(angle*2.5)
    strokeWeight(6)
    line(0,0,40,0)
    angle += speed * angelDirection
    if angle > QUARTER_PI or angle <0:
        angelDirection = -angelDirection
