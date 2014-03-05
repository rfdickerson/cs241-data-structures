#!/usr/bin/env python2

from linkedlist import LinkedList
import unittest


class TestLineSegment(unittest.TestCase):

    def setUp(self):
        self.q = LinkedList()
        self.q.append(5)
        self.q.append(10)
        self.q.append(15)
        self.q.append(20)
        self.q.append(25)

    def testLen(self):
        l = len(self.q)
        self.assertEquals(l, 5,
            "len(): expected length of 5 but got {}".format(l))

    def testPosIndex(self):
        e = self.q[2]
        self.assertEquals(e, 15,
            "positive indexing: expected 15 but got {}".format(e))

    def testZeroIndex(self):
        e = self.q[0]
        self.assertEquals(e, 5,
            "indexing: sliced index 0. expected 5 but got {}".format(e))

    def testAppend(self):
        self.q.append("Bob")
        l = len(self.q)
        last = self.q[5]
        self.assertEquals(l, 6,
            "appending: expected new list length 6 but got {}".format(l))
        self.assertEquals(last, "Bob",
            "appending: expected \"Bob\" element but got {}".format(last))

    def testNegIndex(self):
        e = self.q[-2]
        self.assertEquals(e, 20,
            "negative indexing: expected 20, but got {}".format(e))

    def testHighIndex(self):
        try:
            self.q[99]
            self.assertEquals(True, True,
                "positive indexing: expected IndexError")
        except IndexError as e:
            pass
        except:
            self.assertEquals(True, True,
                "positive indexing: expected IndexError, got {}".format(e))

    def testLowIndex(self):
        try:
            self.q[-100]
            self.assertEquals(True, True,
                "negative indexing: expected IndexError")
        except IndexError as e:
            pass
        except:
            self.assertEquals(True, True,
                "negative indexing: expected IndexError, got {}".format(e))

    def testWeirdIndex(self):
        try:
            self.q["Bob"]
            self.assertEquals(True, True,
                "negative indexing: expected IndexError")
        except IndexError as e:
            pass
        except Exception as e:
            self.assertEquals(True, True,
                "negative indexing: expected IndexError, got {}".format(e))

    def testString(self):
        s = str(self.q).replace(' ', '')
        self.assertEquals(s, "[5,10,15,20,25]",
            "printing/str(): expected [5,10,15,20,25], but got {}".format(s))

    def testConstructByList(self):
        q2 = LinkedList([2, 4, 6, 8, 10, 12])
        l = len(q2)
        self.assertEquals(l, 6,
            "constructing by list: expected length of 6, got {}".format(l))

    def testSlice(self):
        self.assertEquals(self.q[2:4][0], 15,
            "slicing region: expected [15,20], got {}".format(self.q[2:4]))
        self.assertEquals(self.q[2:4][1], 20,
            "slicing region: expected [15,20], got {}".format(self.q[2:4]))

    def testSliceReturnType(self):
        t = type(self.q[2:4])
        isLinkedList = t is LinkedList
        self.assertEquals(isLinkedList, True,
            "slicing region: expected an instance of LinkedList, got {}".format(t))

    def testSetValue(self):
        self.q[1] = "Alfred"
        e = self.q[1]
        self.assertEquals(e, "Alfred",
            "setting: expected \"Alfred\", got {}".format(e))

    def testHas(self):
        self.assertEquals(10 in self.q, True,
            "in operator: expected 10 to be in list")

    def testHas2(self):
        self.assertEquals(66 in self.q, False,
            "in operator: didn't expect 66 to be in list")

    def testIter(self):
        q3 = LinkedList([3, 1, 4, 1, 5, 9, 2, 6, 5])
        i = 0
        for n in q3:
            i += 1
        self.assertEquals(i, 9,
            "iterating: expected 9 iterations, instead iterated {} times".format(i)) 

if __name__ == "__main__":
    unittest.main()
