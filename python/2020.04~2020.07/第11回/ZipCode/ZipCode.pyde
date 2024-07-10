zmap = []
input = None
input_number = 0

class Code(object):
    def __init__(self, data):
        self.Prf = data[0]
        self.City = data[1]
        self.zip_code = data[2]
        self.longitude = float(data[4][1:4]) + float(data[4][5:7])/60.0
        self.latitude = float(data[4][14:16]) + float(data[4][17:19])/60.0
        # print self.longitude
        # print self.latitude
        
code = []

min_x = None
max_x = None
min_y = None
max_y = None
query = ['_', '_', '_', '-', '_', '_', '_', '_']
angle = 0.0

def setup():
    global min_x, max_x, min_y, max_y
    size(800, 600)
    background(color(0, 0, 0))
    colorMode(RGB, 255)
    ellipseMode(CENTER)
    
    data = loadStrings("zipcode.txt")
    for i in range(len(data)):
        temp = split(data[i], '\t');
        code.append(Code(temp))
    
    ave_longitude = 0.0
    ave_latitude = 0.0
    max_x = max_y = 0.0
    min_x = min_y = 100000.0

    for i in range(len(data)):
        ave_longitude += code[i].longitude
        ave_latitude += code[i].latitude
        if max_x < code[i].longitude:
            max_x = code[i].longitude
        if min_x > code[i].longitude:
            min_x = code[i].longitude
        if max_y < code[i].latitude:
            max_y = code[i].latitude
        if min_y > code[i].latitude:
            min_y = code[i].latitude
        
    ave_longitude = ave_longitude/len(data)
    ave_latitude = ave_latitude/len(data)

def keyReleased():
    global input_number
    global angle
    print key
    
    if keyCode == LEFT and input_number > 0:
        input_number -= 1
        query[input_number] = '_'
    elif key < '0' or key > '9' or input_number >= 8:
        print("Error")
    else:
        query[input_number] = key
        input_number += 1
    
    if keyCode != LEFT:
        if input_number == 3:
            query[input_number] = '-'
            input_number += 1

def draw():
    global min_x, max_x, min_y, max_y
    # scale(2.0)
    background(20)
    
    for i in range(len(code)):
        x = map(code[i].longitude, min_x, max_x, 0, width)
        y = height - map(code[i].latitude, min_y, max_y, 0, height)
        flag = True
        for j in range(input_number):
            if code[i].zip_code[j] != query[j]:
                flag = False
        if flag and input_number > 0:
            if input_number == 8:
                fill(255, 0, 0)
                noStroke()
                ellipse(x, y, input_number, input_number)
                stroke(255)
                line(x-20, y, x+20, y)
                line(x, y-20, x, y+20)
            else:
                fill(255, 0, 0)
                noStroke()
                ellipse(x+random(-1,1), y+random(-1,1), 2, 2)
        else:
            stroke(255, 100)
            point(x, y)

    fill(255)
    textSize(10)    
    for j in range(8):
        text(query[j], width/2-40+j*10, height/2)
        
        
    
    
