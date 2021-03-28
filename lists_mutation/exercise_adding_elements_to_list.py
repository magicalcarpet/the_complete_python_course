# Write a factors function that accepts a positive whole number
# It should return a list of all of the number's factors in ascending order
# HINT: Could the range function be helpful here? Or maybe a while loop?
#
# EXAMPLES
# factors(1)  => [1]
# factors(2)  => [1, 2]
# factors(10) => [1, 2, 5, 10]
# factors(64) => [1, 2, 4, 8, 16, 32, 64]

def factors(numbers):
    new_list = []
    for item in range(numbers+1):
        if item == 0:
            continue
        elif numbers % item == 0:
            new_list.append(item)
    return new_list 

print(factors(1))
print(factors(2))
print(factors(10))
print(factors(64))

# Or

def factors(numbers):
    new_list = []
    last_item = [numbers]
    for item in range(numbers):
        if item == 0:
            continue
        elif numbers % item == 0:
            new_list.append(item)
    return new_list + last_item