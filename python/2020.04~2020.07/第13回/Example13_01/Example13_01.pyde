add_library('sound')

blip = None
radius = 40
x = 0
speed = 1.0
direction = 1

def setup():
    global blip,x
    size(300,300)
    ellipseMode(RADIUS)
    blip = SoundFile(this,"blip.wav")
    x = width/2
    
def draw():
    global x,direction
    background(208)
    noStroke()
    x += speed * direction
    if x > width-radius or x < radius:
        direction = -direction
        blip.play()
    if direction == 1:
        arc(x,height/2,radius,radius,0.52,5.76)
    else:
        arc(x,height/2,radius,radius,3.67,8.9)
