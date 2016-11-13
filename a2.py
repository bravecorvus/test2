# a2.py

n = []

# make a list of 1-99
for x in range(1,100):
    n.append(str(x))

# pad 0's to the front if the value is of lengh 1
for count, data in enumerate(n):
    if len(data) == 2:
        continue
    elif len(data) == 1:
        n[count] = "0" + n[count]

# if there is a 0, then it must come after the first 2
for count, data in enumerate(n):
    for countinner, datainner in enumerate(n[count]):
        if datainner == "0":
            if countinner == 0:
                # n.remove(data)
                n[count] = 'aa'
            elif countinner == 1:
                if n[count][countinner-1] == "2":
                    continue
                    # n.remove(data)
                else:
                    n[count] = 'aa'
#at least one 2.
for count, data in enumerate(n):
    if data[0] == '2' or data[1] == '2':
        continue
    else:
        n[count] = 'aa'


new_n = list(filter(('aa').__ne__, n))
a_2 = len(new_n)
print("a(2) = ", len(new_n))