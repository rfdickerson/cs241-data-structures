import math

def parentindex( curindex):
    return (curindex - 1) // 2

def leftchild( i ):
    return i*2 + 1

class PriorityQueue ( object ):
    """ A priority queue implemented by a list heap"""

    def __init__(self):
        self.a = []


    def insert(self, value):
        # insert initial node into priority queue
	
	
    def remove(self):
        """ Returns the top element, places the bottom element to the top of
        the tree and the tree of then reheapify from the top"""
        # WRITE THIS FUNCTION 
        pass

    def reheapify(self, i):
        """ checks if the left or right is smaller than the top, and flips the position """
        # WRITE THIS FUNCTION
        pass
        

    def __len__(self):
        """ returns the left of the heap """
        return len(self.a)
                

    def __str__(self):
        """ returns the comma seperated values for the heap """
        return ",".join(map(str,self.a))

if __name__ == "__main__":
    p = PriorityQueue()
    p.insert(30)
    p.insert(10)
    p.insert(80)
    p.insert(60)
    p.insert(20)
    p.insert(30)
    while len(p):
        # print p
        print p.remove()


