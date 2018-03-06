

#s_id = 100
#u_id = 100


class Item():
    def __init__(self, db_connection,user_id, item_id, store_id,item_price, item_purschase_date, item_url):
        self.db_connection          = db_connection
        self.user_id                = user_id
        self.item_id                = item_id
        self.store_id               = store_id
        self.item_price             = item_price
        self.item_purschase_date    = item_purschase_date
        self.item_url               = item_url

    def StoreItem(self):
        sql = "EXEC [dbo].[usp_CreateStoreItem] {},{},'{}'".format(self.store_id,self.item_id, self.item_url)
        self.db_connection.execute(sql)#, params) #executing sproc
        self.db_connection.commit()#need this to commit transaction

    def TrackItem(self):
        sql =  """\
                DECLARE	@user_id INT,
	                       @item_id INT,
	                       @store_id int,
	                       @price DEC(8,2),
	                       @purchase_date DATE,
	                       @message VARCHAR(50);
                exec [dbo].[usp_CreateUserItemTrack] @user_id = ?,
                                             @item_id = ?,
                                             @store_id = ?,
                                             @price = ? ,
                                             @purchase_date = ?,
                                             @message = @message OUTPUT;
                Select @message;
            """
        params = (self.user_id,self.item_id,self.store_id,self.item_price,self.item_purschase_date,) #creating parms
        self.db_connection.execute(sql, params) #executing sproc
        data = self.db_connection.fetchone() #putting results into row class
        message = data[0]
        self.db_connection.commit()#need this to commit transaction
        return message



def GetItems(db_connection):
    sql = "EXEC [dbo].[usp_GetItems];"
    db_connection.execute(sql)
    return db_connection.fetchall()#[0] #fetchone will only return first result


def CreateItem(db_connection):
    print("Create new item place holder")
