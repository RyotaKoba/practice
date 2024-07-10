def setup():
    size(300,300)
    stroke(255)
    for i in range(6):
        for e range(5):
            x = 50 + 50*e
            y = 50 + 50*i
            
def logo(x,y,s,c):
    pushMatrix()
    translate(x,y)
    stroke(c)
    strokeWeight(4*s)
    fill(255,255,255)
    ellipse(0*s,0*s,300*s,300*s)
    strokeWeight(2*s)
    ellipse(0*s,0*s,240*s,240*s)
    noStroke()
    fill(c)
    ellipse(0*s,0*s,230*s,230*s)
    # logo
    fill(255,255,255)
    rect(-38*s,70*s,76*s,15*s)
    rect(-10*s,85*s,20*s,5*s)
    rect(-45*s,25*s,90*s,15*s)
    rect(-60*s,-35*s,20*s,125*s)
    rect(40*s,-35*s,20*s,125*s)
    rect(20*s,-35*s,25*s,15*s)
    rect(20*s,-15*s,25*s,15*s)
    rect(20*s,5*s,25*s,15*s)
    rect(-45*s,-35*s,25*s,15*s)
    rect(-45*s,-15*s,25*s,15*s)
    rect(-45*s,5*s,25*s,15*s)
    rect(25*s,-60*s,35*s,15*s)
    rect(-60*s,-60*s,35*s,15*s)
    rect(-10*s,-105*s,20*s,10*s)
    rect(-60*s,-95*s,120*s,17*s)
    quad(-18*s,-80*s,0*s,-80*s,-11*s,-45*s,-30*s,-45*s)
    quad(0*s,-80*s,18*s,-80*s,30*s,-45*s,11*s,-45*s)
    quad(-18*s,-35*s,-5*s,-35*s,18*s,20*s,5*s,20*s)
    quad(5*s,-35*s,18*s,-35*s,-5*s,20*s,-18*s,20*s)
    triangle(-38*s,45*s,38*s,45*s,0*s,83*s)
    fill(c)
    triangle(-13*s,55*s,13*s,55*s,0*s,70*s)
    popMatrix()
    
