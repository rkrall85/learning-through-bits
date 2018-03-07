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
