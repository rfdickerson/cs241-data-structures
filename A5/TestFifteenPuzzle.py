#!/usr/bin/env python2

from slidingpuzzle import BadMoveException, PuzzleState, PuzzleSolver
import unittest

class TestPuzzleState(unittest.TestCase):
    '''
    Performs logical tests on PuzzleState
    '''

    def setUp(self):
        self.fifteenPuzzle = PuzzleState(
                dimensions=(4, 4),
                gamestate=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None],
                parent=None,
                lastMove=None)

    def testDimensionsInput(self):
        expected = (4, 4)
        observed = self.fifteenPuzzle.dimensions
        m = "Dimensions weren't what we passed in. Make sure self.dimensions is a tuple of ints.\n\nObserved: {}\nExpected: {}"
        self.assertEquals(observed, expected, m.format(observed, expected))

    def testItemCount(self):
        x, y = self.fifteenPuzzle.dimensions
        observedList = self.fifteenPuzzle.gamestate
        observedCount = len(observedList)
        observedDimensions = self.fifteenPuzzle.dimensions
        expectedCount = x * y
        m = '''Too many or too few elements in gamestate for current dimensions.

Observed gamestate: {} ({} elements)
Dimensions: {}'''
        message = m.format(observedList, observedCount, observedDimensions)
        self.assertEquals(observedCount, expectedCount, message)

    def testCoordToIndex(self):
        m = '''Wrong index given from coordinate. Check coordToIndex() method.

Coordinates given: {}
Observed index: {}
Expected index: {}'''

        coord = (0, 2)
        expectedIndex = 8
        observedIndex = self.fifteenPuzzle.coordToIndex(coord)
        message = m.format(coord, observedIndex, expectedIndex)
        self.assertEquals(observedIndex, expectedIndex, message)

        coord = (0, 0)
        expectedIndex = 0
        observedIndex = self.fifteenPuzzle.coordToIndex(coord)
        message = m.format(coord, observedIndex, expectedIndex)
        self.assertEquals(observedIndex, expectedIndex, message)

        coord = (1, 2)
        expectedIndex = 9
        observedIndex = self.fifteenPuzzle.coordToIndex(coord)
        message = m.format(coord, observedIndex, expectedIndex)
        self.assertEquals(observedIndex, expectedIndex, message)

        coord = (2, 2)
        expectedIndex = 10
        observedIndex = self.fifteenPuzzle.coordToIndex(coord)
        message = m.format(coord, observedIndex, expectedIndex)
        self.assertEquals(observedIndex, expectedIndex, message)

        coord = (3, 3)
        expectedIndex = 15
        observedIndex = self.fifteenPuzzle.coordToIndex(coord)
        message = m.format(coord, observedIndex, expectedIndex)
        self.assertEquals(observedIndex, expectedIndex, message)

        coord = (3, 2)
        expectedIndex = 11
        observedIndex = self.fifteenPuzzle.coordToIndex(coord)
        message = m.format(coord, observedIndex, expectedIndex)
        self.assertEquals(observedIndex, expectedIndex, message)

        coord = (2, 0)
        expectedIndex = 2
        observedIndex = self.fifteenPuzzle.coordToIndex(coord)
        message = m.format(coord, observedIndex, expectedIndex)
        self.assertEquals(observedIndex, expectedIndex, message)

    def testIndexToCoord(self):
        m = '''Wrong coordinate given from index. Check indexToCoord() method.

Index given: {}
Observed coordinate: {}
Expected coordinate: {}'''
        index = 3
        expectedCoord = (3, 0)
        observedCoord = self.fifteenPuzzle.indexToCoord(index)
        message = m.format(index, observedCoord, expectedCoord)
        self.assertEquals(observedCoord, expectedCoord, message)

        index = 1
        expectedCoord = (1, 0)
        observedCoord = self.fifteenPuzzle.indexToCoord(index)
        message = m.format(index, observedCoord, expectedCoord)
        self.assertEquals(observedCoord, expectedCoord, message)

        index = 0
        expectedCoord = (0, 0)
        observedCoord = self.fifteenPuzzle.indexToCoord(index)
        message = m.format(index, observedCoord, expectedCoord)
        self.assertEquals(observedCoord, expectedCoord, message)

        index = 8
        expectedCoord = (0, 2)
        observedCoord = self.fifteenPuzzle.indexToCoord(index)
        message = m.format(index, observedCoord, expectedCoord)
        self.assertEquals(observedCoord, expectedCoord, message)

        index = 2
        expectedCoord = (2, 0)
        observedCoord = self.fifteenPuzzle.indexToCoord(index)
        message = m.format(index, observedCoord, expectedCoord)
        self.assertEquals(observedCoord, expectedCoord, message)

        index = 15
        expectedCoord = (3, 3)
        observedCoord = self.fifteenPuzzle.indexToCoord(index)
        message = m.format(index, observedCoord, expectedCoord)
        self.assertEquals(observedCoord, expectedCoord, message)

    def testEquals(self):
        m = "PuzzleState did not equal itself! Check your __eq__ method.\n"
        self.assertEquals(self.fifteenPuzzle, self.fifteenPuzzle, m)

    def testStr(self):
        m = '''Something went wrong when printing PuzzleState! Check your __str__ method.\n\nPrint call output:
{}'''
        observedVisual = str(self.fifteenPuzzle)
        self.assertIsInstance(observedVisual, str, m.format(observedVisual))

    def testMoveFunctions(self):
        controlState = PuzzleState(
                dimensions=(4, 4),
                gamestate=[1, 2, 3, 4, 5, 6, None, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                parent=None,
                lastMove=None)
        m = '''Move {0} returned an incorrect PuzzleState (or None). Check your move{0} method.

Input:
{1}

Observed:
{2}

Expected:
{3}'''

        upState = PuzzleState(
                dimensions=(4, 4),
                gamestate=[1, 2, None, 4, 5, 6, 3, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                parent=None,
                lastMove=None)
        observedUpState = controlState.moveUp()
        message = m.format("Up", controlState, observedUpState, upState)
        self.assertEquals(upState, observedUpState, message)

        downState = PuzzleState(
                dimensions=(4, 4),
                gamestate=[1, 2, 3, 4, 5, 6, 10, 7, 8, 9, None, 11, 12, 13, 14, 15],
                parent=None,
                lastMove=None)
        observedDownState = controlState.moveDown()
        message = m.format("Down", controlState, observedDownState, downState)
        self.assertEquals(downState, observedDownState, message)

        leftState = PuzzleState(
                dimensions=(4, 4),
                gamestate=[1, 2, 3, 4, 5, None, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                parent=None,
                lastMove=None)
        observedLeftState = controlState.moveLeft()
        message = m.format("Left", controlState, observedLeftState, leftState)
        self.assertEquals(leftState, observedLeftState, message)

        rightState = PuzzleState(
                dimensions=(4, 4),
                gamestate=[1, 2, 3, 4, 5, 6, 7, None, 8, 9, 10, 11, 12, 13, 14, 15],
                parent=None,
                lastMove=None)
        observedRightState = controlState.moveRight()
        message = m.format("Right", controlState, observedRightState, rightState)
        self.assertEquals(rightState, observedRightState, message)


class TestPuzzleSolver(unittest.TestCase):

    def setUp(self):

        initialGamestate = [
            1, 2, 3, 4,
            5, None, 6, 8,
            9, 10, 7, 12,
            13, 14, 11, 15]

        goalGamestate = [
            1, 2, 3, 4,
            5, 6, 7, 8,
            9, 10, 11, 12,
            13, 14, 15, None]

        self.fifteenInitial = PuzzleState((4, 4), initialGamestate, None, None)
        self.fifteenGoal = PuzzleState((4, 4), goalGamestate, None, None)
        self.fifteenSolver = PuzzleSolver(self.fifteenInitial, self.fifteenGoal)
        self.redundantSolver = PuzzleSolver(self.fifteenInitial, self.fifteenInitial)
        self.cardinal = {
            "north": "up",
            "south": "down",
            "west": "left",
            "east": "right",
        }

    def testSolve(self):
        expectedElements = (self.fifteenInitial.gamestate, self.fifteenGoal.gamestate)
        observedStates = self.fifteenSolver.solve()
        observedElements = [ x.gamestate for x in observedStates ]

        m_solution = '''PuzzleSolver ultimately arrives at the wrong solution! Check your solve() method.

Input:
{}

Observed last element of solution chain
{}

Expected last element of solution chain:
{}'''
        expectedPrintable = '\n'.join([ str(x) for x in expectedElements ])
        observedPrintable = '\n'.join([ str(x) for x in observedElements ])

        message = m_solution.format(self.fifteenInitial, observedPrintable, expectedPrintable)
        self.assertEquals(observedElements[-1], expectedElements[-1], message)

    def testMovesToSolve(self):
        m = '''I couldn't recognise the moves PuzzleSolver returns in movesToSolve() as English directions. Hint: these tests take north/south/east/west or up/down/left/right and don't care about capitalization.

Observed moves list:
{}'''
        rawMoves = self.fifteenSolver.movesToSolve()

        # default to x.lower() if x.lower() isn't in self.cardinal.keys()
        try:
            observedDirections = [ self.cardinal[x.lower()] for x in rawMoves ]
        except KeyError:
            observedDirections = [ x.lower() for x in rawMoves ]

        message = m.format(rawMoves)
        goodDirections = all([x in ['left', 'right', 'up', 'down'] for x in observedDirections])
        self.assertTrue(goodDirections, message)

    def testDoMovesWork(self):
        m = '''Following PuzzleSolver's reported moves doesn't actually solve the puzzle! Check your movesToSolve() and solve() methods.

Input:
{}

Reported moves from movesToSolve():
{}

After following the moves above, we got:
{}

The actual solution:
{}'''
        rawMoves = self.fifteenSolver.movesToSolve()

        # default to x.lower() if x.lower() isn't in self.cardinal.keys()
        moves = [ self.cardinal.get(x.lower(), x.lower()) for x in rawMoves ]

        initialVisual = str(self.fifteenInitial)
        for move in moves:

            # table-driven testing is hip now, just ask Nigel Tao (or ken)
            # https://code.google.com/p/go-wiki/wiki/TableDrivenTests
            moveFunctions = {
                "up": self.fifteenInitial.moveUp,
                "down": self.fifteenInitial.moveDown,
                "left": self.fifteenInitial.moveLeft,
                "right": self.fifteenInitial.moveRight,
            }

            # execute the tabled function
            self.fifteenInitial = moveFunctions[move]()

        message = m.format(initialVisual, rawMoves, self.fifteenInitial, self.fifteenGoal)
        self.assertEquals(self.fifteenInitial, self.fifteenGoal, message)

    def testAlreadySolvedMoves(self):
        m = '''PuzzleSolver did something unexpected when the initial and goal PuzzleStates are the same.

These tests expect an empty list of moves or None to be returned from movesToSolve() in this case.

Observed moves list:
{}'''

        expectedMoves = ([], None)
        observedMoves = self.redundantSolver.movesToSolve()
        message = m.format(observedMoves)
        self.assertIn(observedMoves, expectedMoves, message)

    def testAlreadySolvedSolve(self):
        m = '''PuzzleSolver did something unexpected when the initial and goal PuzzleStates are the same.

These tests expect solve() to return a list containing only one item: the initial/goal state.

Observed solution:
{}'''
        expectedSoln = [ self.fifteenInitial ]
        observedSoln = self.redundantSolver.solve()
        message = m.format("\n".join([ str(x) for x in observedSoln ]))
        self.assertEquals(observedSoln, expectedSoln, message)


if __name__ == "__main__":
    import sys

    # Load both test suites
    stateTests = unittest.TestLoader().loadTestsFromTestCase(TestPuzzleState)
    solverTests = unittest.TestLoader().loadTestsFromTestCase(TestPuzzleSolver)

    # Run both test suites. Default to running more verbose tests.
    print "\n\n", '~' * 5, "TestPuzzleState", '~' * 5
    unittest.TextTestRunner(verbosity=2, stream=sys.stdout).run(stateTests)
    print "\n\n", '~' * 5, "TestPuzzleSolver", '~' * 5
    unittest.TextTestRunner(verbosity=2, stream=sys.stdout).run(solverTests)
