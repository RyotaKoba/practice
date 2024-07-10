def setup():
    size(300,300)
    
def draw():
    background(208)
    translate(width/2,height/2)
    strokeWeight(3)
    rotate(-HALF_PI)
    for angle in range(0,360,6):
        pushMatrix()
        rotate(radians(angle))
        translate(100,0)
        if angle/6 == second():
            stroke(255,0,0)
        elif angle/6 == minute():
            stroke(0,255,0)
        elif angle/30.0 == hour()%12:
            stroke(0,0,255)
        else:
            stroke(100)
        line(0,0,10,0)
        popMatrix()
