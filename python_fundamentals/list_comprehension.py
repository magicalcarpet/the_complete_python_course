numbers = [0, 1, 2, 3, 4]
doubled_numbers = []

doubled_numbers = [number * 2 for number in numbers]


friends_ages = [22, 31, 36, 39]
age_strings = [f"My friend is {age} years old." for age in friends_ages]

print(age_strings)

names = ['Rolf', 'James', 'Jenny']
lower_case_names = [name.lower() for name in names]

print(lower_case_names)


friend = input("Enter your friend's name: ")
friends_list = ['Rolf', 'James', 'Jenny', 'Sam', "Anna"]
lower_case_friends = [name.lower() for name in friends_list]

if friend.lower() in lower_case_friends:
    print(f'{friend.title()} is one of your friends.')


