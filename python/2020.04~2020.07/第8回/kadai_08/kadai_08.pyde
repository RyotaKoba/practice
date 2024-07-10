#theme audio visualizer
offset = 175
offset2 = 50
a = False
b = False
c = False
d = False
scalar = 50
scalar2 = 50
angle = 0.0
anglea = 0.0
angleb = 0.0
anglec = 0.0
angled = 0.0
angleapple = 0
flag = True

def setup():
    size(500,700)
    background(0)
    
def draw():
    global angleapple
    if flag:
        background(0)
        apple(color(192,192,192),250,360,2.2,0,0,0)
        stroke(255)
        fill(0)
        ellipse(250,350,200,200)
        apple(color(random(0,255),random(0,255),random(0,255)),250,360,0.4,angleapple,color(255,0,0),color(0,255,0))
        speed(random(0.05,0.15),True,False,False,False)
        speed(random(0.05,0.15),False,True,False,False)
        speed(random(0.05,0.15),False,False,True,False)
        speed(random(0.05,0.15),False,False,False,True)
        speed2()
        wave(0,700,255,255,255,-h1)
        wave(20,700,255,255,255,-h2)
        wave(40,700,255,255,255,-h3)
        wave(60,700,255,255,255,-h4)
        wave(80,700,255,255,255,-h5)
        wave(100,700,255,255,255,-h6)
        wave(120,700,255,255,255,-h7)
        wave(140,700,255,255,255,-h8)
        wave(160,700,255,255,255,-h9)
        wave(180,700,255,255,255,-h10)
        wave(200,700,255,255,255,-h11)
        wave(220,700,255,255,255,-h12)
        wave(240,700,255,255,255,-h13)
        wave(260,700,255,255,255,-h14)
        wave(280,700,255,255,255,-h15)
        wave(300,700,255,255,255,-h16)
        wave(320,700,255,255,255,-h17)
        wave(340,700,255,255,255,-h18)
        wave(360,700,255,255,255,-h19)
        wave(380,700,255,255,255,-h20)
        wave(400,700,255,255,255,-h21)
        wave(420,700,255,255,255,-h22)
        wave(440,700,255,255,255,-h23)
        wave(460,700,255,255,255,-h24)
        wave(480,700,255,255,255,-h25)
        stick(0,color(255,0,2),y1)
        stick(10,color(255,35,0),y2)
        stick(20,color(255,73,0),y3)
        stick(30,color(255,111,0),y4)
        stick(40,color(255,149,0),y5)
        stick(50,color(255,187,0),y6)
        stick(60,color(248,255,0),y7)
        stick(70,color(210,255,0),y8)
        stick(80,color(172,255,0),y9)
        stick(90,color(134,255,0),y10)
        stick(100,color(96,255,0),y11)
        stick(110,color(58,255,0),y12)
        stick(120,color(0,255,17),y13)
        stick(130,color(0,255,55),y14)
        stick(140,color(0,255,93),y15)
        stick(150,color(0,255,131),y16)
        stick(160,color(0,255,169),y17)
        stick(170,color(0,255,207),y18)
        stick(180,color(0,228,255),y19)
        stick(350,color(255,0,20),y20)
        stick(340,color(255,0,40),y21)
        stick(330,color(255,0,116),y22)
        stick(320,color(255,0,154),y23)
        stick(310,color(255,0,192),y24)
        stick(300,color(243,0,255),y25)
        stick(290,color(205,0,255),y26)
        stick(280,color(167,0,255),y27)
        stick(270,color(129,0,255),y28)
        stick(260,color(91,0,255),y29)
        stick(250,color(53,0,255),y30)
        stick(240,color(0,0,255),y31)
        stick(230,color(0,38,255),y32)
        stick(220,color(0,76,255),y33)
        stick(210,color(0,114,255),y34)
        stick(200,color(0,152,255),y35)
        stick(190,color(0,190,255),y36)
        angleapple += 1
    else:
        noStroke()
        fill(255,255,255,50)
        rect(220,320,20,60)
        rect(260,320,20,60)
    
def stick(deg,c,y):
    pushMatrix()
    strokeWeight(11)
    translate(250,350)
    rotate(radians(deg))
    stroke(c)
    line(0,125,0,y)
    strokeWeight(5)
    popMatrix()
    
def wave(x,y,r,g,b,h):
    pushMatrix()
    translate(x,y)
    noStroke()
    fill(r,g,b,200)
    rect(0,0,20,h)
    popMatrix()
    
def speed(sp,a,b,c,d):
    global anglea,angleb,anglec,angled,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20,y21,y22,y23,y24,y25,y26,y27,y28,y29,y30,y31,y32,y33,y34,y35,y36
    if a:
        y1 = offset + sin(anglea) * scalar
        y2 = offset + sin(anglea + 0.1) * scalar
        y3 = offset + sin(anglea + 0.2) * scalar
        y4 = offset + sin(anglea + 0.3) * scalar
        y5 = offset + sin(anglea + 0.4) * scalar
        y6 = offset + sin(anglea + 0.5) * scalar
        y7 = offset + sin(anglea + 0.6) * scalar
        y8 = offset + sin(anglea + 0.7) * scalar
        y9 = offset + sin(anglea + 0.8) * scalar
        anglea += sp
    if b:
        y10 = offset + cos(angleb) * scalar
        y11 = offset + cos(angleb + 0.1) * scalar
        y12 = offset + cos(angleb + 0.2) * scalar
        y13 = offset + cos(angleb + 0.3) * scalar
        y14 = offset + cos(angleb + 0.4) * scalar
        y15 = offset + cos(angleb + 0.5) * scalar
        y16 = offset + cos(angleb + 0.6) * scalar
        y17 = offset + cos(angleb + 0.7) * scalar
        y18 = offset + cos(angleb + 0.8) * scalar
        angleb += sp
    if c:
        y19 = offset + sin(anglec) * scalar
        y36 = offset + sin(anglec + 0.1) * scalar
        y35 = offset + sin(anglec + 0.2) * scalar
        y34 = offset + sin(anglec + 0.3) * scalar
        y33 = offset + sin(anglec + 0.4) * scalar
        y32 = offset + sin(anglec + 0.5) * scalar
        y31 = offset + sin(anglec + 0.6) * scalar
        y30 = offset + sin(anglec + 0.7) * scalar
        y29 = offset + sin(anglec + 0.8) * scalar
        anglec += sp
    if d:
        y28 = offset + cos(angled) * scalar
        y27 = offset + cos(angled + 0.1) * scalar
        y26 = offset + cos(angled + 0.2) * scalar
        y25 = offset + cos(angled + 0.3) * scalar
        y24 = offset + cos(angled + 0.4) * scalar
        y23 = offset + cos(angled + 0.5) * scalar
        y22 = offset + cos(angled + 0.6) * scalar
        y21 = offset + cos(angled + 0.7) * scalar
        y20 = offset + cos(angled + 0.8) * scalar
        angled += sp
    
def speed2():
    global angle,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14,h15,h16,h17,h18,h19,h20,h21,h22,h23,h24,h25
    h1 = offset2 + sin(angle) * scalar2
    h2 = offset2 + sin(angle+random(0.01,0.5)) * scalar2
    h3 = offset2 + sin(angle+random(0.01,0.5)) * scalar2
    h4 = offset2 + sin(angle+random(0.01,0.5)) * scalar2
    h5 = offset2 + sin(angle+random(0.01,0.5)) * scalar2
    h6 = offset2 + sin(angle+random(0.01,0.5)) * scalar2
    h7 = offset2 + sin(angle+random(0.01,0.5)) * scalar2
    h8 = offset2 + sin(angle+random(0.01,0.5)) * scalar2
    h9 = offset2 + sin(angle+random(0.01,0.5)) * scalar2
    h10 = offset2 + sin(angle+random(0.01,0.5)) * scalar2
    h11 = offset2 + sin(angle+random(0.01,0.5)) * scalar2
    h12 = offset2 + sin(angle+random(0.01,0.5)) * scalar2
    h13 = offset2 + sin(angle+random(0.01,0.5)) * scalar2
    h14 = offset2 + sin(angle+random(0.01,0.5)) * scalar2
    h15 = offset2 + sin(angle+random(0.01,0.5)) * scalar2
    h16 = offset2 + sin(angle+random(0.01,0.5)) * scalar2
    h17 = offset2 + sin(angle+random(0.01,0.5)) * scalar2
    h18 = offset2 + sin(angle+random(0.01,0.5)) * scalar2
    h19 = offset2 + sin(angle+random(0.01,0.5)) * scalar2
    h20 = offset2 + sin(angle+random(0.01,0.5)) * scalar2
    h21 = offset2 + sin(angle+random(0.01,0.5)) * scalar2
    h22 = offset2 + sin(angle+random(0.01,0.5)) * scalar2
    h23 = offset2 + sin(angle+random(0.01,0.5)) * scalar2
    h24 = offset2 + sin(angle+random(0.01,0.5)) * scalar2
    h25 = offset2 + sin(angle+random(0.01,0.5)) * scalar2
    angle += 0.08
    
def apple(c,x,y,s,z,v1,v2):
    pushMatrix()
    translate(x,y)
    rotate(radians(z))
    fill(v1)
    stroke(c)
    strokeWeight(4)
    beginShape()
    curveVertex(0*s,118*s)
    curveVertex(0*s,118*s)
    curveVertex(-10*s,120*s)
    curveVertex(-20*s,124*s)
    curveVertex(-30*s,128*s)
    curveVertex(-40*s,132*s)
    curveVertex(-50*s,134*s)
    curveVertex(-60*s,131*s)
    curveVertex(-70*s,124*s)
    curveVertex(-80*s,116*s)
    curveVertex(-90*s,106*s)
    curveVertex(-95*s,100*s)
    curveVertex(-100*s,94*s)
    curveVertex(-102*s,90*s)
    curveVertex(-104*s,86*s)
    curveVertex(-107*s,80*s)
    curveVertex(-110*s,74*s)
    curveVertex(-114*s,66*s)
    curveVertex(-116*s,60*s)
    curveVertex(-120*s,50*s)
    curveVertex(-124*s,40*s)
    curveVertex(-127*s,30*s)
    curveVertex(-130*s,18*s)
    curveVertex(-131*s,10*s)
    curveVertex(-132*s,0*s)
    curveVertex(-133*s,-10*s)
    curveVertex(-134*s,-20*s)
    curveVertex(-133*s,-30*s)
    curveVertex(-132*s,-40*s)
    curveVertex(-129*s,-50*s)
    curveVertex(-124*s,-60*s)
    curveVertex(-120*s,-68*s)
    curveVertex(-110*s,-80*s)
    curveVertex(-100*s,-90*s)
    curveVertex(-90*s,-98*s)
    curveVertex(-80*s,-104*s)
    curveVertex(-60*s,-106*s)
    curveVertex(-40*s,-105*s)
    curveVertex(-20*s,-98*s)
    curveVertex(-10*s,-95*s)
    curveVertex(-4*s,-95*s)
    curveVertex(0,-95*s)
    curveVertex(20*s,-103*s)
    curveVertex(40*s,-108*s)
    curveVertex(60*s,-109*s)
    curveVertex(80*s,-104*s)
    curveVertex(100*s,-94*s)
    curveVertex(116*s,-78*s)
    curveVertex(107*s,-70*s)
    curveVertex(100*s,-64*s)
    curveVertex(90*s,-50*s)
    curveVertex(86*s,-40*s)
    curveVertex(83*s,-30*s)
    curveVertex(82*s,-20*s)
    curveVertex(85*s,0*s)
    curveVertex(90*s,12*s)
    curveVertex(100*s,29*s)
    curveVertex(110*s,40*s)
    curveVertex(124*s,49*s)
    curveVertex(120*s,62*s)
    curveVertex(110*s,82*s)
    curveVertex(100*s,97*s)
    curveVertex(80*s,120*s)
    curveVertex(70*s,130*s)
    curveVertex(60*s,133*s)
    curveVertex(40*s,129*s)
    curveVertex(20*s,120*s)
    curveVertex(0,118*s)
    curveVertex(0,118*s)
    endShape()
    fill(v2)
    beginShape()
    curveVertex(-7*s,-111*s)
    curveVertex(-7*s,-111*s)
    curveVertex(-7*s,-120*s)
    curveVertex(-5*s,-130*s)
    curveVertex(0*s,-142*s)
    curveVertex(10*s,-156*s)
    curveVertex(20*s,-166*s)
    curveVertex(30*s,-175*s)
    curveVertex(40*s,-183*s)
    curveVertex(50*s,-188*s)
    curveVertex(58*s,-188*s)
    curveVertex(60*s,-180*s)
    curveVertex(59*s,-170*s)
    curveVertex(56*s,-160*s)
    curveVertex(52*s,-152*s)
    curveVertex(46*s,-140*s)
    curveVertex(38*s,-130*s)
    curveVertex(26*s,-120*s)
    curveVertex(12*s,-112*s)
    curveVertex(0,-110*s)
    curveVertex(-7*s,-111*s)
    curveVertex(-7*s,-111*s)
    endShape()
    popMatrix()
    
def mousePressed():
    global flag
    if flag:
        flag = False
    else:
        flag = True
