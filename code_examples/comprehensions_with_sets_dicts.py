friends = ['Bob', 'harry', 'Sam', 'Jill', 'Kate']
guests = ['Susan', 'Finley', 'pete', 'jill', 'bob']

friends_lower = {f.lower() for f in friends}
guests_lower = {g.lower() for g in guests}

# this method removed duplicate elements (which oculd be good or bad depending on your use)

present = {name.title() for name in friends_lower.intersection(guests_lower)}

print(present)


cheeses = ['Brie', 'Cheddar', 'Stilton', 'Port Salut']
strengths = [4.5, 2, 7, 3]

cheese_strengths = {
    cheeses[i]: strengths[i]
    for i in range(len(cheeses))
    if strengths[i] > 4
}

print(cheese_strengths)
