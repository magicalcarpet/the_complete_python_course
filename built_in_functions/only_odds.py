# Declare an only_odds function.
# It should accept a list of whole numbers.
# It should return a list with only the odd numbers from the original list.
# Do NOT use list comprehension.
#
# EXAMPLES:
# only_odds([1, 3, 5, 6, 7, 8])      =>  [1, 3, 5, 7]
# only_odds([2, 4, 6, 8])            =>  []


# def only_odds(array):
#     new_list = []
#     for item in array:
#         if item % 2 == 1:
#             new_list.append(item)
#     return new_list

def only_odds(array):
    return list(filter(lambda number: number % 2 == 1, array))

print(only_odds([1, 3, 5, 6, 7, 8]))
print(only_odds([2, 4, 6, 8]))



