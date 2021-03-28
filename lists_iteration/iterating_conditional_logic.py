values = [3, 6, 9, 12, 15, 18, 21, 24]
other_values = [5, 10, 15, 20, 25, 30]

def odds_sum(array):
    sum = 0
    for element in array:
        if element % 2 == 1:
            sum += element
    return sum


print(odds_sum(values))
print(odds_sum(other_values))