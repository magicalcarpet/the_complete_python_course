countries = ['Italy', 'Greece', 'United Kingdom', 'Belgium']
index = 0

# for country in countries:
#     print(index, country)
#     index += 1


# for x in range(6):
#     print(x)

# for index in range(len(countries)):
#     print(index, countries[index])


# enumerated_countries = enumerate(countries)
# print(type(enumerated_countries))

# enumerated_countries = enumerate(countries)
# print(list(enumerated_countries))

# for country in enumerate(countries):
#     print(country)

# for index, country in enumerate(countries):
#     print(index, country)

# for index, country in enumerate(countries, 50):
#     print(index, country)


# countries = ('Italy', 'Greece', 'United Kingdom', 'Belgium')

# for index, country in enumerate(countries):
#     print(index, country)

countries = [('Italy', 'Rome'), ('Greece', 'Athens'), ('United Kingdom', 'London'),
 ('Belgium', 'Brussels')]

print(countries[0][0])
print(countries[0][1])

for index, country in enumerate(countries):
    print(f"Index {index}: the capital of {country[0]} is {country[1]}")

country = 'Italy'
for index, character in enumerate(country):
    print(f"Character index {index} {character}")


