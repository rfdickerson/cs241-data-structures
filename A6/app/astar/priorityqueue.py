import math

def parentindex( curindex):
    return (curindex - 1) // 2

def leftchild( i ):
    return i*2 + 1

class PriorityQueue ( object ):
    """ A priority queue implemented by a list heap 
    You can insert any datatype that is comparable into the heap. The lowest
    value element is kept at the root of the tree.  """

    def __init__(self):
        self.a = []


    def insert(self, value):
        """ insert a node into priority queue"""
        # WRITE THIS FUNCTION
        pass
	
	
    def remove(self):
        """ Returns the element at the top of the heap. Moves the bottom
        element to the top of the tree and then reheapifies from the
        top of the heap"""
        # WRITE THIS FUNCTION 
        pass

    def reheapify(self, i): 
        """ checks if the left or right is smaller than the
        top, if so, flips their positions in the heap. Then reheapifies from
        the the position of the largest child. """
        # WRITE THIS FUNCTION
        pass
        

    def __len__(self):
        """ returns the size of the heap """
        return len(self.a)
                

    def __str__(self):
        """ returns the comma seperated values for the heap """
        return ",".join(map(str,self.a))

if __name__ == "__main__": 
    
    """ Use the following code to ensure that the heap will remove the elements
    from lowest to highest values """
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


