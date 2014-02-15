class Node (object):
    
    def __init__(self, value):
        self.value = value
        self.north = None
        self.south = None
        self.east = None
        self.west = None

class LinkedMatrix (object) :

    def __init__(self, x, y, defaultValue=None):
        """ creates a new matrix with x columns and y rows with default value default value """
        self.headnode = None
        self.defaultValue = defaultValue

    def __str__(self):
        """ return the string representation of the matrix """
        pass

    def __getitem__(self, index):
        """ return the element at the index expressed as a tuple """
        pass

    def __setitem__(self, index, a):
        """ set value at index to a """
        pass

    def __iter__(self):
        """returns a list of all the items in the matrix first across down then across repeat"""
        pass

    def insertRow(self, rowIndex, defaultValue=self.defaultValue):
        """inserts a row at the given index, shifting columns if necessary"""
        pass

    def insertColumn(self, colIndex, defaultValue=self.defaultValue):
        """inserts a column at the given index, shifting columns if necessary"""
        pass

    def removeRow(self, rowIndex):
        """removes a row at the given index, shifting columns if necessary"""
        pass

    def removeColumn(self, colIndex):
        """removes a column at the given index, shifting columns if necessary"""
        pass
