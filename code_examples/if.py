number = 14
guess = int(input('Please enter a number: '))

if guess == number:
    print('Well done, you got it right')
else:
    print('Sorry, you got it wrong')

cheeses = ['cheddar', 'brie', 'stilton']
meats = ['beef', 'chicken', 'pork']

user_food = input('Please enter your favourite meat or cheese: ')

if user_food in cheeses:
    print('We like this cheese too')
elif user_food in meats:
    print('We like this meat too')
else:
    print('We do not like this food')
