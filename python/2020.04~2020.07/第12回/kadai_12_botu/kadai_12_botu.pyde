flag = False
L = 0
r = 255
g = 255
b = 255
a = 330
d = 30
L = 5
Z = 0

def setup():
    size(410,410)
    translate(50,0)
    background(255)
    fill(0)
    noStroke()
    rect(300,0,60,410)
    fill(204,204,204)
    rect(-50,0,350,60)
    stroke(0)
    strokeWeight(5)
    line(300,0,300,410)
    stroke(255)
    strokeWeight(0.8)
    line(302,0,302,410)
    stroke(255)
    strokeWeight(1)
    fill(255)
    ellipse(330,30,40,40)
    fill(255,0,0)
    ellipse(330,80,40,40)
    fill(0,0,255)
    ellipse(330,130,40,40)
    fill(0,255,0)
    ellipse(330,180,40,40)
    fill(255,255,0)
    ellipse(330,230,40,40)
    fill(255,165,0)
    ellipse(330,280,40,40)
    fill(128,0,128)
    ellipse(330,330,40,40)
    fill(0,255,255)
    ellipse(330,380,40,40)
    fill(0)
    ellipse(30,30,40,40)
    textSize(12)
    fill(255)
    text("RESET",13,35)
    fill(192,192,192)
    strokeWeight(2)
    ellipse(220,30,40,40)
    noStroke()
    ellipse(170,30,40,40)
    ellipse(270,30,40,40)
    stroke(0)
    strokeWeight(10)
    line(160,40,180,20)
    strokeWeight(5)
    line(210,40,230,20)
    strokeWeight(2)
    line(260,40,280,20)
    fill(0)
    noStroke()
    rect(-50,60,348,350)
    fill(255)
    textSize(30)
    text("Please select color",0,230)
    
def draw():
    translate(50,0)
    if flag:
        if mouseX-50 > 295:
            ColorSelect(mouseX-50,mouseY)    
        elif mouseY < 60:
            OptionSelect(mouseX-50,mouseY)
        else:
            stroke(r,g,b)
            strokeWeight(L)
            line(pmouseX-50,pmouseY,mouseX-50,mouseY)
                
def OptionSelect(m,n):
    global L
    RE = dist(m,n,30,30)
    F  = dist(m,n,170,30)
    N  = dist(m,n,220,30)
    T  = dist(m,n,270,30)
    
    if RE < 20:
        fill(0)
        noStroke()
        rect(-50,60,348,350)
        
    if F < 20:
        L = 10
        check2(255,255,255,204,204,204,204,204,204)
    if N < 20:
        L = 6
        check2(204,204,204,255,255,255,204,204,204)
    if T < 20:
        L = 2
        check2(204,204,204,204,204,204,255,255,255)
            
def ColorSelect(x,y):
    global L,r,g,b
    K = dist(x,y,330,30)
    R = dist(x,y,330,80)
    B = dist(x,y,330,130)
    G = dist(x,y,330,180)
    Y = dist(x,y,330,230)
    O = dist(x,y,330,280)
    P = dist(x,y,330,330)
    W = dist(x,y,330,380)
    
    if K < 20:
        r = 255
        g = 255
        b = 255
        check(255,0,0,0,0,0,0,0)
    if R < 20:
        r = 255
        g = 0
        b = 0
        check(0,255,0,0,0,0,0,0)
    if B < 20:
        r = 0
        g = 0
        b = 255
        check(0,0,255,0,0,0,0,0)
    if G < 20:
        r = 0
        g = 255
        b = 0
        check(0,0,0,255,0,0,0,0)
    if Y < 20:
        r = 255
        g = 255
        b = 0
        check(0,0,0,0,255,0,0,0)
    if O < 20:
        r = 255
        g = 165
        b = 0
        check(0,0,0,0,0,255,0,0)
    if P < 20:
        r = 128 
        g = 0
        b = 128
        check(0,0,0,0,0,0,255,0)
    if W < 20:
        r = 0
        g = 255
        b = 255
        check(0,0,0,0,0,0,0,255)
        
def check2(Fr,Fg,Fb,Nr,Ng,Nb,Tr,Tg,Tb):
    strokeWeight(2)
    fill(0,0,0,0)
    stroke(Fr,Fg,Fb)
    ellipse(170,30,40,40)
    stroke(Nr,Ng,Nb)
    ellipse(220,30,40,40)
    stroke(Tr,Tg,Tb)
    ellipse(270,30,40,40)
        
def check(Kc,Rc,Bc,Gc,Yc,Oc,Pc,Wc):
    strokeWeight(2)
    fill(0,0,0,0)
    stroke(Kc)
    ellipse(330,30,47,47)
    stroke(Rc)
    ellipse(330,80,47,47)
    stroke(Bc)
    ellipse(330,130,47,47)
    stroke(Gc)
    ellipse(330,180,47,47)
    stroke(Yc)
    ellipse(330,230,47,47)
    stroke(Oc)
    ellipse(330,280,47,47)
    stroke(Pc)
    ellipse(330,330,47,47)
    stroke(Wc)
    ellipse(330,380,47,47)
    
def mousePressed():
    global Z
    if Z < 1:
        fill(0)
        noStroke()
        rect(0,60,298,350)
        Z += 1
    global flag
    flag = True
    
def mouseReleased():
    global flag
    flag = False
