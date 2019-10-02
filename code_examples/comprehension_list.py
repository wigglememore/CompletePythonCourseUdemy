numbers = [1, 5, 4, 9, 12]

# to double them all without list comprehension you would have to do
numbers_times_two = []
for n in numbers:
    numbers_times_two.append(n * 2)

# with list comprehension it looks like
numbers_times_two_good = [n * 2 for n in numbers]

print(numbers_times_two)
print(numbers_times_two_good)

# can also create lists like this
list_of_fives = [5 for number in range(5)]
print(list_of_fives)
