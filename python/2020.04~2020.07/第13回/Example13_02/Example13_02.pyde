add_library('sound')

sine = None
freq = 40

def setup():
    global sine
    size(440,440)
    sine = SinOsc(this)
    sine.play()
    
def draw():
    background(176,204,176)
    hertz = map(mouseX,0,width,20.0,440.0)
    sine.freq(hertz)
    stroke(26,76,102)
    for x in range(width):
        angle = map(x,0,width,0,TWO_PI * hertz)
        sinValue = sin(angle) * 120
        line(x,0,x,height/2 + sinValue)
