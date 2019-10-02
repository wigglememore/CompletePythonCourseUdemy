
print('Hello World!')

string = 'He said "Hi there" to the dog'
string2 = "They drove 'slowly' to their destination"
string3 = 'They decided to ''always'' use single quotation marks'
string_multiline = """This string
can go over
many lines"""
print(string_multiline)

client_name = 'Jess'
client_age = 37
greeting = 'Hi ' + client_name + ', you are ' + str(client_age) + ' years old'
print(greeting)
# f strings take the variable as input, changing variable doesn't change string
print(f'You are {client_age} years old and your name is {client_name}')

# .format is similar, but if you change the varialbe you change the string
greeting_template = 'Hi {}, you are {} years old, wow'
greeting_jess = greeting_template.format(client_name, client_age)
print(greeting_jess)
