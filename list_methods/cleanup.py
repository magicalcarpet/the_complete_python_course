# Define a cleanup function that accepts a list of strings.
# The function should return the strings joined together by a space.
# There's one BIG problem -- some of the strings are empty or only 
# consist of spaces!
# These should NOT be included in the final string
#
# cleanup(["cat", "er", "pillar"])           => "cat er pillar"
# cleanup(["cat", " ", "er", "", "pillar"])  => "cat er pillar"
# cleanup(["", "", " "])                     => ""

def cleanup(array):
    clean_array = []

    for item in array:
        if item.isspace() or len(item) == 0:
            continue
        clean_array.append(item)
    return " ".join(clean_array)
    



print(cleanup(["cat", "er", "pillar"]) )
print(cleanup(["cat", " ", "er", "", "pillar"]))
print(cleanup(["", "", " "]))