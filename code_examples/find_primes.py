for i in range(2, 10):
    # actually only have to check from 2 to sqrt(i)
    for j in range(2, i):
        if i % j == 0:
            print(f'{i} = {j} * {i/j}')
            break
            # the break only effects the closest for loop
    else:
        print(f'{i} is prime')
