import math
from priorityqueue import PriorityQueue


# You can set the cost of moving these directions in the following constants
LAT_COST = 10
DIAG_COST = 14

class MapTile (object):
    """ Holds information about a tile on the map.
    g is the cost of travelling from the start to that node. Allows diagonal moves.
    h is manhattan distance from that node to the end.  terrain is the type of
    terrain, 0 is passable, 1 is a water (you can extend this)
    parent is the node that precedes the node- used for backtracking
    """

    def __init__(self, coords, g, h, terrain, parent):
        self.coords = coords
        self.g = g
        self.h = h
        self.terrain = terrain
        self.parent = parent

    def f(self):
        return self.g + self.h

    def __lt__(self, other):
        return self.f() < other.f()

    def locatedAt(self, coords):
        return self.coords[0] == coords[0] and self.coords[1] == coords[1]


def mandistance(start, end):
    """ manhatten distance from start to end """
    return abs(start[0]-end[0]) + abs(start[1]-end[1])

def terraintype(mapdata, width, height, coords):
    return mapdata[coords[0] + coords[1]*width] 

def north ( cur ):
    return [cur[0], cur[1] - 1]

def south ( cur ):
    return [cur[0], cur[1] + 1]

def east ( cur ):
    return [cur[0] + 1, cur[1]]

def west ( cur ):
    return [cur[0] - 1, cur[1]]

def northwest ( cur ):
    return [cur[0] - 1, cur[1] - 1]

# WRITE OTHER DIAGONAL CARDINALITIES HERE

def onMap( cur, width, height):
    """ checks if you are out of bounds on the map """
    if cur[0] >= 0 and cur[0] < width and cur[1] >= 0 and cur[1] < height:
        return True
    else:
        return False

def find(mapdata, width, height, start, end):
    """ mapdata is a one-dimensional list of values, start and end are vectors of size 2 """
    # WRITE THIS FUNCTION 
    pass
    



