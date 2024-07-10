img = None

def setup():
    global img
    size(300,300)
    img = loadImage("lunar.jpg")
    
def draw():
    image(img,0,0)
    image(img,150,150,150,150)
