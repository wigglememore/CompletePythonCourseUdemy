scores = [87, 94, 56, 80, 61]

# to break out of a loop
for status in scores:
    if status < 60:
        print(f'This student failed with a score of {status}.')
        break
    print(f'This student scored {status} on their test.')
    print('Sending report')

print('_______________________')
# to skip an iteration in a loop
for status in scores:
    if status < 60:
        print(f'This student failed with a score of {status}, going to next student.')
        continue
    print(f'This student scored {status} on their test.')
    print('Sending report')

print('_______________________')
# NEWB approach to printing something if everyone passes
all_passed = True

for status in scores:
    if status < 60:
        print(f'This student failed with a score of {status}, going to next student.')
        all_passed = False
        continue
    print(f'This student scored {status} on their test.')
    print('Sending report')

if all_passed:
    print('All the students passed')

print('_______________________')
# good approach to printing something if everyone passes
for status in scores:
    if status < 60:
        print(f'This student failed with a score of {status}, going to next student.')
        break
    print(f'This student scored {status} on their test.')
    print('Sending report')
else:
    print('All the students passed')
# else will go if the loop is NOT broken
