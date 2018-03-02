#main program to handle input from user.

import datetime as dt

import db_connection as d
import user_info as ui
import stores as s
import items as it


db_connection = d.database_connection()




def PriceTrackInput(db_connection):
    print("We currently support the following stores")
    lst_stores = s.GetStores(db_connection)
    print("Store ID - Store Name")
    print("_"*100)
    for i in (lst_stores):
        print("{} - {}".format(i[0],i[1]))

    s_id = int(input("Which store would you like to start with? (Please enter store id)"))
    store_name = s.GetStoreName(db_connection,s_id)
    print("Let's get started with price tracking for an item at {}".format(store_name))

    print("We currently support the following items")
    lst_items = it.GetItems(db_connection)
    print("Brand - Name(ID) - Model - Description - UPC")
    print("_"*100)
    for i in (lst_items):
        #brand - Name (ID) - model - desc - UPC
        print("{} - {}({}) - {} - {} - {}".format(i[1],i[2],i[0],i[3],i[4],i[5]))

    #add function to add new item
    new_item = input("Item missing and want to add it?")
    if new_item == 'y': it.CreateItem(db_connection)
    i_id = int(input("Please enter a item ID:"))
    i_price = input("What price did you pay?")
    i_purchase_date = input("When did you purchase the item (mm/dd/yyyy)?")
    month, day, year = map(int, i_purchase_date.split('/'))
    i_date = dt.date(year, month, day)
    i_url = input("What is the URL of the item from {}:".format(store_name))

    return i_id, s_id,i_price, i_date, i_url



#def main():
############Getting user profile information###################

current_user = str(input("Are you a user(y/n)?"))
if current_user.lower() == 'y':
    user_name = str(input("Please enter your user name:"))
    user_profile = ui.User(db_connection,user_name = 'robert.krall' )
    #if user_profile.GetUser()[0] != 0:
    print("Welcome back {}!".format(user_profile.GetUser()[1]))
    user_id = user_profile.GetUser()[0]
else:
    print("Please answer the following questions to set up an account")
    user_name   = input("User Name:")
    first_name  = input("First Name:")
    last_name   = input("Last Name:")
    email       = input("email:")
    user_profile = ui.User(db_connection,user_name,first_name,last_name, email)
    if user_profile.CreateUser()[0] != 0:
        print("You have successful created an account. Your user id is {}!".format(user_profile.GetUser()[0]))
        user_id = user_profile.GetUser()[0]
#######################################################
price_track = input("Would you like to price track a new item?(y/n)")
if price_track.lower() == 'y':
    #call price track py scirpt
    price_input = PriceTrackInput(db_connection)
    item_id = price_input[0]
    store_id = price_input[1]
    item_price = price_input[2]
    item_purschase_date = price_input[3]
    item_url = price_input[4]
    track_item = it.TrackItem(db_connection,user_id,item_id,store_id, item_price, item_purschase_date, item_url)
    #track_item.CreateStoreItem() #create new store item #wont insert values for some reason




#ask about reporting



db_connection.close()
