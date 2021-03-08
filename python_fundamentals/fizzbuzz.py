# Print out numbers from 1 to 100 (including 100).
# But, instead of printing multiples of 3, print "Fizz"
# Instead of printing multiples of 5, print "Buzz"
# Instead of printing multiples of both 3 and 5, print "FizzBuzz".

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# Usig a while loop

counter = 1

while counter < 101:
    if (counter % 3 == 0) and (counter % 5 == 0):
        print('FizzBuzz')
    elif counter % 5 == 0:
        print('Buzz')
    elif counter % 3 == 0:
        print('Fizz')
    else:
        print(counter)
    counter += 1

