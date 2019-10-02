grades = [80, 95, 72, 54]

total = sum(grades)
length = len(grades)
average = total/length
print(f'The average grade is {average}')

# for this use case, a set is the worse choice as you can't have multiples
# a tuple isn't great because you can't add grades easily
# a list is great

# if you're not adding grades then a tuple is preferred over a list
# if you want to compare two lots of grades then a set is good
