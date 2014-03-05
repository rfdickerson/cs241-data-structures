from linesegment import LineSegment
from point import Point
import unittest

class TestLineSegment(unittest.TestCase):

    def setUp(self):
        self.s = LineSegment(Point(0,3), Point(2,3))

    def testString(self):
        self.assertEquals(str(self.s), "(0, 3)#(2, 3)", 'incorrect string formatting')

    def testEndPointA(self):
        self.assertEquals(self.s.endPointA(), Point(0,3))

    def testEndPointB(self):
        self.assertEquals(self.s.endPointB(), Point(2,3))

    def testLength(self):
        self.assertEquals(self.s.length(), 2.0)

    def testIsVertical(self):
        self.assertEquals(self.s.isVertical(), False, "line is not vertical")

    def testIsHorizontal(self):
        self.assertEquals(self.s.isHorizontal(), True, "line is horizontal")
    
    def testParallel(self):
        b = LineSegment(Point(3, 5), Point(5,5))
        self.assertEquals(self.s.isParallel(b), True)



if __name__ == "__main__":
    unittest.main()
        
