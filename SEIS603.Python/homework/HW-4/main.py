#Robert Krall
#main.py

import calendar


def input_function():
    user_year = int(input("Please enter a year:")) #ask user for year
    #if year is less than 1582 they need to reenter the year
    if user_year < 1582:
        print("Please enter a year greater than 1582")
        input_function()
    else:
        #step 1
        if user_year % 4==0:
            #step 2
            if user_year % 100 == 0:
                #step 3
                if user_year % 400 == 0:
                    leap_year(user_year=user_year)
                else:
                    not_leap(user_year=user_year)
            else:
                leap_year(user_year=user_year)
        else:
            not_leap(user_year=user_year)
#step 4
def leap_year(user_year):
    print("{} is a leap year!".format(user_year))
    get_day_count(user_year=user_year)

#step 5
def not_leap(user_year):
    print("{} is not a lear year.".format(user_year))
    get_day_count(user_year=user_year)

#output how many days are in the year entered
def get_day_count(user_year):
    print ('There is'
            ,366 if calendar.isleap(user_year) else 365
            ,' days in {}'.format(user_year))

#start the program
input_function()
