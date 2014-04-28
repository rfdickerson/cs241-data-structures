# Sound Processor

from circularbuffer import CircularBuffer


if __name__ == "__main__":

    # load values into filter
    # f = [1,.2,.1,.05,.01]

    f = []
    ff = open('data/filter.txt', 'r')
    for d in ff:
        f.append(float(d))

    print 'Filter is ' + str(f)

    # load the data file
    fd = open('data/signal.txt', 'r')

    input = []
    output = []
    correct = [10.0, 14.0, 17.0, 18.0, 18.1]

    # make a circular buffer of size 5
    c = CircularBuffer(len(f))
    for d in fd:
        input.append(int(d))
        c.push(int(d))

        # convolve the filter with values in the buffer
        y = zip(f, c)
        a = sum( map(lambda x: x[0] * x[1], y))
        output.append( a )


    print "Original signal is:"
    print input
    
    print "Convolved signal is:"
    print output

    print "Should be:"
    print correct
        


    
    





