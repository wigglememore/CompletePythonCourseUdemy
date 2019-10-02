cheeses = [
    'cheddar',
    'brie',
    'stilton',
    'blue',
    "feta"
]
# print out the list
print(', '.join(cheeses))
# print the 2nd and 3rd elements of the list (remember lists start at 0)
print(', '.join(cheeses[2:4]))
# print out everything after the first element
print(', '.join(cheeses[1:]))
# print out everything before the fourth one
print(', '.join(cheeses[:3]))
# you can index negatives (e.g. starting three in from the end)
print(', '.join(cheeses[-3:4]))
# similarly (e.g. if you wanted everything apart from the last two)
print(', '.join(cheeses[:-2]))
