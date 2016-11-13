def digit_sum(num):
  return sum( [ int(char) for char in str(num) ] )


userinp = 1
while(True):
    if(userinp == "done"):
        break
    else:
        userinp = input("What number do you want to get the digit sum of?\n")
        third = 8 * int(userinp)
        theinput = int(userinp) + 8 + third
        dasum = digit_sum(theinput) 
        print(str(dasum))
