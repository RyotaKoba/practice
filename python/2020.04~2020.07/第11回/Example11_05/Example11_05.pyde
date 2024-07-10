import json

films = []

def setup():
    global films
    size(300,300)
    filmFileHandle = open("films.json")
    films = json.load(filmFileHandle)
    
def draw():
    y = 36
    for i in range(len(films)):
        film = films[i]
        ratingSize= map(film["rating"],6.5,8.1,5,30)
        pushMatrix()
        y += ratingSize
        translate(32,y)
        rotate(-QUARTER_PI/3.0)
        textSize(ratingSize)
        text(film["title"],0,0)
        popMatrix()
