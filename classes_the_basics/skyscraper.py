# Declare a Skyscraper class that accepts name and year parameters. 

# In the initialization process for an object, assign the name parameter to a name attribute 
# and the year parameter to a year attribute.

# Instantiate a Skyscraper object with the name “Empire State Building”  and the year 1931. 
# Assign it to a “empire" variable.

# Instantiate a Skyscraper object with the name “One World Trade Center” and the year 2014. 
# Assign it to a “wtc" variable.

class Skyscraper:
    def __init__(self, name, year):
        self.name = name
        self.year = year

empire = Skyscraper("Empire State Building", 1931)
wtc = Skyscraper("One World Trade Center", 2014)

