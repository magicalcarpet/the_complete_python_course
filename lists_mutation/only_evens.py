# Define an only_evens function that accepts a list of numbers. 
# It should return a new list consisting of only the even numbers 
# from the original list.
#
# EXAMPLES
# only_evens([4, 8, 15, 16, 23, 42]) => [4, 8, 16, 42]
# only_evens([1, 3, 5])              => []
# only_evens([])                     => []

def only_evens(array):
    new_list = []
    for item in array:
        if item % 2 == 0:
            new_list.append(item)
    return new_list


print(only_evens([4, 8, 15, 16, 23, 42]))
print(only_evens([1, 3, 5]))
print(only_evens([]))