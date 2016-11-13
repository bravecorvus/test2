total = 0

for i in range(0,101):
    if (i-1) % 3 == 0:
        print(i)
        total += 1

print("The number of 3 divisible elements is ", total)