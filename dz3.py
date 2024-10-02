def power_of_three():
    n = 0
    while True:
        yield 3 ** n
        n += 1

generator = power_of_three()

for i in range(10):
    print(next(generator))