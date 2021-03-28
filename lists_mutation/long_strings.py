# Define a long_strings function that accepts a list of strings. 
# It should return a new list consisting of only the strings that 
# have 5 characters or more.
#
# EXAMPLES
# long_strings(["Hello", "Goodbye", "Sam"])  => ["Hello", "Goodbye"]
# long_strings(["Ace", "Cat", "Job"])        => []
# long_strings([])                           => []

def long_strings(array):
    new_list = []
    for item in array:
        if len(item) >= 5:
            new_list.append(item)
    return new_list

print(long_strings(["Hello", "Goodbye", "Sam"]))
print(long_strings(["Ace", "Cat", "Job"]) )
print(long_strings([]))