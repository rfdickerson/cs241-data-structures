from collections import deque

class BadMoveException (Exception):
    pass

class PuzzleState (object):

    def __init__(self, gamestate, parent):
        self.gamestate = gamestate
        self.parent = parent

    def coordtoindex(self, coord):
        pass

    def indextocoord(self, index):
        pass

    def moveUp(self):
        pass

    def moveDown(self):
        pass

    def moveRight(self):
        pass

    def moveLeft(self):
        pass

    def __str__(self):
        pass

    def __eq__(self, other):
        pass

class EightPuzzleSolver (object):

    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def solve(self):
        pass

if __name__ == "__main__":
    initial = PuzzleState([2,8,3,1,6,4,7,None,5], None)
    goal = PuzzleState([None,2,3,1,8,6,7,5,4], None)

    solver = EightPuzzleSolver(initial, goal)
    solver.solve()

