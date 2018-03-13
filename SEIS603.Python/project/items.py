

#s_id = 100
#u_id = 100


class Item():
    def __init__(self,dt, db_connection,user_id, store_id,store_name):
        self.dt                     = dt
        self.db_connection          = db_connection
        self.user_id                = user_id
        self.store_id               = store_id
        self.store_name             =  store_name


    def CreateItem(self):
        print("place holder for create item")
        #insert into item table as well as store_item table
        #need to return item id
        return 101

def GetItems(db_connection,pd):
    sql = "EXEC [dbo].[usp_GetItems];"
    db_connection.execute(sql)
    list_items = db_connection.fetchall()
    labels = ['ID','Brand','Name','Model','Description','UPC'] #might drop UPC
    df = pd.DataFrame.from_records(list_items, columns=labels) #create dataframe from list
    print (df) #output dataframe
    db_connection.commit()#need this to commit transaction



#def GetItemInfo(db_connect, item_id):
