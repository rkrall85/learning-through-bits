#Robert Krall
#sumrange

#asking user for range
user_start  = int(input("Please enter starting number:"))
user_end    = int(input("Please enter ending number:"))

#loop through to sum the range
for num in range(user_start,user_end+1,1):
    if num == user_start:
        total = user_start
    else:
        total += num

#output restuls on screen
print("The range total between " + str(user_start)
        + " and " + str(user_end)
        + " is " + str(total))
