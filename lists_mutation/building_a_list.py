powerball_numbers = [4, 8, 15, 16, 23, 42]

def squares(numbers):
    squared_numbers = []
    for number in numbers:
       squared_numbers.append(number * number)
    return squared_numbers



print(squares(powerball_numbers)) 


def convert_to_float(numbers):
    floated = []
    for number in numbers:
        floated.append(float(number))
    return floated

print(convert_to_float(powerball_numbers))

def even_or_odd(numbers):
    new_list = []
    for number in numbers:
        if number % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
    

print(even_or_odd(powerball_numbers))