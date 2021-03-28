# Declare a Shape class that accepts a sides parameter. 

# In the initialization process for an object, assign the sides parameter to a sides attribute on the object.

# Instantiate a Shape object with 3 sides and assign it to a “triangle" variable.

# Instantiate a Shape object with 4 sides and assign it to a “square" variable.

# Instantiate a Shape object with 10 sides and assign it to a “decagon" variable.

class Shape:
    def __init__(self, sides):
        self.sides = sides

triangle = Shape(3)
square = Shape(4)
decagon = Shape(10)
