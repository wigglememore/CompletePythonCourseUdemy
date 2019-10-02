# booleans are True and False (note capitals)

age = int(input('Enter your age: '))
# boolean comparitor
is_over_age = age >= 15
is_twenty = age == 20
print(f'The statement "You are over 14" is {is_over_age}')
print(f'The statement "You are 20 years old" is {is_twenty}')

age2 = int(input('Enter your age: '))
# 'and' and 'or'
can_use_knex = age2 > 5 and age2 < 17
print(f'You can use knex: {can_use_knex}')

# zeros and empty strings resolve to false
print(bool(35))
print(bool(0))
print(bool(12))

first_name = input('Enter your first name: ')
surname = input('Enter your surname: ')
greeting_name = first_name or f'Ms. {surname}'
print(f'Hello {greeting_name}')
