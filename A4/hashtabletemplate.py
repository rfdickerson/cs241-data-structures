from collections import Hashable

class Node (object):

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.nextNode = None

class LinkedList (object):
    # insert your assignment 2 here


class Hashtable (object):

    def __init__(self, hashFunction, size=500):
        """ Initialize a blank hashtable

        hashFunction - a function that contains 2 arguments, key and size of hash
            and returns an index to a bucket
        size - the number of buckets in your hash
        """

        pass
        

    def __setitem__(self, key, value):
        """ Sets the value at the key to value

        key - any immutable object
        value - any object

        if key is mutable, raise a TypeError
        """

        pass
        

    def __getitem__(self, key):
        """ Returns the value at the key 
        key - immutable key value

        if there is no value at key, raise AttributeError
        """

        pass


    def getBucketSizes(self):
        """ yield the sizes of each bucket as an iterator"""

        pass

    def __len__(self):
        """ Returns the total number of items in the hash"""

        pass


    def __contains__(self, key):
        """ Returns True is the hash has a key """

        pass


def hashFunction(key, numbuckets):

    pass


if __name__ == "__main__":
    h = Hashtable(hashFunction, 1000)
    h["cat"] = "a feline"
    h["memphis"] = "a city"
   
    print h["cat"]
    print h['memphis']
    print 'Does h contain {}, {}'.format('cat', 'cat' in h)
    print 'Does h contain {}, {}'.format('piano', 'piano' in h)
    print 'h has a size {}'.format(len(h))

