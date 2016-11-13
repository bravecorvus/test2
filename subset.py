from itertools import combinations
sets = combinations(range(1, 101), 4) # range is half-closed
print(len(filter(lambda s: sum(s) % 2 == 0, sets)))