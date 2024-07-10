p = second()
Mo  = month()
Y = 20
D = day()
Dn = False
Yn = False
Mon = False
Hn = False
Min = False
Sn = True
flag = False
n = 0
H = hour()
Mi = minute()
S = second()
s = False
Pr = 204
Pg = 255
Pb = 255

def setup():
    size(800,165)
    background(204,255,255)
    noStroke()
    fill(204,255,255)
    ellipse(540,70,20,20)
    ellipse(540,110,20,20)       
    ellipse(680,70,20,20)        
    ellipse(680,110,20,20)
    stroke(0)
    strokeWeight(5)
    line(0,40,800,40)
    line(130,50,110,130)
    line(270,50,250,130)
    line(400,40,400,140)
    line(0,143,800,143)
    fill(0)
    textSize(13)
    text("SECOND",724,25)
    text("MINUTE",586,25)
    text("HOUR",451,25)
    text("DAY",316,25)
    text("MONTH",166,25)
    text("YEAR",35,25)
    text("24H",390,35)
    text("The selected time is set in motion",300,160)
    fill(0)
    textSize(80)
    noStroke()
    check(204,255,255,204,255,255,204,255,255,204,255,255,204,255,255,0,0,0)
    
def draw():
    global p,s,Y,D,Mo
    n = second()+1
    if p > 1 and n == 1:
        elapse()
        p = 1
    elif n > p:
        elapse()
        p += 1
        if s:
            Point(0,0,0)
            s = False
        else:
            Point(204,255,255)
            s = True
        
    if flag:
        target(mouseX,mouseY)
        update(420)
    text(Y,5,120)
    text(Mo,140,120)
    text(D,280,120)
    text(H,420,120)
    text(Mi,560,120)
    text(S,700,120)
    
def elapse():
    global Y,Mo,D,H,Mi,S
    if Yn:
        Y += 1
        update(0)
    if Dn:
        if Mo == 2:
            if D < 28:
                D += 1
                update(280)
            else:
                Mo += 1
                D = 1
                update(280)
                update(140)
                if Mo > 12:
                    Mo = 1
                    Y += 1
                    update(140)
                    update(0)
        else:
            Dayelapse()
                                
    if Mon:
        if Mo < 12:
            Mo += 1
            update(140)
        else:
            Mo = 1
            Y += 1
            update(140)
            update(0)
    if Hn:
        if H < 23:
            H += 1
            update(420)
        else:
            H = 0
            update(420)
    if Min:
        if Mi < 59:
            Mi += 1
            update(560)
        else:
            Mi = 0
            H +=1
            update(560)
            update(420)
            if H == 24:
                H = 0
                update(420)
                update(560)
    if Sn:
        if S < 59:
            S += 1
            update(700)
        else:
            S = 0
            Mi += 1
            update(560)
            update(700)
            if Mi == 60:
                Mi = 0
                H += 1
                update(560)
                update(420)
                if H == 24:
                    H = 0
                    update(420)
                    update(560)
def Dayelapse():
    global D,Y,Mo
    if Mo == 4 or Mo == 6 or Mo == 9 or Mo == 11:
        if D < 30:
            D += 1
            update(280)
        else:
            Mo += 1
            D = 1
            update(280)
            update(140)
            if Mo > 12:
                Mo = 1
                Y += 1
                update(140)
                update(0)
    else:
        if D < 31:
            D += 1
            update(280)
        else:
            Mo += 1
            D = 1
            update(280)
            update(140)
            if Mo > 12:
                Mo = 1
                Y += 1
                update(140)
                update(0)   
            
def target(x,y):
    global Yn,Dn,Mon,Hn,Min,Sn
    if x < 100:
        Yn = True
        Dn = False
        Mon = False
        Hn = False
        Min = False
        Sn = False
        check(0,0,0,204,255,255,204,255,255,204,255,255,204,255,255,204,255,255)
    if x > 100 and x < 240:
        Yn = False
        Dn = False
        Mon = True
        Hn = False
        Min = False
        Sn = False
        check(204,255,255,0,0,0,204,255,255,204,255,255,204,255,255,204,255,255)
    if x > 280 and x < 380:
        Yn = False
        Dn = True
        Mon = False
        Hn = False
        Min = False
        Sn = False
        check(204,255,255,204,255,255,0,0,0,204,255,255,204,255,255,204,255,255)
    if x > 420 and x < 520:
        Yn = False
        Dn = False
        Mon = False
        Hn = True
        Min = False
        Sn = False
        check(204,255,255,204,255,255,204,255,255,0,0,0,204,255,255,204,255,255)
    if x > 560 and x < 660:
        Yn = False
        Dn = False
        Mon = False
        Hn = False
        Min = True
        Sn = False
        check(204,255,255,204,255,255,204,255,255,204,255,255,0,0,0,204,255,255)
    if x > 700:
        Yn = False
        Dn = False
        Mon = False
        Hn = False
        Min = False
        Sn = True
        check(204,255,255,204,255,255,204,255,255,204,255,255,204,255,255,0,0,0)
        
def update(q):
    fill(204,255,255)
    rect(q,50,105,90)
    fill(0) 
    
def Point(Pr,Pg,Pb):
    noStroke()
    fill(Pr,Pg,Pb)
    ellipse(540,70,20,20)
    ellipse(540,110,20,20)       
    ellipse(680,70,20,20)        
    ellipse(680,110,20,20) 
    fill(0)      

def check(Yr,Yg,Yb,Mor,Mog,Mob,Dr,Dg,Db,Hr,Hg,Hb,Mir,Mig,Mib,Sr,Sg,Sb):
    fill(0,0,0,0)
    strokeWeight(2)
    stroke(Yr,Yg,Yb)
    rect(20,10,60,20)
    stroke(Mor,Mog,Mob)
    rect(160,10,60,20) 
    stroke(Dr,Dg,Db)
    rect(300,10,60,20)  
    stroke(Hr,Hg,Hb)
    rect(440,10,60,20)    
    stroke(Mir,Mig,Mib)  
    rect(580,10,60,20)     
    stroke(Sr,Sg,Sb) 
    rect(720,10,60,20)        
    fill(0)        
    noStroke()
def mousePressed():
    global flag
    flag = True

def mouseReleased():
    global flag
    flag = False
