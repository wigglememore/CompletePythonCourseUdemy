cheese_strengths = {
    'cheddar': 2,
    'brie': 4,
    'stilton': 9
}

# to loop over keys
for name in cheese_strengths:
    print(name)

# to loop over values
for strength in cheese_strengths.values():
    print(strength)

# to have both keys and values
for name, strength in cheese_strengths.items():
    print(f'{name} has strength {strength}')
