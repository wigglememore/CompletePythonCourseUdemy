# use to repeat something a defined number of times
cheeses = ['cheddar', 'brie', 'stilton']
for name in cheeses:
    print(name)

# use underscore when you don't want to use the index in the loop
elements = [0, 1, 2, 3]
for _ in elements:
    print('Hi there')

# instead of creating an iterable you can just use
for _ in range(4):
    print('Hi there again')

# set intervals and limits on the range function
for index in range(2, 21, 3):
    print(index)

# just a lil' example
cheeses = (
    {'name': 'cheddar', 'strength': 2},
    {'name': 'stilton', 'strength': 9},
    {'name': 'brie', 'strength': 4}
)
for cheese in cheeses:
    name = cheese['name']
    strength = cheese['strength']
    print(f'The strength of {name} is {strength}')

# using the index in the loop
for i in range(1, 6):
    print(f'This is sentence number {i}')
