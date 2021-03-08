ages = [34, 87, 35, 31, 19, 44, 16]
odds = [age for age in ages if age % 2 == 1]

print(odds)


friends = ['Rolf', 'james', 'Sam', 'alex', 'Louise']
guests = ['jose', 'benjamin', 'Mark', 'Alex', 'Sophie', 'michelle', 'rolf']

lower_case_friends = [friend.lower() for friend in friends]
lower_case_guests = [guest.lower() for guest in guests]

present_friends = [ 
    name for name in lower_case_guests if name in lower_case_friends

]

print(present_friends)


