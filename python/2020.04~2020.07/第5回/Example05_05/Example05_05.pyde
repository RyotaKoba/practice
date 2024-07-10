def setup():
    size(300,300)
    textSize(50)
    
def draw():
    if keyPressed:
        fill(random(255),random(255),random(255))
        x = random(width)-10
        y = random(height)+10
        text(key,x,y)
