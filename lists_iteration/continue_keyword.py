def sum_of_positive_numbers(values):
    total = 0

    for value in values:
        if value > 0:
            total += value
    return total