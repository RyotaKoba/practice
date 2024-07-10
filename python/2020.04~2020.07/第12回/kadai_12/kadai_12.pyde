theta = 0.00
rotx = 0.00
roty = 0.00
r = 255
g = 0
b = 0
s = "S\nK\nY\nT\nR\nE\nE"

def setup():
    size(220,500,P3D)
    
def draw():
    global theta
    textSize(20)
    translate(110,250,0)
    background(0)
    rotateX(-rotx)
    rotateY(-roty)
    fill(255,255,0)
    theta = 0.000
    pushMatrix()
    translate(0,0,0)
    for i in range(3):
        rotateY(radians(theta))
        text(s,-70,-100,0)
        theta += 1
    popMatrix()
    theta = 0.00
    pushMatrix()
    translate(0,250,0)
    for i in range(360):
        rotateY(radians(theta))
        noFill()
        stroke(r,g,b)
        beginShape()
        vertex(0,-68,0)
        vertex(-22,-68,0)
        vertex(-10,-282,0)
        vertex(-13,-289,0)
        vertex(-14,-290,0)
        vertex(-20,-306,0)
        vertex(-18,-306,0)
        vertex(-19,-313,0)
        vertex(-19,-315,0)
        vertex(-19,-313,0)
        vertex(-10,-313,0)
        vertex(-10,-320,0)
        vertex(-9,-320,0)
        vertex(-8,-353,0)
        vertex(-12,-367,0)
        vertex(-9,-367,0)
        vertex(-8,-372,0)
        vertex(-6,-372,0)
        vertex(-6,-392,0)
        vertex(-2,-392,0)
        vertex(-2,-474,0)
        vertex(-4,-478,0)
        vertex(-4,-484,0)
        vertex(0,-484,0)
        vertex(0,-68,0)
        endShape()
        stroke(255)
        beginShape()
        vertex(0,-50,0)
        vertex(-32,-50,0)
        vertex(-32,-68,0)
        vertex(0,-68,0)
        vertex(0,-50,0)
        endShape()
        theta += 1
    popMatrix()
    change()
    
def mouseDragged():
    global rotx,roty
    rate = 0.01
    rotx += (pmouseY-mouseY) * rate
    roty += (pmouseX-mouseX) * rate
    
def change():
    global r,g,b
    #n kisuu only
    n = 3
    if g < 130 and b == 0:
        g += n
    elif g < 255 and b == 0:
        g += n
        r -= n
    elif r > 30 and b == 0:
        r -= n
    elif r > 0 and g == 255:
        r -= n
        b += n
    elif b < 205 and r == 0:
        b += n
    elif b < 255 and r == 0:
        b += n
        g -= n
    elif g > 0 and b == 255 and r == 0:
        g -= n
    elif r < 240 and g == 0:
        r += n
    elif r < 255 and g == 0:
        r += n
        b -= n
    elif b > 0 and g == 0:
        b -= n
