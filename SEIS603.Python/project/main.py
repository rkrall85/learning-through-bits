#main program to handle input from user.

#python libraries
import datetime as dt
import db_connection as dbconn
import pandas as pd

#various user scripts
import user_profile as usrprfl
import store_item
import items
import item_track
import item_price_history

db_connection = dbconn.database_connection()

#def main():
############Getting user profile information###################
current_user = str(input("Are you a user(y/n)?"))
user = usrprfl.User(db_connection, current_user = current_user)
user_profile = user.UserProfile()
user_id = user_profile[0]
first_name = user_profile[1]
#################################################################


######Current Items Tracking Tracking Items#######################
print("You are currently tracking the following itmes")
item_track.GetCurrentTracking(db_connection,pd,user_id)
print("*"*75)
print("Current prices at items tracking")
item_track.GetUserItemTrackPrices(db_connection=db_connection,pd=pd,user_id=user_id, item_id="NULL")
print("*"*75)
#################################################################

####Track New Item##############################################
track_new_item = str(input("Would you like to track a new item(y/n)?"))
item_id = 0
if track_new_item.lower() ==  'y':
    print("Current Items supported")
    items.GetItems(db_connection,pd)
    item_listed = str(input("Is your item listed(y/n)?"))
    if item_listed == 'n':
        print("place holder for new item")
        new_item = items.Item(db_connection, pd)
        item_id = new_item.CreateItem()
        print(item_id)
    else:
        item_id = int(input("Please enter the item id:"))
    #item_track.CreateUserItemTrack(db_connection=db_connection,user_id=user_id, item_id=item_id)
########Attached Item to Store(s)#####################################
    #out put all stores that item is attached to
    store_items = store_item.StoreItem(db_connection=db_connection,pd=pd,item_id=item_id, user_id = user_id)
    store_items.StoreItemProfile()
#####################################################################


#####Grab Current website prices#################################
if item_id == 0: item_id = "NULL" #convert to null for sproc to grab all items
#issue with babies r us web scrap
get_daily_price = str(input("Would you like to get the daily price of items tracked(y/n)?"))
if get_daily_price.lower() == 'y':
    track_item_daily = item_price_history.ItemPrice(db_connection, item_id=item_id)
    track_item_daily.CreateDailyPrice()
get_item_prices = str(input("Would you like to view current prices on items(y/n)?"))
if get_item_prices.lower() == 'y':
    item_track.GetUserItemTrackPrices(db_connection=db_connection,pd=pd,user_id=user_id, item_id=item_id)
#################################################################

#################################################################

##reporting done off of juypter####
