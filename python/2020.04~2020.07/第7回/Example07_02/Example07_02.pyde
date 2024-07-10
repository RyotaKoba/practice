img = None

def setup():
    global img
    size(300,300)
    img = loadImage("lunar.jpg")
    image(img,0,0,300,300)
    textSize(12)
    
def draw():
    for y in range(300):
        for x in range(300):
           fill(get(x,y))
           text('A',x,y+10)
