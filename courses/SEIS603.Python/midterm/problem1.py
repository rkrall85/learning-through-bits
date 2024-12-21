#Robert Krall
#mid term - problem 1

#making sure they only enter digits and not try to enter a letter
prompt="Please enter a number:"
active = False
while not(active):
    user_input = list(input(prompt))
    for i in user_input:
        if not(i.isdigit()):
            print("{} is not a digit".format(i))
            active = False
        else:
            active = True

#variables for counts
even_counter = 0
odd_counter = 0
zero_counter = 0

#loop through all the digits in the input
for i in range(len(user_input)):
    #grab current digit and cast to int
    current_digit = int(user_input[i])
    #determing if its a 0, even or odd number
    if current_digit == 0:
        zero_counter += 1
    elif current_digit % 2 == 0:
        even_counter += 1
    elif current_digit % 2 != 0:
        odd_counter += 1
    else:
        pass

#output the number of each digit type
print("odd: {}, even: {}, and zero: {}".format(odd_counter, even_counter, zero_counter))
