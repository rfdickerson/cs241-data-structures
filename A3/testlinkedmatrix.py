#!/usr/bin/env python2

from linkedmatrix import LinkedMatrix
import unittest


class TestLinkedMatrix(unittest.TestCase):

    def setUp(self):
        self.empty = LinkedMatrix(0, 0, None)
        self.expected = [[row * 6 + col for col in range(5)] for row in range(6)]

        # flatten the expected values from self.expected (stored as nested
        # lists) as one long list
        self.flatExpected = [item for sublist in self.expected for item in sublist]

        self.q = LinkedMatrix(5, 6, row * 6 + col)
        for row in range(6):
            for col in range(5):
                self.q[(col, row)] = row*6 + col

    def testHeadNode(self):
        head = self.q.headnode
        self.assertIsNotNone(head, "headnode: something strange happened. Perhaps your headnode isn't called headnode? Otherwise, check the value.")

    def testZeroMatrix(self):
        q1 = LinkedMatrix(0, 0, None)
        self.assertIsNone(q1.headnode,
            "zero-size matrix: headnode pointed to something. Perhaps it should point to nothing?")

    def testOneColumnMatrix(self):
        ok = False
        try:
            q1 = LinkedMatrix(1, 5, "t")
            ok = True
        except:
            pass
        finally:
            self.assertTrue(ok, "one-column matrix: failed to construct")

    def testOneRowMatrix(self):
        ok = False
        try:
            q1 = LinkedMatrix(5, 1, "t")
            ok = True
        except:
            pass
        finally:
            self.assertTrue(ok, "one-row matrix: failed to construct")

    def testDimensions(self):
        current = self.q.headnode
        cols = rows = 1
        while current.south is not None:
            current = current.south
            rows += 1
        while current.east is not None:
            current = current.east
            cols += 1
        self.assertEquals((cols, rows), self.q.dimensions, "dimensions: incorrect matrix dimensions")

    def testContent(self):
        current = rowHead = self.q.headnode
        xdim, ydim = self.q.dimensions
        columns = list()
        for y in range(ydim):
            row = list()
            for x in range(xdim):
                row.append(self.q[(x, y)])
            columns.append(row)
        self.assertEquals(self.expected, columns,
'''matrix contents: matrix did not contain what was expected.
should have gotten:
{}
but instead got:
{}'''.format(self.expected, columns))

    def testIterCount(self):
        expected = 5 * 6
        i = 0
        for _ in self.q:
            i += 1
        self.assertEquals(expected, i,
            "iteration: expected {} items, got {}".format(expected, i))

    def testIterValues(self):
        actual = [x for x in self.q]
        self.assertEquals(self.flatExpected, actual,
            "iteration: matrix values did not match expected values")

    def testStr(self):
        q1 = LinkedMatrix(1, 1)
        s = str(q1)
        self.assertIsInstance(s, str,
            "str: string/print method did not give a valid string")

    def testGetItem(self):
        actual = list()
        for row in range(6):
            for col in range(5):
                actual.append(self.q[(col, row)])
        self.assertEquals(self.flatExpected, actual,
            "getitem: expected {} but got {}".format(self.flatExpected, actual))

    def testLinkedStructure(self):
        hn = self.q.headnode
        self.assertEquals(hn.south.value, 6, "expected 6 to be connected to 0")
        
    def testSetItem(self):
        q1 = LinkedMatrix(4, 3, "t")
        q1[(3, 2)] = "changed"
        self.assertEquals(q1[(3, 2)], "changed",
            "setitem: could not set a node value")
        
    def testInsertColumn(self):
        q1 = LinkedMatrix(2, 3, "t")
        x1, y1 = q1.dimensions
        q1.insertColumn(0)
        x2, y2 = q1.dimensions
        self.assertEquals(y1, y2, "inserting column: a new row appeared from nowhere!")
        self.assertNotEquals(x1, x2, "inserting column: dimensions didn't change")
        self.assertEquals(x1 + 1, x2, "inserting column: wrong new dimensions")

    def testInsertRow(self):
        q1 = LinkedMatrix(2, 3, "t")
        x1, y1 = q1.dimensions
        q1.insertRow(0)
        x2, y2 = q1.dimensions
        self.assertEquals(x1, x2, "inserting row: a new column appeared from nowhere!")
        self.assertNotEquals(y1, y2, "inserting row: dimensions didn't change")
        self.assertEquals(y1 + 1, y2, "inserting row: wrong new dimensions")
       
    def testRemoveRow(self):
        q1 = LinkedMatrix(2, 3, "t")
        q1[(0, 1)] = "should be removed"
        x1, y1 = q1.dimensions
        q1.removeRow(1)
        x2, y2 = q1.dimensions
        self.assertEquals(x1, x2, "deleting row: a column disappeared!")
        self.assertNotEquals(y1, y2, "deleting row: dimensions didn't change")
        self.assertEquals(y1 - 1, y2, "deleting row: wrong new dimensions")
        self.assertNotEquals(q1[(0, 1)], "should be removed",
            "deleting row: old row still remains")

    def testRemoveColumn(self):
        q1 = LinkedMatrix(3, 4, "t")
        q1[(1, 0)] = "should be removed"
        x1, y1 = q1.dimensions
        q1.removeColumn(1)
        x2, y2 = q1.dimensions
        self.assertEquals(y1, y2, "deleting column: a row disappeared!")
        self.assertNotEquals(x1, x2, "deleting column: dimensions didn't change")
        self.assertEquals(x1 - 1, x2, "deleting column: wrong new dimensions")
        self.assertNotEquals(q1[(1, 0)], "should be removed",
            "deleting column: old column still remains")

    def testInsertAndDeleteColumn2(self):
        q1 = LinkedMatrix(3, 2, "t")
        strBefore = str(q1)
        d = q1.dimensions
        q1.removeColumn(1)
        strDuring = str(q1)
        q1.insertColumn(1)
        strAfter = str(q1)
        self.assertEquals(d, q1.dimensions,
            "inserting & deleting columns: dimensions were not updated")
        self.assertNotEquals(strBefore, strDuring,
            "inserting & deleting columns: nothing changed during delete")
        message = '''inserting & deleting columns: values changed unexpectedly
before we deleted, the test matrix contained:
{}
after we deleted, the test matrix contained:
{}
after we inserted, the test matrix contained:
{}'''
        message = message.format(strBefore, strDuring, strAfter)
        self.assertEquals(strBefore, strAfter, message)
        
    def testInsertAndDeleteColumn1(self):
        q1 = LinkedMatrix(2, 3, "t")
        strBefore = str(q1)
        d = q1.dimensions
        q1.removeColumn(1)
        strDuring = str(q1)
        q1.insertColumn(1)
        strAfter = str(q1)
        self.assertEquals(d, q1.dimensions,
            "inserting & deleting columns: dimensions were not updated")
        self.assertNotEquals(strBefore, strDuring,
            "inserting & deleting columns: nothing changed during delete")
        message = '''inserting & deleting columns: values changed unexpectedly
before we deleted, the test matrix contained:
{}
after we deleted, the test matrix contained:
{}
after we inserted, the test matrix contained:
{}'''
        message = message.format(strBefore, strDuring, strAfter)
        self.assertEquals(strBefore, strAfter, message)
        
    def testInsertAndDeleteRow1(self):
        q1 = LinkedMatrix(3, 2, "t")
        strBefore = str(q1)
        d = q1.dimensions
        q1.removeRow(1)
        strDuring = str(q1)
        q1.insertRow(1)
        strAfter = str(q1)
        self.assertEquals(d, q1.dimensions,
            "inserting & deleting rows: dimensions were not updated")
        self.assertNotEquals(strBefore, strDuring,
            "inserting & deleting rows: nothing changed during delete")
        message = '''inserting & deleting rows: values changed unexpectedly
before we deleted, the test matrix contained:
{}
after we deleted, the test matrix contained:
{}
after we inserted, the test matrix contained:
{}'''
        message = message.format(strBefore, strDuring, strAfter)
        self.assertEquals(strBefore, strAfter, message)
        
    def testInsertAndDeleteRow2(self):
        q1 = LinkedMatrix(2, 3, "t")
        strBefore = str(q1)
        d = q1.dimensions
        q1.removeRow(1)
        strDuring = str(q1)
        q1.insertRow(1)
        strAfter = str(q1)
        self.assertEquals(d, q1.dimensions,
            "inserting & deleting rows: dimensions were not updated")
        self.assertNotEquals(strBefore, strDuring,
            "inserting & deleting rows: nothing changed during delete")
        message = '''inserting & deleting rows: values changed unexpectedly
before we deleted, the test matrix contained:
{}
after we deleted, the test matrix contained:
{}
after we inserted, the test matrix contained:
{}'''
        message = message.format(strBefore, strDuring, strAfter)
        self.assertEquals(strBefore, strAfter, message)
        
if __name__ == "__main__":
    unittest.main()
