# Declare a Musical class that accepts a name parameter. 
# In the initialization process for an object, assign the
# name parameter to a name attribute on the object.
#
# Instantiate a Musical object with the name “Rent” 
# and assign it to an “rent" variable.
#
# Instantiate a second Musical object with the name “Book of Mormon" 
# and assign it to a “mormon” variable.
#
# Instantiate a third object from the class with the name “Chicago" 
# and assign it to a “chicago” variable.

class Musical:
    def __init__(self, name):
        self.name = name


rent = Musical("Rent")
mormon = Musical("Book of Mormon")
chicago = Musical("Chicago")

