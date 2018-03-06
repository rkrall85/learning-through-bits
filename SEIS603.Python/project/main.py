#main program to handle input from user.

import datetime as dt

import db_connection as d
import user_profile as up
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
user = up.User(db_connection, current_user = current_user)
user_profile = user.UserProfile()
user_id = user_profile[0]
first_name = user_profile[1]



print(user_id, first_name)

#print(user_name)

'''
#######################################################
price_track = input("Would you like to price track a new item?(y/n)")
if price_track.lower() == 'y':
    #call price track py scirpt
    track_input = PriceTrackInput(db_connection)
    item_id = track_input[0]
    store_id = track_input[1]
    item_price = track_input[2]
    item_purschase_date = track_input[3]
    item_url = track_input[4]
    #new_item = it.Item(db_connection,user_id,item_id,store_id, item_price, item_purschase_date, item_url)
    new_item = it.Item(db_connection = db_connection,user_id = user_id, item_id = item_id, store_id = store_id,item_price = item_price, item_purschase_date = item_purschase_date, item_url = item_url)
    #new_item.CreateStoreItem() #create new store item #wont insert values for some reason
    new_item.TrackItem()[0]
'''


#ask about reporting



#db_connection.close()
