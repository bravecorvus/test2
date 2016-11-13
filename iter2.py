numsequences = 2450
middlenumber = 51
total = 80850
doublecounter = 0

while(middlenumber <= 100):
    if(middlenumber > 51):
        doublecounter -= 2
    numsequences += doublecounter
    total += numsequences
    middlenumber+=1
    print("Middle Number")
    print(middlenumber)
    print("\n")
    print("number of sequences")
    print(numsequences)
    print("\n")
    print("total")
    print(total)
    print("\n")



# print(n)