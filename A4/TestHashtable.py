#!/usr/bin/env python2

from hashtable import Hashtable, hashFunction
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
        self.doubles = { n : n + n for n in range(193) }
        self.testingFunction = lambda k, n: sum(map(ord, str(k))) % n

    def testSmallGetSetWithoutFunction(self):
        q = Hashtable(self.testingFunction, 3)
        for key, value in self.buildings.iteritems():
            q[key] = value
        for key, expected in self.buildings.iteritems():
            observed = q[key]
            self.assertEquals(observed, expected, "small hashtable without your hash function: value changed after being added!\nkey:{}\nexpected value:{}\nobserved value:{}".format(key, value, q[key]))

    def testLargeGetSetWithoutFunction(self):
        q = Hashtable(self.testingFunction, 800)
        for key, value in self.doubles.iteritems():
            q[key] = value
        for key, expected in self.doubles.iteritems():
            observed = q[key]
            self.assertEquals(observed, expected, "large hashtable without your hash function: value changed after being added!\nkey:{}\nexpected value:{}\nobserved value:{}".format(key, value, q[key]))

    def testSmallGetSetWithFunction(self):
        q = Hashtable(hashFunction, 3)
        for key, value in self.buildings.iteritems():
            q[key] = value
        for key, expected in self.buildings.iteritems():
            observed = q[key]
            self.assertEquals(observed, expected, "small hashtable with your hash function: value changed after being added! check __getitem__/__setitem__\nkey:{}\nexpected value:{}\nobserved value:{}".format(key, value, q[key]))

    def testLargeGetSetWithFunction(self):
        q = Hashtable(hashFunction, 800)
        for key, value in self.doubles.iteritems():
            q[key] = value
        for key, expected in self.doubles.iteritems():
            observed = q[key]
            self.assertEquals(observed, expected, "large hashtable with your hash function: value changed after being added! check __getitem__/__setitem__\nkey:{}\nexpected value:{}\nobserved value:{}".format(key, value, q[key]))

    def testSmallContains(self):
        q = Hashtable(hashFunction, 3)
        for key, value in self.buildings.iteritems():
            q[key] = value
        for key in self.buildings:
            self.assertIn(key, q, "membership in small hashtable: `in` keyword didn't work! check __contains__.\nkey:{}".format(key))

    def testLargeContains(self):
        q = Hashtable(hashFunction, 800)
        for key, value in self.doubles.iteritems():
            q[key] = value
        for key in self.doubles:
            self.assertIn(key, q, "membership in large hashtable: `in` keyword didn't work! check __contains__.\nkey:{}".format(key))

    def testSmallLen(self):
        q = Hashtable(hashFunction, 3)
        for key, value in self.buildings.iteritems():
            q[key] = value
        l = len(q)
        self.assertIsInstance(l, type(len(self.buildings)), "length of small hashtable: incorrect type!")
        self.assertLessEqual(l, len(self.buildings), "length of small hashtable: {} items is too many! expected {}; check __len__.".format(l, len(self.buildings)))
        self.assertGreaterEqual(l, len(self.buildings), "length of small hashtable: {} items is not enough! expected {}; check __len__.".format(l, len(self.buildings)))

    def testLargeLen(self):
        q = Hashtable(hashFunction, 800)
        for key, value in self.doubles.iteritems():
            q[key] = value
        l = len(q)
        self.assertIsInstance(l, type(len(self.doubles)), "length of large hashtable: incorrect type!")
        self.assertLessEqual(l, len(self.doubles), "length of large hashtable: {} items is too many! expected {}; check __len__.".format(l, len(self.doubles)))
        self.assertGreaterEqual(l, len(self.doubles), "length of large hashtable: {} items is not enough! expected {}; check __len__.".format(l, len(self.doubles)))

if __name__ == "__main__":
    # Default to running more verbose tests.
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHashtable)
    unittest.TextTestRunner(verbosity=2).run(suite)
