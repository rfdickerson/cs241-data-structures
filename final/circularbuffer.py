class CircularBuffer (object):

    def __init__(self, size):
        # data is an array of zeros
        self.data = [0] * size
        # s is the index of the beginning of the buffer
        self.s = 0
        # num is the number of elements stored in the buffer
        self.num = 0
        
    def push (self, value):
        # pushes the value to the end of the circular buffer
        pass

    def pop (self):
        # returns the value at the beginning of the buffer
        pass

    def __len__(self):
        return self.num

    def __iter__(self):
        # yields values from the start to the end of the buffer
        pass



if __name__ == "__main__":
    c = CircularBuffer(4)
    c.push(5)
    c.push(6)
    c.push(7)
    c.push(8)
    c.push(9)
    print c.data
    l = [x for x in c]
    print l
    print c.pop()
    print c.pop()
    print c.pop()
    print c.pop()
    print c.pop()
