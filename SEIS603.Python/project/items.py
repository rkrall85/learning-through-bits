

#s_id = 100
#u_id = 100


class TrackItem():
    def __init__(self, db_connection,user_id, item_id, store_id,item_price, item_purschase_date, item_url):
        self.db_connection = db_connection
        self.user_id = user_id
        self.item_id = item_id
        self.store_id = store_id
        self.item_price  = item_price
        self.item_purschase_date = item_purschase_date
        self.item_url = item_url

    def CreateStoreItem(self):
        sql = "EXEC [dbo].[usp_CreateStoreItem] {},{},'{}'".format(self.store_id,self.item_id, self.item_url)
        print(sql)
        self.db_connection.execute(sql)#, params) #executing sproc

    #def CreatePriceTrack(self):

def GetItems(db_connection):
    sql = "EXEC [dbo].[usp_GetItems];"
    db_connection.execute(sql)
    return db_connection.fetchall()#[0] #fetchone will only return first result

def CreateItem(db_connection):
    print("Create new item place holder")
