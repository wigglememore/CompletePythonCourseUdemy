# lambda functions are used to take inputs and return outputs
# for example the print function would not be an example of a lambda function

# # a normal function might be something like
# def divide(a, b):
#     return a / b
#
# # to re-write this as a lambda function it would be
# divide_lambda = lambda a, b: a / b
# print(divide_lambda(8, 2))


# this is very uncommon and basically discouraged
# a more useful way to use lambda functions would be

operations = {
    'average': lambda seq: sum(seq) / len(seq),
    'total': sum,  # lambda seq: sum(seq),  # here you can see that the lambda function is useless
    'max': lambda seq: max(seq)  # you don't need the intermediary lambda function that call the 'sum' function
}

students = [
    {'name': 'carla', 'grades': [64, 87, 24, 98]},
    {'name': 'james', 'grades': [64, 87, 24, 53]},
    {'name': 'sylvia', 'grades': [20, 13, 24, 98]},
    {'name': 'daniel', 'grades': [74, 87, 34, 67]}
]

for student in students:
    name = student['name']
    grades = student['grades']

    print(f'For student {name} do you want to:')
    operation = input("Calculate 'average', 'total' or 'max' of their grades: ")

    result = operations[operation](grades)
    print(f"{name}'s {operation} is {result}")
