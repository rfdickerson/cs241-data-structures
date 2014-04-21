from app import app

from flask import Flask, render_template, request, g
import json
import sqlite3
import datetime

from astar.pathfinder import find
from mapbuilder import Map, MapBuilder

DATABASE = 'tmp/database.db'

def get_db():
    """ Gets the handle to the sqlite database """
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    """ closes the connection to the database upon close """
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def save_map(m):
    """ commits the map information into the database """
    db = get_db()
    c = db.cursor()
    query = "INSERT INTO maps VALUES ('{0}',{1},{2},'{3}')".format(json.dumps(m.mapdata), 
            m.width, 
            m.height, 
            datetime.datetime.now())
    c.execute(query)
    db.commit()

def get_map():
    """ gets the most recent map from the database for pathfinding"""
    db = get_db()
    c = db.cursor()
    query = "SELECT * from maps order by date_created desc limit 1"
    for m in c.execute(query):
        pass
    if m is not None:
        mapdata = json.loads(m[0])
        width = m[1]
        height = m[2]
        return Map(width, height, mapdata)
    return None




def processinput(input):
    return int(input)

@app.route("/")
def hello():
    """ Renders the main webpage """
    return render_template("index.html")

@app.route("/newmap")
def map():
    """ a new map is generated upon a GET request, saves map to database """

    mapwidth = request.args.get('mapwidth','')
    mapheight = request.args.get('mapheight','')
    mapwidth = int(mapwidth)
    mapheight = int(mapheight)

    builder = MapBuilder()
    generatedmap = builder.generate(mapwidth, mapheight)
    save_map(generatedmap)

    db = get_db()

    payload = {}
    payload["mapdata"] = generatedmap.mapdata
    payload["width"] = generatedmap.width
    payload["height"] = generatedmap.height
    return json.dumps(payload)

@app.route("/solve")
def solve(): 
    """ gets the start and end coordinates from the request, loads the last
    generated map from the database and calls the pathfinder algorithm. The
    result of a list of coordinates are serialized as JSON and passed to the
    browser for rendering. """
    
    sx = request.args.get('sx','')
    sy = request.args.get('sy','')
    dx = request.args.get('dx','')
    dy = request.args.get('dy','')
    sx = processinput(sx)
    sy = processinput(sy)
    dx = processinput(dx)
    dy = processinput(dy)

    generatedmap = get_map()

    if generatedmap != None:

        path = find(generatedmap.mapdata, 
                generatedmap.width, 
                generatedmap.height, [sx, sy], [dx,dy])
        return json.dumps(path)

    return "[]"



if __name__ == "__main__":
    app.run(debug=True)
