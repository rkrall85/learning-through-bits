#Robert Krall
#mileage.py



'''
Write a program that will compute MPG for a car.
Prompt the user to enter the number of miles driven and the number of gallons used.
Print a nice message with the answer.
'''


miles_driven        = int(input("Please enter the miles you drive: "))
num_of_gals_used    = int(input("Please enter gallons of gas used: "))

mpg = miles_driven // num_of_gals_used

print("The MPG for your car is " + str(mpg))
