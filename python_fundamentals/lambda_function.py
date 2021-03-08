def divide(x, y):
    return x / y


divide = lambda x, y: x / y
print(divide(12, 4))

def average(sequence):
    return sum(sequence) / len(sequence)

students = [
    {'name': 'Rolf', 'grades': (67, 90, 95, 100)},
    {'name': 'Bob', 'grades': (56, 78, 90, 90)},
    {'name': 'Rolf', 'grades': (98, 90, 95, 99)},
    {'name': 'Rolf', 'grades': (100, 100, 95, 100)},
]

for student in students:
    print(average(student['grades']))

