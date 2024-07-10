def setup():
    size(300,300)
    background(208)
    noStroke()
    fill(0)
    
def draw():
    rect(mouseX,mouseY,6,6)
    
def mousePressed():
    fill(255)
    
def mouseReleased():
    fill(0)
