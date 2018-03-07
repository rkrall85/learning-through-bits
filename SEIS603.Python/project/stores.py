#this script will get all the stores we support
#Would like to add insert and update functionality later

def GetStores(db_connection):
    sql = "EXEC [dbo].[usp_GetStores];"
    db_connection.execute(sql)
    return db_connection.fetchall()#[0] #fetchone will only return first result



def GetStoreInfo(db_connection,s_id):
    sql = """\
            exec [dbo].[usp_GetStoreInfo] @s_id = ?;
        """
    params = (s_id,) #creating parms
    db_connection.execute(sql, params) #executing sproc
    data = db_connection.fetchone() #putting results into row class
    store_name = data[0] #getting id
    web_scrap = data[1] #flag to see if the store is web scrapable or not.
    return store_name, web_scrap



def GetStoreItems(db_connection,pd,store_id=0):
    sql = "EXEC [dbo].[usp_GetStoreItems] {}".format(store_id)
    db_connection.execute(sql)#, params) #executing sproc
    list_store_items = db_connection.fetchall()#[0] #fetchone will only return first result
    labels = ['item id','item name']
    df_store_items = pd.DataFrame.from_records(list_store_items, columns=labels) #create dataframe from list
    print (df_store_items) #output dataframe
    db_connection.commit()#need this to commit transaction
