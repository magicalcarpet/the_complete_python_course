metals = ['gold', 'silver', 'platinum', 'palladium']

print(list(filter(lambda metal: len(metal) > 5, metals)))
letter = 'p'
print(list(filter(lambda letter: 'p' in letter, metals)))

print(list(map(lambda word: word.count('l'), metals)))

# Write a function to compute 3x + 1

def func(x):
    return 3*x + 1

print(func(2))


g = lambda x: 3*x + 1
print(g(2))

# Combine first and last name into a single 'Full Name'

full_name = lambda first_name, last_name: first_name.strip().title() +\
    " "+ last_name.strip().title()

print(full_name("    leonard ", ' EULER'))

sci_fiction_authors = ['Isaac Asimov', 'Ray Bradbury',
                        'Robert Heinlein',
                        'Arthur C. Clarke',
                        'Frank Herbert',
                         'Orson Scott Card',
                          'Douglas Adams',
                           'H.G. Wells',
                            'Leigh Brackett'
                    ]

sci_fiction_authors.sort(key=lambda name: name.split(" ")[-1].lower())
print(sci_fiction_authors)


