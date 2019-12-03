import math

"""
* Create a class called `Point` which has two instance variables,
`x` and `y` that represent the `x` and `y` co-ordinates respectively. 

* Initialize these instance variables in the `__init__` method

* Define a method, `distance` on `Point` which accepts another `Point` object as an argument and 
returns the distance between the two points.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, coordinate):
        x_diff = coordinate.x - self.x
        y_diff = coordinate.y - self.y
        return math.sqrt(x_diff**2 + y_diff**2)
