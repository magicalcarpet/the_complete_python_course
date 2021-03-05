friends_ages = {"Frank": 25, "Adam": 32, "Anna": 37}

friends_ages["Anthony"] = 41
friends_ages["Frank"] = 26

print(friends_ages)

chums = (
    {'name': 'Frank Smith', 'age': 23},
    {'name': 'Adam Wool', 'age': 32},
    {'name': 'Anna Pun', 'age': 37}
)

print(chums[0]['name'])
print(chums[1]['name'])
print(chums[2]['name'])

friends = [('Frank', 25), ('Adam', 32), ('Anna', 37)]
converted_friends = dict(friends)
print(converted_friends)

