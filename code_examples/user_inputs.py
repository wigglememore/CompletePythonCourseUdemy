user_name = input('Enter your name: ')
print(f'Your name is {user_name}')
# input returns a string type, turn into int for mathematical opeartions
user_age = input('Enter your age: ')
print(f'You have lived for {int(user_age)*12} months')
# ORRRRRRR
user_age = int(input('Enter your age: '))
months = user_age * 12
print(f'You have lived for {months} months')
