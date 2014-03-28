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


class TestPuzzleSolver(unittest.TestCase):

    def setUp(self):
        pass

    def testArbitraryTestcase(self):
        self.assertEquals(True, True, "message")


if __name__ == "__main__":
    # Load both test suites
    stateTests = unittest.TestLoader().loadTestsFromTestCase(TestPuzzleState)
    solverTests = unittest.TestLoader().loadTestsFromTestCase(TestPuzzleSolver)

    # Run both test suites. Default to running more verbose tests.
    unittest.TextTestRunner(verbosity=2).run(stateTests)
    unittest.TextTestRunner(verbosity=2).run(solverTests)
