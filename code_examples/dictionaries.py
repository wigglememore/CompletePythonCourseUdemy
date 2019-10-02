cheese_strengths = {
    'cheddar': 2,
    'brie': 4,
    'stilton': 9
}

cheddar_strength = cheese_strengths['cheddar']
print(f'The strength of cheddar is {cheddar_strength} out of 10')

# you can add entries
cheese_strengths['port salut'] = 3
# you can change definitions of values
cheese_strengths['brie'] = 5
print(cheese_strengths)

# for multiples you can use a tuple, or list, of dictionaries
cheeses = (
    {'name': 'cheddar', 'strength': 2},
    {'name': 'stilton', 'strength': 9}
)

# print(f'The cheese {cheeses[1]['name']} has strength {cheeses[1]['strength']}')

print(cheeses[1]['name'])

# you can turn a list into a dictionary very easily
cheese_squishieness = [
    ('cheddar', 1),
    ('brie', 8),
    ('stilton', 3),
]
print(cheese_squishieness)
cheese_squishieness_dictionary = dict(cheese_squishieness)
print(cheese_squishieness_dictionary)

brie_squishieness = cheese_squishieness_dictionary['brie']
print(brie_squishieness)
