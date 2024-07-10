numFrame = 11
images = []
currentFrame = 0

def setup():
    size(300,300)
    background(208)
    
    for i in range(numFrame):
        imageName = "frame-" + nf(i,4) + ".png"
        images.append(loadImage(imageName))
    frameRate(24)
    
def draw():
    global currentFrame
    
    image(images[currentFrame],width/2-120,height/2-60)
    
    if mousePressed:
        if mouseButton == LEFT:
            currentFrame += 1
        elif mouseButton == RIGHT:
            currentFrame -= 1
    if currentFrame >= len(images):
        currentFrame = 0
    elif currentFrame <= 0:
        currentFrame = len(images) -1
