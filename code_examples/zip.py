# this is used to combine two lists in such a way that they can be passed through dict
# unlike when using a dictionary comprehension, ,you can't use any conditionals

cheeses = ['Brie', 'Cheddar', 'Stilton', 'Port Salut']
strengths = [4.5, 2, 7, 3]

# creates a new list where each element is a tuple of elements
# zip can be used to combine any number of lists
combined = list(zip(cheeses, strengths))
print(combined)

dictionary = dict(combined)
print(dictionary)

# can combine into dict(zip(cheeses, strengths))
