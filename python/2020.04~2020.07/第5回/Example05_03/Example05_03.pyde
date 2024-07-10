flag = False

def setup():
    size(300,300)
    background(208)
    strokeWeight(4)
    
def draw():
    if flag:
        stroke(random(128,255),0,0)
        line(pmouseX,pmouseY,mouseX,mouseY)
    
def mousePressed():
    global flag
    flag = True
    
def mouseReleased():
    global flag
    flag = False
