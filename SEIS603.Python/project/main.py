#main program to handle input from user.

import  db_connection as d,user_info as ui,stores as s



connection = d.database_connection()
#def main():
############Getting user profile information###################
current_user = str(input("Are you a user(y/n)?"))
if current_user.lower() == 'y':
    user_name = str(input("Please enter your user name:"))
    user_profile = ui.User(user_name = 'robert.krall' )
    #if user_profile.GetUser()[0] != 0:
    print("Welcome back {}!".format(user_profile.GetUser()[1]))
else:
    print("Please answer the following questions to set up an account")
    user_name   = input("User Name:")
    first_name  = input("First Name:")
    last_name   = input("Last Name:")
    email       = input("email:")
    user_profile = ui.User(user_name,first_name,last_name, email)
    if user_profile.CreateUser()[0] != 0:
        print("You have successful created an account. Your user id is {}!".format(user_profile.GetUser()[0]))
#######################################################

################Listing stores######################
print("We currently support the following stores")
lst_stores = s.GetStores()
for i in (lst_stores):
    print("{} - {}".format(i[0],i[1]))


s_id = int(input("Which store would you like to start with? (Please enter store id)"))
store_name = s.GetStoreName(s_id)
print("Let's get started with price tracking for an item at {}".format(store_name))
#######################################################
