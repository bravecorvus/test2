# recurrancechecker.py
import a2
from a2 import a_2
import a3
from a3 import a_3
import a4
from a4 import a_4
import a5
from a5 import a_5

x = 1000
y = 1000
xlist = []
ylist = []
for n in range(0, x):
    xlist.append(n)

for n in range(0, y):
    ylist.append(n)



# checking for x * a(n-1)
for n in xlist:
    if (n*a_4) == a_5 and (n*a_3) == a_4 and (n*a_2) == a_3:
        print("Recurrance Relation is a(n) = ", n, "a(n-1)\n")

# checking for x * a(n-1) +/- y * a(n-2) and y * a(n-2) - x * a(n-1)
for n in xlist:
    for z in ylist:
        if (n*a_4) + (z*a_3) == a_5 and (n*a_3) + (z*a_2) == a_4:
            print("Recurrance Relation is a(n) =", n, "a(n-1) +", z, "a(n-2)\n")
        elif (n*a_4) - (z*a_3) == a_5 and (n*a_3) - (z*a_2) == a_4:
            print("Recurrance Relation is a(n) =", n, "a(n-1) -", z, "a(n-2)\n")
        elif (z*a_3) - (n*a_4) == a_5 and (z*a_2) - (n*a_3) == a_4:
            print("Recurrance Relation is a(n) =", n, "a(n-2) - ", z, "a(n-1)\n")


# checking for a(n-1)^x
for n in xlist:
    if a_4^n == a_5 and a_3^n == a_4 and a_2^n == a_3:
        print("Recurrance Relation is a(n) = a(n-1)^", n)



# checking for a(n-1)^x + a(n-2)^y, a(n-1)^x - a(n-2)^y, a(n-2)^y - a(n-1)^x
for n in xlist:
    for z in ylist:
        if a_4^n + a_3^z == a_5 and a_3^n + a_2^z == a_4:
            print("Recurrance Relation is a(n) = a(n-1)^", n, " + a(n-2)^", z)
        elif a_4^n - a_3^z == a_5 and a_3^n - a_2^z == a_4:
            print("Recurrance Relation is a(n) = a(n-1)^", n, " - a(n-2)^", z)
        elif a_3^z - a_4^n == a_5 and a_2^z - a_3^n == a_4:
            print("Recurrance Relation is a(n) = a(n-2)^", z, " - a(n-1)^", x)

