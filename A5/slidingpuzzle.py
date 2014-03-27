from collections import deque

class BadMoveException (Exception):
    pass


class PuzzleState (object):
    '''
    Abstracts a sliding puzzle with one gap. Internally stored as a flattened
    list called 'gamestate', with the gap represented as None.

    For details, see: https://github.com/rfdickerson/CS241/tree/master/A5
    '''

    def __init__(self, dimensions, gamestate, parent, lastMove):
        self.dimensions = dimensions
        self.gamestate = gamestate
        self.parent = parent
        self.lastMove = lastMove

    def coordToIndex(self, coord):
        '''Given an (x, y) tuple, return the index in the gamestate list
        corresponding to the tile at (x, y). Coordinates are zero-indexed.'''
        pass

    def indexToCoord(self, index):
        '''Given a tile index into gamestate list, return the (x, y) tuple
        corresponding to that tile. Coordinates are zero-indexed.'''
        pass

    def moveUp(self):
        '''Returns a new instance of PuzzleState where the gap and the value
        above it are flipped.'''
        pass

    def moveDown(self):
        '''Returns a new instance of PuzzleState where the gap and the value
        below it are flipped.'''
        pass

    def moveLeft(self):
        '''Returns a new instance of PuzzleState where the gap and the value
        to its left are flipped.'''
        pass

    def moveRight(self):
        '''Returns a new instance of PuzzleState where the gap and the value
        to its right are flipped.'''
        pass

    def __str__(self):
        '''Returns a string giving a human-readable representation of the
        puzzle's state.'''
        pass

    def __eq__(self, other):
        '''Tests whether two PuzzleState instances have the same gamestates.'''
        pass


class PuzzleSolver (object):
    '''Takes two instances of PuzzleState, an initial and final state, and
    determines the solution and some statistics to the problem.

    For details, see: https://github.com/rfdickerson/CS241/tree/master/A5'''

    def __init__(self, initial, goal):
        assert initial.dimensions == goal.dimensions, "initial and goal dimensions must be the same"
        self.initial = initial
        self.goal = goal

    def solve(self):
        '''Solves the puzzle and returns the PuzzleStates used to get from the
        initial state to the goal state.
        
        Tips! (er, requirements...)
        - Use deque from the collections module to keep track of pending
          states, that is, parents whose children need finding. Use append and
          popleft to push and pop items, respectively.
        - Keep track of states you've already found so you don't move back and
          forth between the same states forever. A Python list is fine here.
        - Keeping track of parents and moves in the constructor of the
          PuzzleState class means you don't need to do any weird additional
          linking stuff to keep track of the solution. It's already done!'''
        pass

    def movesToSolve(self):
        '''Returns a list of strings representing the directions to move the
        blank space in order to solve the puzzle. Depends on the solve method,
        above.'''

        solution = self.solve()

        # [1:] slicing omits the lastMove of the initial state, which is None
        return [ state.lastMove for state in solution[1:] ]


if __name__ == "__main__":
    dimensions = (3, 3)
    parent = lastMove = None
    initial = PuzzleState(dimensions, [2,8,3,1,6,4,7,None,5], parent, lastMove)
    goal = PuzzleState(dimensions, [None,2,3,1,8,6,7,5,4], parent, lastMove)

    solver = PuzzleSolver(initial, goal)
    soln = solver.solve()
