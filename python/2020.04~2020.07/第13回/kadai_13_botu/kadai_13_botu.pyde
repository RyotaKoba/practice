class chara():
    def __init__(self,x,y,a):
        self.xpos = x
        self.ypos = y
        self.afterImage = a
       # self.Color = c
        
    def display(self):
        for i in range(100):
            background(0)
            cube(self.xpos,self.ypos,self.afterImage-i*2)

a = chara(230,230,200)        
                        
def setup():
    size(500,500)
    
def draw():
    global 
    CUBE = []
    if flag:
        CUBE.append(
    
def cube(x,y,e):
    pushMatrix()
    translate(x,y)
    stroke(255,255,255,e)
    strokeWeight(10)aa
    noFill()
    rect(0,0,80,80)
    popMatrix()
    
#def keyPressed():
    
