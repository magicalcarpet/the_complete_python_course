# Declare a same_index_values function that accepts two lists.
# The function should return a list of the index positions in 
# which the two lists have equal elements
#
# EXAMPLES
# same_index_values([1, 2, 3], [3, 2, 1])                         => [1]
# same_index_values(["a", "b", "c", "d"], ["c", "b", "a", "d"])   => [1, 3]

def same_index_values(array1, array2):
    position = []
    for index, value in enumerate(array1):
        if value == array2[index]:
            position.append(index)

    return position


print(same_index_values([1, 2, 3], [3, 2, 1]))

print(same_index_values(["a", "b", "c", "d"], ["c", "b", "a", "d"]))