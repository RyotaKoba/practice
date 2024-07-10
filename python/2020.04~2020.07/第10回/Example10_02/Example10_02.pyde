x = []

def setup():
    size(300,300)
    noStroke()
    fill(100,200)
    for i in range(3000):
        x.append(random(-10000, 200))
    
def draw():
    global x1,x2,x3,x4,x5
    background(208)
    
    for i in range(len(x)):
        x[i] += 0.5
        y = i*0.4
        arc(x[i], y, 40, 40, 0.52, 5.76)
