When programming in Python , when you write:

a = []

a dynamic array is created and bound to the symbol a. All of the details so how items are appended, the array is resized, are abstracted away from the user. For this assignment, instead of an array, we prefer to keep our items stored in a Linked List.

The Python language does not provide a LinkedList implementation in its standard library. You have been tasked to create a LinkedList class that implements all the necessary methods so that behaves exactly like a Python List, so that for all purposes the user of the class can treat it just like the default Python List. Refer to the following reference material for the methods that need to be overloaded so that your class behaves like a collection. 

Implement the following methods:

__init__(self, pythonlist = None)

creates a new Linked List by taking a Python list as an (optional) argument and making a new node for each.

def append(self, newvalue)

__str__(self)

returns a String representation for the Linked List, groups of items separated by commas in square brackets

__getitem__(self, key)

returns the value at the node positioned at the value of key (i.e. a[8] would return the 9th element in the linked list)

__setitem__(self, key, value)

sets the value at position key a particular value

__len__

returns the size of the linked list as an integer

__contains__(self, value)

scans the list for a node with the value passed in, returns true if the value exists in the linked list

__iter__(self):

return a new generator that returns the values in the LinkedList, throws a StopIteration exception when the end of the linked list is reached.

__getslice__(self, i, j)

returns a new linked list with the subset of nodes in the original linked list from i and j non-inclusive.
Tips:

    Make sure you understand the difference between the linkedlist's value and the node object that stores values. All of the methods abstract away all of the mechanics regarding nodes, and just return the values inside of the nodes.

 
Test Cases:

testlinkedlist.pyView in a new window
