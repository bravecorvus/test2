# a4.py

n = []

# make a list of 1-9999
for x in range(1,10000):
    n.append(str(x))

# pad 0's to the front if the value is of lengh 3 or shorter
for count, data in enumerate(n):
    if len(data) == 4:
        continue
    elif len(data) == 3:
        n[count] = "0" + n[count]
    elif len(data) == 2:
        n[count] = "00" + n[count]
    elif len(data) == 1:
        n[count] = "000" + n[count]


# if there is a 0, then it must come after the first 2
for count, data in enumerate(n):
    for countinner, datainner in enumerate(n[count]):
        if datainner == "0":
            if countinner == 0:
                # n.remove(data)
                n[count] = 'aaaa'
            elif countinner == 1:
                if n[count][countinner-1] == "2":
                    continue
                else:
                    # n.remove(data)
                    n[count] = 'aaaa'
            elif countinner == 2:
                if n[count][countinner-1] == "2" or n[count][countinner-2] == "2":
                    continue
                else:
                    # n.remove(data)
                    n[count] = 'aaaa'
            elif countinner == 3:
                if n[count][countinner-1] == "2" or n[count][countinner-2] == "2" or n[count][countinner-3] == "2":
                    continue
                else:
                    # n.remove(data)
                    n[count] = 'aaaa'

#at least one 2.
for count, data in enumerate(n):
    if data[0] == '2' or data[1] == '2' or data[2] == '2' or data[3] == '2':
        continue
    else:
        n[count] = 'aaaa'


new_n = list(filter(('aaaa').__ne__, n))
a_4 = len(new_n)
print("a(4) = ", len(new_n))