numbers = [3, 4, 5, 6, 7]
# squares = []

# for number in numbers:
#     squares.append(number ** 2)

# print(squares)

squares = [number ** 2 for number in numbers]
print(squares)

rivers = ['Amazon', 'Nile', 'Yangtze']

river_lengths = [len(river) for river in rivers]
print(river_lengths)

expressions = ['lol', 'rofl', 'lmao']
cap_expressions = [expression.upper() for expression in expressions]
print(cap_expressions)

decimals = [4.95, 3.28, 1.08]

int_decimals = [int(decimal) for decimal in decimals]
print(int_decimals)