# functions


cars = [
    {'make': 'Ford', 'mileage': 43222, 'fuel_consumed': 832},
    {'make': 'Toyota', 'mileage': 36930, 'fuel_consumed': 520},
    {'make': 'Mini', 'mileage': 6563, 'fuel_consumed': 34},
    {'make': 'Range Rover', 'mileage': 54226, 'fuel_consumed': 7632}
]


def calculate_mpg(car):
    mpg = car['mileage'] / car['fuel_consumed']
    name = car['make']
    # print(f'{name} runs at {mpg} miles per gallon')
    return name, mpg


for car_it in cars:
    name, mpg = calculate_mpg(car_it)
    car_it['mpg'] = mpg

print(cars)
