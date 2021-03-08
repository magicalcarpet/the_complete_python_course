def add(x, y):
    total = x + y
    return total

print(add(5, 10))

def add(x, y=3):
    total = x + y
    return total

print(add(5))
print(add(5, 7))

print(add(x=2))
print(add(x=8, y=4))


print(1, 2, 3, 4, 5)
print(1, 2, 3, 4, 5, sep=' - ')

# The default value is stored at the definition of the function
# as shown in the following example

default_y = 3

def add(x, y=default_y):
    total = x + y
    print(total)

add(6)
# When the value of the variable is changed, the output is the same

default_y = 25
add(6)

