Assignment 3 
------------------------

# Introduction #

It turns out that you can modify the concept of a linked list, but have nodes
connected by any topology you like.In this assignment, you will be modifying
your linked list to implement a two-dimensional linked-list (or matrix) by
defining a node as having a north, south, east, and west neighbor as well as a
value. The scaffold for your class should look like:


# FAQ #

* Can I change the Node class?

Please do not change the Node class since I will not be able to test to see if
you have built the program correctly.

* What does the default value mean?

When you create a new matrix with a defined dimension, you must specify what
the default value is set to for each Node. Later in the operation of the code,
one can reset the value of the node to be anything he or she wishes.

* Can I use a Python list?

Yes, you can use a Python list, but make sure that you are only temporarily
using it- just for helping you create a new matrix, or to insert new rows or
columns. The actual persistent data for holding the values in the LinkedMatrix
are composed of linked Nodes.

