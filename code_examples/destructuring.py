# if you for example have a tuple
exchange_rates = (0.75, 4.3)
# destructure the tuple into different variables
eur, rmb = exchange_rates
print(eur)
print(rmb)

# if you had a list of tuples
cheeses = [
    ('cheddar', 2),
    ('brie', 4),
    ('stilton', 9)
]
# you can destructure like so
for cheese, strength in cheeses:
    print(f'The strength of {cheese} is {strength}')
