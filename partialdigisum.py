def digit_sum(num):
  return sum( [ int(char) for char in str(num) ] )





userinp = 1
while(True):
    userinp = input("What number do you want to get the digit sum of?\n")
    if(userinp == "done"):
        break
    else:
        dasum = digit_sum(int(userinp)) 
        print(str(dasum))
