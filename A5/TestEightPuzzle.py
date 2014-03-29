#!/usr/bin/env python2

from slidingpuzzle import BadMoveException, PuzzleState, PuzzleSolver
import unittest

class TestPuzzleState(unittest.TestCase):
    '''
    Performs logical tests on PuzzleState
    '''

    def setUp(self):
        self.eightPuzzle = PuzzleState(
                dimensions=(3, 3),
                gamestate=[1, 2, 3, 4, 5, 6, 7, 8, None],
                parent=None,
                lastMove=None)
        self.fifteenPuzzle = PuzzleState(
                dimensions=(4, 4),
                gamestate=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None],
                parent=None,
                lastMove=None)

    def testDimensionsInput(self):
        expected = (3, 3)
        observed = self.eightPuzzle.dimensions
        m = "Dimensions weren't what we passed in. Make sure self.dimensions is a tuple of ints.\n\nObserved: {}\nExpected: {}"
        self.assertEquals(observed, expected, m.format(observed, expected))

    def testItemCount(self):
        x, y = self.eightPuzzle.dimensions
        observedList = self.eightPuzzle.gamestate
        observedCount = len(observedList)
        observedDimensions = self.eightPuzzle.dimensions
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
        expectedIndex = 6
        observedIndex = self.eightPuzzle.coordToIndex(coord)
        message = m.format(coord, observedIndex, expectedIndex)
        self.assertEquals(observedIndex, expectedIndex, message)

        coord = (0, 0)
        expectedIndex = 0
        observedIndex = self.eightPuzzle.coordToIndex(coord)
        message = m.format(coord, observedIndex, expectedIndex)
        self.assertEquals(observedIndex, expectedIndex, message)

        coord = (1, 2)
        expectedIndex = 7
        observedIndex = self.eightPuzzle.coordToIndex(coord)
        message = m.format(coord, observedIndex, expectedIndex)
        self.assertEquals(observedIndex, expectedIndex, message)

        coord = (2, 2)
        expectedIndex = 8
        observedIndex = self.eightPuzzle.coordToIndex(coord)
        message = m.format(coord, observedIndex, expectedIndex)
        self.assertEquals(observedIndex, expectedIndex, message)

        coord = (2, 0)
        expectedIndex = 2
        observedIndex = self.eightPuzzle.coordToIndex(coord)
        message = m.format(coord, observedIndex, expectedIndex)
        self.assertEquals(observedIndex, expectedIndex, message)

    def testIndexToCoord(self):
        m = '''Wrong coordinate given from index. Check indexToCoord() method.

Index given: {}
Observed coordinate: {}
Expected coordinate: {}'''
        index = 3
        expectedCoord = (0, 1)
        observedCoord = self.eightPuzzle.indexToCoord(index)
        message = m.format(index, observedCoord, expectedCoord)
        self.assertEquals(observedCoord, expectedCoord, message)

        index = 1
        expectedCoord = (1, 0)
        observedCoord = self.eightPuzzle.indexToCoord(index)
        message = m.format(index, observedCoord, expectedCoord)
        self.assertEquals(observedCoord, expectedCoord, message)

        index = 0
        expectedCoord = (0, 0)
        observedCoord = self.eightPuzzle.indexToCoord(index)
        message = m.format(index, observedCoord, expectedCoord)
        self.assertEquals(observedCoord, expectedCoord, message)

        index = 8
        expectedCoord = (2, 2)
        observedCoord = self.eightPuzzle.indexToCoord(index)
        message = m.format(index, observedCoord, expectedCoord)
        self.assertEquals(observedCoord, expectedCoord, message)

        index = 2
        expectedCoord = (2, 0)
        observedCoord = self.eightPuzzle.indexToCoord(index)
        message = m.format(index, observedCoord, expectedCoord)
        self.assertEquals(observedCoord, expectedCoord, message)

    def testEquals(self):
        m = "PuzzleState did not equal itself! Check your __eq__ method.\n"
        self.assertEquals(self.eightPuzzle, self.eightPuzzle, m)

    def testStr(self):
        m = "Something went wrong when printing PuzzleState! Check your __str__ method.\n\nPrint call output: {}"
        observedVisual = str(self.eightPuzzle)
        self.assertIsInstance(observedVisual, str, m.format(observedVisual))

    def testMoveFunctions(self):
        controlState = PuzzleState(
                dimensions=(3, 3),
                gamestate=[1, 2, 3, 4, None, 5, 6, 7, 8],
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
                dimensions=(3, 3),
                gamestate=[1, None, 3, 4, 2, 5, 6, 7, 8],
                parent=None,
                lastMove=None)
        observedUpState = controlState.moveUp()
        message = m.format("Up", controlState, observedUpState, upState)
        self.assertEquals(upState, observedUpState, message)

        downState = PuzzleState(
                dimensions=(3, 3),
                gamestate=[1, 2, 3, 4, 7, 5, 6, None, 8],
                parent=None,
                lastMove=None)
        observedDownState = controlState.moveDown()
        message = m.format("Down", controlState, observedDownState, downState)
        self.assertEquals(downState, observedDownState, message)

        leftState = PuzzleState(
                dimensions=(3, 3),
                gamestate=[1, 2, 3, None, 4, 5, 6, 7, 8],
                parent=None,
                lastMove=None)
        observedLeftState = controlState.moveLeft()
        message = m.format("Left", controlState, observedLeftState, leftState)
        self.assertEquals(leftState, observedLeftState, message)

        rightState = PuzzleState(
                dimensions=(3, 3),
                gamestate=[1, 2, 3, 4, 5, None, 6, 7, 8],
                parent=None,
                lastMove=None)
        observedRightState = controlState.moveRight()
        message = m.format("Right", controlState, observedRightState, rightState)
        self.assertEquals(rightState, observedRightState, message)


class TestPuzzleSolver(unittest.TestCase):

    def setUp(self):
        self.eightInitial = PuzzleState((3, 3), [2,8,3,1,6,4,7,None,5], None, None)
        self.eightGoal = PuzzleState((3, 3), [None,2,3,1,8,6,7,5,4], None, None)
        self.eightSolver = PuzzleSolver(self.eightInitial, self.eightGoal)

    def testSolve(self):
        expectedElements = [
                [2, 8, 3, 1, 6, 4, 7, None, 5],
                [2, 8, 3, 1, 6, 4, 7, 5, None],
                [2, 8, 3, 1, 6, None, 7, 5, 4],
                [2, 8, 3, 1, None, 6, 7, 5, 4],
                [2, None, 3, 1, 8, 6, 7, 5, 4],
                [None, 2, 3, 1, 8, 6, 7, 5, 4]]
        observedStates = self.eightSolver.solve()
        observedElements = [ x.gamestate for x in observedStates ]

        m_solution = '''PuzzleSolver ultimately arrives at the wrong solution! Check your solve() method.

Input:
{}

Observed last element of solution chain
{}

Expected last element of solution chain:
{}'''
        m_full = '''PuzzleSolver gives the wrong solution chain! Check your solve() method.

Input:
{}

Observed solution chain:
{}

Expected solution chain:
{}'''
        expectedPrintable = '\n'.join([ str(x) for x in expectedElements ])
        observedPrintable = '\n'.join([ str(x) for x in observedElements ])

        message = m_solution.format(self.eightInitial, observedPrintable, expectedPrintable)
        self.assertEquals(observedElements[-1], expectedElements[-1], message)

        message = m_full.format(self.eightInitial, observedPrintable, expectedPrintable)
        self.assertEquals(observedElements, expectedElements, message)

    def testMovesToSolve(self):
        m = '''PuzzleSolver gave the wrong moves, or I didn't recognise them as English directions. Hint: I'll take north/south/east/west or up/down/left/right.

Observed moves list: {}'''
        expectedDirections = (
                ['right', 'up', 'left', 'up', 'left'],
                ['east', 'north', 'west', 'north', 'west'])
        observedDirections = [ x.lower() for x in self.eightSolver.movesToSolve() ]
        message = m.format(observedDirections)
        self.assertIn(observedDirections, expectedDirections, message)


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
