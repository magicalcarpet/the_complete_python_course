friends_ages = {'Rolf': 25, 'Anna': 37, 'Charlie': 31, 'Bob': 23}

# for friend in friends_ages:
#     print(friend)

for age in friends_ages.values():
    print(age)

for friend, age in friends_ages.items():
    print(friend, age)


