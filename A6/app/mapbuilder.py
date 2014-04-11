import random

class Map (object):
    """ Holds information about the geography"""

    def __init__(self, width, height, mapdata):
        self.width = width
        self.height = height
        self.mapdata = mapdata

    def __str__(self):
        toret = ""
        for i in range(0, self.height * self.width):
            if self.mapdata[i] == 0:
                toret += '.'
            else:
                toret += '#'
            if i % self.width == self.width-1:
                toret += "\n"
        return toret


class MapBuilder (object):
    """ Cellar Automata Method for Generating Random Maps """

    def __init__(self):
        pass

    def generate(self, 
            width=60, height=40, 
            simsteps=2, wallPercent=45, 
            deathlimit=2, birthlimit=2):

        self.width = width
        self.height = height
        mapdata = self.randomFillMap(width, height, wallPercent)
        for s in range(0, simsteps):
            mapdata = self.doSimulationStep(mapdata, width, height, deathlimit, birthlimit)
        return Map(width, height, mapdata)

    def ctoi(self, col, row, width, height):
        return row*width + col

    def isOutOfBounds(self, x, y, width, height):
        if x < 0 or y < 0:
            return True
        elif x > (width - 1) or y > (height - 1):
            return True
        return False

    def doSimulationStep(self, oldmap, width, height, deathlimit, birthlimit):
        newmap = list(oldmap)
        for y in range(0, height-1):
            for x in range(0, width-1):
                nbs = self.getAdjacentWalls(oldmap, x, y, width, height, 1, 1)
                if oldmap[self.ctoi(x,y, width, height)] == 1:
                    if nbs < deathlimit:
                        newmap[self.ctoi(x,y, width, height)] = 0
                    else:
                        newmap[self.ctoi(x,y, width, height)] = 1
                else:
                    if nbs > birthlimit:
                        newmap[self.ctoi(x,y, width, height)] = 1
                    else:
                        newmap[self.ctoi(x,y, width, height)] = 0
        return newmap
    
    
    def randomFillMap(self, width, height, wallPercent):
        mapdata = [None]*width*height
        mapMiddle = 0
        for row in range(0, height):
            for col in range(0, width):
                if col == 0:
                    mapdata[self.ctoi(col,row,width,height)] = 1
                elif row == 0:
                    mapdata[self.ctoi(col,row,width,height)] = 1
                elif col == width-1:
                    mapdata[self.ctoi(col,row,width,height)] = 1
                elif row == height-1:
                    mapdata[self.ctoi(col,row,width,height)] = 1
                else:
                    mapMiddle = height // 2
                    if row == mapMiddle:
                        mapdata[self.ctoi(col, row,width,height)] = 0
                    else:
                        mapdata[self.ctoi(col, row, width, height)] = self.randPercent(wallPercent)
        return mapdata

    def randPercent(self, percent):
        if percent >= random.randint(1,101):
            return 1
        else:
            return 0
    
    def placeWallLogic(self, mapdata, x, y):
        numWalls = self.getAdjacentWalls(x,y,1,1)
        if self.mapdata[self.ctoi(x,y)] == 1:
            if numWalls >= 4:
                return 1
            if numWalls < 2:
                return 0
        else:
            if numWalls >= 5:
                return 1
        return 0

    def isWall(self, mapdata, x, y, width, height):
        if self.isOutOfBounds(x,y, width, height):
            return True
        if mapdata[self.ctoi(x,y, width, height)] == 1:
            return True
        if mapdata[self.ctoi(x,y, width, height)] == 0:
            return False
        return False

    def getAdjacentWalls(self, mapdata, x, y, width, height, scopeX, scopeY):
        startX = x - scopeX
        startY = y - scopeY
        endX = x + scopeX
        endY = y + scopeY
        wallCounter = 0
        for iY in range(startY, endY):
            for iX in range(startX, endX):
                if not (iX==x and iY==y):
                    if self.isWall(mapdata, iX, iY, width, height):
                        wallCounter += 1
        return wallCounter

   
if __name__ == "__main__":
    width = 50
    height = 30
    c = MapBuilder()
    newmap = c.generateCaverns(width,height, 2, 55, 2, 2)
    print str(newmap)




                


        

    
