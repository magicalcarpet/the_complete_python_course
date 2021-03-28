# Declare a destroy_elements function that accepts two lists.
# It should return a list of all elements from the first list that are 
# NOT contained in the second list.
# Use list comprehension in your solution.
#
# EXAMPLES
# destroy_elements([1, 2, 3], [1, 2])      => [3]
# destroy_elements([1, 2, 3], [1, 2, 3])   => []
# destroy_elements([1, 2, 3], [4, 5])      => [1, 2, 3]

def destroy_elements(array1, array2):
    return [element for element in array1 if element not in array2]
    
    
print(destroy_elements([1, 2, 3], [1, 2]))
print(destroy_elements([1, 2, 3], [1, 2, 3]))
print(destroy_elements([1, 2, 3], [4, 5]))

