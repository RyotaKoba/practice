add_library('sound')

class Pad(object):
    def __init__ (self,hz):
        self.sine = SinOsc(this)
        self.sine.freq(hz)
        self.flag = []
        for i in range(8):
            self.flag.append(False)
            
    def display(self,h):
        for i in range(8):
            if(self.flag[i]):
                fill(255)
            else:
                fill(100)
            rect(i*SIZE,7*SIZE-h*SIZE,SIZE,SIZE)
            
    def soundplay(self,num):
        if self.flag[num]:
            self.sine.play()
        else:
            self.sine.stop()
    def setting(self,num):
        if self.flag[num]:
            self.flag[num] = False
        else:
            self.flag[num] = True

tone = [261.62,293.66,329.62,349.22,391.99,440.00,493.88,523.25]
pads = []
SIZE = 0
no = 0

def mousePressed():
    pads[(SIZE*8-mouseY)/SIZE].setting(mouseX/SIZE)
    
def setup():
    global SIZE
    size(320,320)
    SIZE = width/8
    for i in range(8):
        pads.append(Pad(tone[i]))
        
def draw():
    global no
    for i in range(len(tone)):
        pads[i].display(i)
        
    if millis()> no*500:
        for i in range(8):
            pads[i].soundplay(no%8)
        no+=1
    fill(255,255,255,100)
    rect(((no-1)%8)*SIZE,0,SIZE,height)
