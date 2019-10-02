# when defining a function, giving a parameter a value is its default value
# if one parameter has a default value, all subsequent parameters must also
# when the function is defined, the default values are stored, they cannot be changed
# therefore it is highly discouraged use a variable as a default value


def addition(a, b=6):
    return a + b


# uses 3 as the value for b
print(addition(4, 3))
# if no value is passed in for b, the default of 6 is used
print(addition(4))
# you can use the parameter name when you call a function
# this is called a named argument, makes it clear what each number is for
print(addition(a=4, b=1))
# you can't call an argument without a name, after an argument with a name
# print(addition(a = 4, 9)) would give an error
# you can do it the other way around though
# print(addition(4, b=3)) is fine
