

x = 0
while x < 3:
    print("x is currently: " + str(x))
    x+=1

print("Welcome agent")
passcode = 0
while passcode != 123:
    passcode = int(input('Please providie your passcode:'))

    if passcode != 123:
        print("Wrong password")
        print("please try again")
        print("\n")

print("good job correct passcode")


x = 0
while x < 10:
    print(x)
    x += 1
    if x ==3:
        break
