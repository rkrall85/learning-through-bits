#this script will get all the stores we support
#Would like to add insert and update functionality later

import item_track

class StoreItem():
    def __init__(self, db_connection,pd,item_id, user_id):
        self.db_connection  = db_connection
        self.pd             = pd
        self.item_id        = item_id
        self.user_id        = user_id

    def StoreItemProfile(self):
        supported_store_count   = self.GetSupportedStores()
        store_items_count       = self.GetStoreItems()
        missing_prompt = "Would you like to assign this item to a missing store?(enter quit to end): "
        missing_active = True
        if supported_store_count == store_items_count: missing_active = False
        #if missing_active: self.ShowMissingShows()
        #through all the times they want.
        while missing_active:
            self.ShowMissingShows()
            missing_store_message = input(missing_prompt)
            if missing_store_message == 'quit':
                missing_active = False
            else:
                missing_store_id = int(input("Please enter the store id:"))
                #New to insert new item_store
                self.CreateStoreItem(missing_store_id)
                supported_store_count   = self.GetSupportedStores()
                store_items_count       = self.GetStoreItems()
                if supported_store_count == store_items_count: missing_active = False

        #making sure user is tracking the item
        item_track.CreateUserItemTrack(self.db_connection, self.user_id, self.item_id)

    #Get store name and if its web scrapper
    def GetStoreInfo(self, store_id):
        sql = "exec [dbo].[usp_GetStoreInfo] {}".format(store_id)
        self.db_connection.execute(sql) #executing sproc
        data = self.db_connection.fetchone() #putting results into row class
        store_name = data[0] #getting id
        web_scrap = data[1] #flag to see if the store is web scrapable or not.
        return store_name, web_scrap

    #output a listing of all valid stores
    def GetSupportedStores(self):
        sql = "EXEC [dbo].[usp_GetSupportedStores];"
        lst_stores = self.db_connection.execute(sql)
        labels = ['Store ID', 'Store Name']
        df_stores = self.pd.DataFrame.from_records(lst_stores, columns=labels) #create dataframe from list
        #print (df_stores) #output dataframe
        self.db_connection.commit()#need this to commit transaction
        return len(df_stores.index)

    #get a list of stores that have the item they are trying track
    def GetStoreItems(self):
        sql = "EXEC [dbo].[usp_GetStoreItems] {}".format(self.item_id)
        self.db_connection.execute(sql)#, params) #executing sproc
        list_store_items = self.db_connection.fetchall()#[0] #fetchone will only return first result
        labels = ['store id','store name']
        df_store_items = self.pd.DataFrame.from_records(list_store_items, columns=labels) #create dataframe from list
        #print (df_store_items) #output dataframe
        self.db_connection.commit()#need this to commit transaction
        return len(df_store_items.index)

    #output all missing shows that are missing this item
    def ShowMissingShows(self):
        print("The following stores do not have this item assigned to them")
        sql = "EXEC [dbo].[usp_GetMissingStoreItems] {}".format(self.item_id)
        self.db_connection.execute(sql)#, params) #executing sproc
        list_missing_stores = self.db_connection.fetchall()
        labels = ['Store ID', 'Store Name']
        df_missing_stores = self.pd.DataFrame.from_records(list_missing_stores, columns=labels) #create dataframe from list
        print (df_missing_stores) #output dataframe
        self.db_connection.commit()#need this to commit transaction

    #Insert new item into a store
    def CreateStoreItem(self, store_id):
        store_info = self.GetStoreInfo(store_id)
        #checking if its a web scrap store entry
        if store_info[1].lower() == 'y':
            url = str(input("What is the URL of the item at {}?".format(store_info[0])))
            div = str(input("What is the div tag of the item at {}?".format(store_info[0])))
            span = str(input("What is the span of the item at {}?".format(store_info[0])))
            sql = "EXEC [dbo].[usp_CreateStoreItem] {}, {}, {}, {}, {}, {}".format(store_id, self.item_id,store_info[1],url, div, span)
            self.db_connection.execute(sql)
            self.db_connection.commit()#need this to commit transaction
            print("Item was added to {}".format(store_info[0]))
        #need other logic for api calls
        return
