class Point():
    def __init__(self,x,y,s):
        self.xpos = x
        self.ypos = y
        self.xspeed = s
    
    def display(self):
        rect(self.xpos, self.ypos,20,20)
    
    def move(self):
        self.xpos += self.xspeed
        if self.xpos > width:
            self.xpos = 0
            
pointA = Point(0,150,1)
pointB = Point(150,200,2)

def setup():
    size(300,300)
    
def draw():
    background(200)
    pointA.display()
    pointA.move()
    pointB.display()
    pointB.move()
