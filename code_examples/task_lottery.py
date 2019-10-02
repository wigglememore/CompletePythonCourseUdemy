import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(range(22), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

number_of_matches = []

for p in players:
    numbers_temp = p['numbers']
    matches = numbers_temp.intersection(lottery_numbers)
    number_of_matches.append(len(matches))

winnings = 100 ** max(number_of_matches)
index = number_of_matches.index(max(number_of_matches))

print('' + players[index]['name'] + ' won ' + str(winnings))

# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)
