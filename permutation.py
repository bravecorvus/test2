def factorial(arg):
    accumulator = 1
    counter = arg
    while counter > 0:
        accumulator *= counter
        counter -= 1
    return accumulator

n = input("What do you want n to be?\n")
r = input("What do you want r to be?\n")

permutation = factorial(int(n))/(factorial(int(n)-int(r)))
print("\n=" + str(permutation))