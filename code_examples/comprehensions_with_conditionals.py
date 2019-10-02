ages = [20, 54, 9, 95, 34]
odds = [age for age in ages if age % 2 == 1]

print(odds)

friends = ['Bob', 'harry', 'Sam', 'Jill', 'Kate']
guests = ['Susan', 'Finley', 'pete', 'jill', 'bob']

friends_lower = set([f.lower() for f in friends])
guests_lower = set([g.lower() for g in guests])
# because they are turned into sets the order gets lost
print(friends_lower.intersection(guests_lower))


friends_lower2 = [f.lower() for f in friends]
# this way keeps it as a list and doesn't make it into a set
# since they stay a set, the order of the elements in maintained
# .title() capitalises the first letter in the word
friends_comprehension = [
    name.title() for name in guests if name.lower() in friends_lower2
]

print(friends_comprehension)

# to split list comprehensions into multiple lines it usually goes like

# new_list_name = [
#   the elements of the new list
#   the iteration over the current list
#   the conditional
# ]
