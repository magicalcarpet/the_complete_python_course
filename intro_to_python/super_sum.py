# Define a super_sum function that accepts a list of strings. 
# The function should sum the index positions of the first occurence of the letter “s” in each word. 
#
# Not every word is guaranteed to have an “s”.
# Don’t use "sum" as a variable name as it’s a built-in keyword.
#
# super_sum([])                                 => 0
# super_sum(["mustache"])                       => 2
# super_sum(["mustache", "greatest"])           => 8
# super_sum(["mustache", "pessimist"])          => 4
# super_sum(["mustache", "greatest", "almost"]) => 12

def super_sum(array):
    total = 0
    for element in array:
        if 's' in element:
            index = element.index('s')
            total += index
    return total


print(super_sum([]))
print(super_sum(["mustache"]))
print(super_sum(["mustache", "greatest"]))
print(super_sum(["mustache", "greatest", "almost"]))