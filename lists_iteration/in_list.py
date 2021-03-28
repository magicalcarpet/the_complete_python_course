# Define an in_list function that accepts a list of strings and a separate string.
# Return the index where the string exists in the list.
# If the string does not exist, return -1.
# Do NOT use the find or index methods.
#
# EXAMPLES
# strings = ["enchanted", "sparks fly", "long live"]
# in_list(strings, "enchanted")  ==> 0
# in_list(strings, "sparks fly") ==> 1
# in_list(strings, "fifteen")    ==> -1
# in_list(strings, "love story") ==> -1

def in_list(strings, target):
    for index, element in enumerate(strings):
        if element == target:
            return index
    return -1


strings = ["enchanted", "sparks fly", "long live"]

print(in_list(strings, 'enchanted'))
print(in_list(strings, 'sparks fly'))
print(in_list(strings, 'fifteen'))
print(in_list(strings, 'love story'))