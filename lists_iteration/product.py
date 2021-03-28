# Define a product function that accepts a list of numbers.
# The function should return the product of the numbers.
# The list will always have at least one value
#
# EXAMPLES
# product([1, 2, 3])     => 6
# product([4, 5, 6, 7])  => 840
# product([10])          => 10

def product(lists):
    total = 1
    for list in lists:
        total *= list
    return total
    
print(product([1, 2, 3]))
print(product([4, 5, 6, 7]))
print(product([10]))