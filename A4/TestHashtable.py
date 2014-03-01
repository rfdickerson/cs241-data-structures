#!/usr/bin/env python2

from hashtable import Hashtable, LinkedList, hashFunction
import unittest
import collections


class TestHashtable(unittest.TestCase):

    def setUp(self):
        self.buildings = {
            "CSCI" : "McGlothlin-Street",
            "GSWS" : "Tucker",
            "ENGL" : "Tucker",
            "LING" : "Tyler",
            "GERM" : "Washington",
        }

    def testWithoutFunction(self):
        testingFunction = lambda key, numBuckets: sum(map(ord, key)) % numBuckets
        q = Hashtable(testingFunction, 1000)
        for key, value in self.buildings.iteritems():
            q[key] = value
        for key, expected in self.buildings.iteritems():
            observed = q[key]
            self.assertEquals(observed, expected, "small hashtable without your hash function: value changed after being added!\nkey:{}\nexpected value:{}\nobserved value:{}".format(key, value, q[key]))

    def testWithFunction(self):
        q = Hashtable(hashFunction, 1000)
        for key, value in self.buildings.iteritems():
            q[key] = value
        for key, expected in self.buildings.iteritems():
            observed = q[key]
            self.assertEquals(observed, expected, "small hashtable with your hash function: value changed after being added! check __getitem__/__setitem__\nkey:{}\nexpected value:{}\nobserved value:{}".format(key, value, q[key]))

    def testContains(self):
        q = Hashtable(hashFunction, 1000)
        for key, value in self.buildings.iteritems():
            q[key] = value
        for key in self.buildings:
            self.assertIn(key, q, "membership in small hashtable: `in` keyword didn't work! check __contains__.\nkey:{}".format(key))

    def testLen(self):
        q = Hashtable(hashFunction, 1000)
        for key, value in self.buildings.iteritems():
            q[key] = value
        l = len(q)
        self.assertIsInstance(l, type(len(self.buildings)), "length: incorrect type!")
        self.assertLessEqual(l, len(self.buildings), "length: {} items is too many! expected {}; check __len__.".format(l, len(self.buildings)))
        self.assertGreaterEqual(l, len(self.buildings), "length: {} items is not enough! expected {}; check __len__.".format(l, len(self.buildings)))

if __name__ == "__main__":
    unittest.main()
