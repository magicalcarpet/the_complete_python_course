age = int(input("Enter your age: "))
can_learn_programming = age > 0

print(f"You can learn programming: {can_learn_programming}.")

print(bool(35))
print(bool("Roger"))

x = True and False
print(x)

# In python 'and' works according to the rule:
# The second value is returned when the first value is True
y = 35 and 0
print(y)

# However, the first value is returned when it is False
z = 0 and 35
print(z)

# Or will return the first value when it is True or the second if it is True
i = 35 or 0
print(i)

k = 0 and 35
print(k)

# An example use case, leave either surname or first name blank

firstname = input("Enter first name: ")
surname = input("Enter your surname: ")

greeting = firstname or f"Mr. {surname}"
print(greeting)


print(not True)
print(not False)
print(not 35)

