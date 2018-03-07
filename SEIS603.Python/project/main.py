#main program to handle input from user.

#python libraries
import datetime as dt
import db_connection as dbconn
import pandas as pd

#various user scripts
import user_profile as usrprfl
import stores as strs
import items as itms
import item_track as itmtrck
import item_price_history as itmprchstry


db_connection = dbconn.database_connection()

#def main():
############Getting user profile information###################
current_user = str(input("Are you a user(y/n)?"))
user = usrprfl.User(db_connection, current_user = current_user)
user_profile = user.UserProfile()
user_id = user_profile[0]
first_name = user_profile[1]
#################################################################


######show current tracking of items#############################
print("You are currently tracking the following itmes at each store")
usrprfl.GetCurrentTracking(db_connection,user_id)
print(""*100)
#################################################################

track_new_item = str(input("Would you like to track a new item(y/n)?"))
if track_new_item.lower() ==  'y':
    ###########Gettting Store information#############################
    print("We currently support the following stores")
    lst_stores = strs.GetStores(db_connection)
    labels = ['Store ID', 'Store Name']
    df_stores = pd.DataFrame.from_records(lst_stores, columns=labels) #create dataframe from list
    print (df_stores) #output dataframe
    print(""*100)
    store_id = int(input("Which store would you like to start with? (Please enter store id)"))
    store_info = strs.GetStoreInfo(db_connection,store_id)
    store_name = store_info[0]
    web_scrap = store_info[1]
    #################################################################

    #######Getting Item information#################################
    print("We currently support the following items for {}".format(store_name))
    strs.GetStoreItems(db_connection=db_connection,pd = pd,store_id=store_id)
    new_item = str(input("Create a new item(y/n)?"))
    item_id = 0
    if new_item.lower() == 'y':
        item = itms.Item(db_connection, user_id = user_id,store_id = store_id,store_name  = store_name)
        new_item = item.CreateItem()
        item_id = new_item[0] #grab the item id
    else:
        item_id = int(input("Please enter the item id:"))

    track_item = itmtrck.Item(dt,db_connection, user_id = user_id,store_id = store_id,store_name  = store_name, item_id= item_id, web_scrap = web_scrap)
    track_item.TrackInput()
#################################################################


########Grab daily price (one item or all)###############################
track_item_daily = itmprchstry.ItemPrice(db_connection, item_id)
track_item_daily.CreateDailyPrice()
#################################################################
if item_id == 0:
    usrprfl.GetCurrentTracking(db_connection,user_id)
else:
    print("Summary of item you just set up for tracking")
    usrprfl.GetUserCurrentPriceItem(db_connection, pd, item_id, store_id, user_id)


##reporting done off of juypter####
