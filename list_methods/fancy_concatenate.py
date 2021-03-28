# Define a fancy_concatenate function that accepts a list of lists of strings
# The function should return a concatenated string
# The strings in a list should only be concatenated if the length of 
# the list is 3
#
# EXAMPLES
# fancy_concatenate([["A", "B", "C"]])                        => "ABC"
# fancy_concatenate([["A", "B", "C"], ["D", "E", "F"]])       => "ABCDEF"
# fancy_concatenate([["A", "B", "C"], ["D", "E", "F", "G"]])  => "ABC"
# fancy_concatenate([["A", "B", "C"], ["D", "E"]])            => "ABC"
# fancy_concatenate([["A", "B"], ["C", "D"]])                 => ""

def fancy_concatenate(array_of_arrays):
    concat_box = []
    join_concat = ""
    for outer in array_of_arrays:
        for inner in outer:
            if len(outer) == 3:
                concat_box.append(inner)
                join_concat = "".join(concat_box)
    return join_concat


print(fancy_concatenate([["A", "B", "C"]]))
print(fancy_concatenate([["A", "B", "C"], ["D", "E", "F"]]))
print(fancy_concatenate([["A", "B", "C"], ["D", "E", "F", "G"]]))
print(fancy_concatenate([["A", "B", "C"], ["D", "E"]]))
print(fancy_concatenate([["A", "B"], ["C", "D"]]))

