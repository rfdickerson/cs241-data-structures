# Line Segment


***Deliverables: point.py and linesegment.py.***

## Introduction

A line segment is a straight line bounded by two endpoints defined in the two-dimensional Cartesian coordinate system. The operations that can be performed on a line segment are defined below:

 
```python
LineSegment(pointA, pointB)

"""Creates a new line segment defined by the two Point objects."""

 

endPointA()

""" Returns the first endpoint of the line segment."""

 

endPointB()

""" Returns the second endpoint of the line segment."""

 

length()

""" Returns the length of the line segment given as the Euclidean distance between the two endpoints."""

 

isVertical()

""" Returns a boolean indicating if the line segment is parallel to the y-axis."""

 

isHorizontal()

""" Returns a boolean indicating if the line segment is parallel to the x-axis."""

 

isParallel(otherLine)

""" Returns a boolean indicating if the line segment is parallel to the otherLine line segment."""

 

isPerpendicular(otherLine)

""" Returns a boolean indicating if the line segment is perpendicular to the otherLine line segment."""

 

slope()

""" Returns the slope of the line segment given as the rise over the run. If the segment is vertical, return False."""

 

midpoint()

""" Returns the midpoint of the line segment as a Point object."""

 

__str__()

""" Returns a string representation of the line segment in the format (Ax, Ay)#(Bx, By)."""
```
 
## Implementation Tips 

In your Point class, overload the method __eq__ and define behavior so that the 2 points are compared in that their x and y components are equivalent. The default equals behavior would check if the 2 variables are pointing to the same instance in memory.
Implementation

 

The class containing your implementation of the Line Segment ADT should be placed within a module named linesegment.py and named LineSegment.

 

You will need to use the Point class described in the lectures and in the book’s Appendix D.1 and name the file point.py and name the class inside of the file Point.

 

The linesegment.py module should only contain the implementation of the class definition. It should not contain any other statements or global variables outside of the class.

 
## Testing 

Download the UnitTest for the assignment.

testlinesegment.pyView in a new window

Place testlinesegment in the same directory as point.py and linesegment.py

Run the unit tests by running the following command when in the directory:  

python testlinesegment.py
