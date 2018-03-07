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
    print("Let's get started with price tracking for an item at {}".format(store_name))
    #################################################################

    #######Getting Item information#################################
    print("We currently support the following items for {}".format(store_name))
    itms.GetStoreItems(db_connection=db_connection, store_id=store_id)
    new_item = str(input("Create a new item(y/n)?"))
    item_id = 0
    if new_item.lower() == 'y':
        item = itms.Item(db_connection, user_id = user_id,store_id = store_id,store_name  = store_name)
        new_item = item.CreateItem()
        item_id = new_item[0] #grab the item id

    #if item_id == 0: item_id = int(input("Enter Item ID:"))
'''
current_track = str(input("Track item(y/n)?"))
if current_track.lower() == 'y':
    track_item = itmtrck.Item(dt,db_connection, user_id = user_id,store_id = store_id,store_name  = store_name, item_id= item_id, web_scrap = web_scrap)
    track_item.TrackInput()
    web_scrap = track_item[0]
    item_url = track_item[1]
    item_web_class = track_item[2]
else:
    user_track_items = itmtrck.GetuserTrackItem(db_connection, user_id = user_id, item_id= item_id, store_id= store_id )
    web_scrap = user_track_items[0]
    item_url = user_track_items[1]
    item_web_class = user_track_items[2]
'''
#################################################################


########Grab daily price all items###############################
track_item_daily = itmprchstry.ItemPrice(db_connection)
track_item_daily.CreateDailyPrice()
#################################################################








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
