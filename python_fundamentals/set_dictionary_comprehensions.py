friends = ['Rolf', 'james', 'Sam', 'alex', 'Louise']
guests = ['jose', 'benjamin', 'Mark', 'Alex', 'Sophie', 'michelle', 'rolf']

friends_lower = {name.lower() for name in friends}
guests_lower = {name.lower() for name in guests}

present_friends = friends_lower.intersection(guests_lower)
print(present_friends)

present_friends = {name.title() for name in present_friends}
print(present_friends)

time_since_seen = [3, 7, 15, 11, 8]

long_timers = {
    friends[i]: time_since_seen[i]
    for i in range(len(friends))
}

print(long_timers)