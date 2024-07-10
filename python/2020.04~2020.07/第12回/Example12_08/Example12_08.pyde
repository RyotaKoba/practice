rotx=-PI/18.0
txt_size = 22

class Text3D(object):
    def __init__(self):
        self.txt = []
        self.vertical = []
        self.speed = []
        
    def loadSong(self,filename):
        msg = loadStrings(filename)
        sentence = join(msg,' ')
        splited = split(sentence,' ')
        for i in range(len(splited)):
            self.txt.append(splited[i])
            self.vertical.append(random(0,TWO_PI))
            self.speed.append(random(0.001,0.04))
            
    def display(self,word):
        textSize(txt_size)
        for i in range(len(self.txt)):
            pushMatrix()
            self.vertical[i] -= self.speed[i]
            rotateY(self.vertical[i])
            translate(0,0,200.0)
            translate(-1.0*10*len(self.txt[i])/2.0,0,0)
            if self.txt[i] == word:
                fill(255,0,0,150)
            else:
                fill(200,150)
            text(self.txt[i],0,0,0)
            popMatrix()
            
song = Text3D()
    
    
def setup():
    size(500,500,P3D)
    frameRate(24)
    song.loadSong("message.txt")
        
def draw():
    background(0)
    translate(width/2,height/2)
    rotateX(rotx)
    song.display("love")
        
def mouseDragged():
    global rotx
    rate = 0.01
    rotx += (pmouseY-mouseY) * rate
