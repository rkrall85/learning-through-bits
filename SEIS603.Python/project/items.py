

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



def GetItems(db_connection):
    sql = "EXEC [dbo].[usp_GetItems];"
    db_connection.execute(sql)
    return db_connection.fetchall()#[0] #fetchone will only return first result

def GetStoreItems(db_connection, store_id):
    sql = "EXEC [dbo].[usp_GetStoreItems] {}".format(store_id)
    db_connection.execute(sql)#, params) #executing sproc
    list_store_items = db_connection.fetchall()#[0] #fetchone will only return first result
    labels = ['item id','item name']
    df_store_items = pd.DataFrame.from_records(list_store_items, columns=labels) #create dataframe from list
    print (df_store_items) #output dataframe
    db_connection.commit()#need this to commit transaction
