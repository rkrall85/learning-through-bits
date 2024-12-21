#Robert Krall
#midterm problem 2

#asking for numerator
numerator   = int(input("Please enter the numerator:"))

prompt="Please enter the denominator:"
active = False
#making sure denominator is not 0
while not(active):
    denominator = int(input(prompt))
    if denominator == 0:
        print("Please do not enter 0")
        active = False
    else:
        active = True

fraction = numerator / denominator
print("{0:.2f}".format(fraction))
