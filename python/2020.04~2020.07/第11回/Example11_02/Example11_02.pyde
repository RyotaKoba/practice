planetList = [{"name":"Mercury","radius":2439.64,"au":0.3871,"period":88.0},
              {"name":"Venus","radius":6051.59,"au":0.7233,"period":224.7},
              {"name":"Earth","radius":6387.1,"au":1.0000,"period":365.25},
              {"name":"Mars","radius":3397.0,"au":1.5237,"period":687.0},
              {"name":"jupiter","radius":69911.0,"au":5.2026,"period":4328.9}
              ]

def setup():
    size(300,300)
    textAlign(LEFT, CENTER)
    
def draw():
    background(0)
    fill(0)
    translate(width/2,height/2)
    planetCount = len(planetList)
    d = dist(width/2,height/2,mouseX,mouseY)
    dm = dist(width/2,height/2,width,height)
    scalar = map(d,0,dm,0.4,2.0)
    scale(scalar)
    stroke(1.0/scalar)
    textSize(1.0/scalar*12)
    for i in range(planetCount):
        pushMatrix()
        planetRadius = planetList[i]['radius']*0.001
        stroke(255,255,255,100)
        noFill()
        ellipse(0,0,planetList[i]['au']*50*2,planetList[i]['au']*50*2)
        rotate(frameCount%planetList[i]['period']/planetList[i]['period']*TWO_PI)
        translate(planetList[i]['au']*50,0)
        fill(255)
        ellipse(0,0,planetRadius,planetRadius)
        fill(200)
        text(planetList[i]['name'],planetRadius,0)
        popMatrix()
