values = [1, 2, 3, 4, 5]

def multiply_element_one_less_than_index(arrays):
    total = 0
    for index, array in enumerate(arrays):
        total += array * (index - 1)
    return total


print(multiply_element_one_less_than_index(values))