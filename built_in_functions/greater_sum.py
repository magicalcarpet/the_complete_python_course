# Declare a greater_sum function that accepts two lists of numbers.
# It should return the list with the greatest sum.
# You can assume the lists will always have different sums.
#
# EXAMPLES
# greater_sum([1, 2, 3], [1, 2, 4]) => [1, 2, 4]
# greater_sum([4, 5], [2, 3, 6])    => [2, 3, 6]
# greater_sum([1], [])              => [1]

def greater_sum(array1, array2):
    if sum(array1) > sum(array2):
        return array1
    return array2


print([1, 2, 3], [1, 2, 4])
print([4, 5], [2, 3, 6])
print([1], [])